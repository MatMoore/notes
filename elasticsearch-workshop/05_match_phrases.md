# Matching multiple terms

Instead of just looking for any matches of the individual search terms, we can require more of the terms to match.

Here are some examples of this that could be part of a larger query.

## All terms in order

The [match_phrase query](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/phrase-matching.html) considers the positions of the terms; documents only match if the relative offsets of the terms match the query terms.

  ```
  GET detailed,mainstream,government/_search
  {
     "query": {
        "match_phrase": {
           "title": {
              "query": "renew passport",
              "analyzer": "query_with_old_synonyms"
           }
        }
     }
  }
  ```

This gives:

- Don't score an own goal - renew your passport
- Allow plenty of time to renew your passport this summer
- MGN 419 Disposal of out of date pyrotechnics (marine flares)

### Wait, why is renewing your passport like disposing of out of date pyrotechnics?

Compare
```
GET mainstream/_analyze?analyzer=query_with_old_synonyms&text=MGN 419 Disposal of out of date pyrotechnics (marine flares)
```

and

```
GET mainstream/_analyze?analyzer=query_with_old_synonyms&text=renew a passport
```

(fixing this is left as an exercise for the reader)

### Precision vs recall
There's sometimes a trade off between *precision* and *recall*

- High precision means the **result set contains mostly relevant content**

- High recall means **most of the relevant content is in the result set**

![precision and recall](https://upload.wikimedia.org/wikipedia/commons/2/26/Precisionrecall.svg)

In this case, we lost a lot of recall. In particular "Renew or replace your adult passport" no longer appears in the results.

## All terms, close to each other

There's a `slop` parameter that allows the terms to be further apart in phrase queries.

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match_phrase": {
         "title": {
            "query": "book theory test",
            "slop": 2,
            "analyzer": "query_with_old_synonyms"
         }
      }
   }
}
```

If set to a higher value, then the words could appear in any order, but they all to have be present and close to each other.

## All terms, anywhere in the field
By default the `match` and `multi_match` queries return documents if *any* of the terms match.

You can change this to require *all* of the terms, using the `operator` field.

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {
         "title": {
            "query": "book theory test",
            "operator": "and",
            "analyzer": "query_with_old_synonyms"
         }
      }
   }
}
```

## Some terms, anywhere in the field

The [minimum_should_match](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-minimum-should-match.html#query-dsl-minimum-should-match) field specifies how many terms need to match,
depending on the number of terms in the query.

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {
         "title": {
            "query": "how to book driving test",
            "minimum_should_match": "2<75%",
            "analyzer": "query_with_old_synonyms"
         }
      }
   }
}
```

This example is equivalent to `"operator": "and"` for 1 or 2 term queries, but longer queries only need 75% of the terms to match.

> A positive integer, followed by the less-than symbol, followed by any of the previously mentioned specifiers is a conditional specification. It indicates that if the number of optional clauses is equal to (or less than) the integer, they are all required, but if it’s greater than the integer, the specification applies.

## N-grams

A [shingle filter](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/shingles.html) extracts bigrams or N-grams (fixed length groups of neighbouring words) from a series of tokens. We're analysing fields in this way at index time but not using them in queries.

Here's an example of how the filter treats a query:

```
GET mainstream/_analyze?analyzer=with_shingles&text=hand luggage restrictions
```

```json
{
   "tokens": [
      {
         "token": "hand luggag",
         "start_offset": 0,
         "end_offset": 12,
         "type": "shingle",
         "position": 1
      },
      {
         "token": "luggag restrict",
         "start_offset": 5,
         "end_offset": 25,
         "type": "shingle",
         "position": 2
      }
   ]
}
```

And an example query:

```
GET detailed,mainstream,government/_search
{
  "query": {
    "match": {
      "title.shingles": {
        "type": "boolean",
        "query": "hand luggage restrictions",
        "operator": "or"
      }
    }
  }
}
```

## Common terms
The [common terms](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-common-terms-query.html) query splits query terms into two sets depending on how many documents they appear in.

All terms get used for scoring, but we can specify that only the low frequency
ones get affected by `minimum_should_match`:

```
GET detailed,mainstream,government/_search
{
  "query": {
    "common": {
      "title": {
        "query": "when is the next bank holiday",
        "cutoff_frequency": 0.001,
        "low_freq_operator": "or",
        "minimum_should_match": 2,
        "analyzer": "query_with_old_synonyms"
      }
    }
  }
}
```
