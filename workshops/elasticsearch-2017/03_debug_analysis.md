# Debugging analysis

In the last exercise we saw that `vote` matched `voting`.

This is because the default analyzer used for the title field used stemming.

Let's look at how the index is configured:

```
GET mainstream/_settings
```

(Note: this endpoint won't work if you pass body JSON)

In here you should see the `default` analyzer:

```json
{
   "type": "custom",
   "char_filter": [
      "normalize_quotes",
      "strip_quotes"
   ],
   "filter": [
      "standard",
      "lowercase",
      "stop",
      "stemmer_override",
      "stemmer_english"
   ],
   "tokenizer": "standard"
},
```

`stemmer_english` is a standard stemmer for English language text, and `stemmer_override` is a GOV.UK filter that prevents some unwanted stemming. For example, we consider `governance` to be significantly different from `government`. We prevent these words from being stemmed to `govern` so we don't lose meaning.  

Both of these are examples of [token filters](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/analysis-tokenfilters.html), which make up the analyzer.

We can see what the analyzer does using the `analyze` API:

```
GET mainstream/_analyze?analyzer=default&text=voting
```

```json
{
   "tokens": [
      {
         "token": "vote",
         "start_offset": 0,
         "end_offset": 6,
         "type": "<ALPHANUM>",
         "position": 1
      }
   ]
}
```


## Changing analzers

Fields in documents can be analyzed in different ways at index time.

This is set in the mapping configuration:
```
GET mainstream/edition/_mapping
```

Here you can see the mapping for the `edition` document type. The `title` property is analyzed with multiple analyzers:

```json
{
   "type": "string",
   "fields": {
      "id_codes": {
         "type": "string",
         "analyzer": "with_id_codes"
      },
      "no_stop": {
         "type": "string",
         "analyzer": "searchable_text"
      },
      "shingles": {
         "type": "string",
         "analyzer": "with_shingles"
      },
      "sort": {
         "type": "string",
         "analyzer": "string_for_sorting"
      },
      "synonym": {
         "type": "string",
         "index_analyzer": "with_index_synonyms",
         "search_analyzer": "with_search_synonyms"
      }
   },
   "copy_to": [
      "spelling_text"
   ],
   "include_in_all": true
},
```

This makes extra fields available like `title.no_stop` (no stopwords) and `title.synonyms` (with synonyms).
Note: These fields are not used by rummager queries at the moment.

When querying those fields, we get the same analyzer applied to the search query.

Compare

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {"title.no_stop": "the a of an"}
   }
}
```

and

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {"title": "the a of an"}
   }
}
```

## Customizing the analyzer in the query
We can also use the standard field and apply a different analyzer at query time:

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {
          "title": {
            "query": "the dole",
            "analyzer": "query_with_old_synonyms"
          }
      }

   }
}
```

The top result should be Jobseeker's Allowance.

We can see how this works using the analyze API again:

```
GET mainstream/_analyze?analyzer=query_with_old_synonyms&text=the dole
```

```json
{
   "tokens": [
      {
         "token": "jobseek",
         "start_offset": 4,
         "end_offset": 8,
         "type": "SYNONYM",
         "position": 2
      },
      {
         "token": "allow",
         "start_offset": 4,
         "end_offset": 8,
         "type": "SYNONYM",
         "position": 3
      }
   ]
}
```

This is how synonyms work at the moment on GOV.UK.
