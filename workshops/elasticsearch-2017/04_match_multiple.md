# Matching multiple fields

So far we've just queried titles.

We can query multiple fields by replacing `match` with [multi_match](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/multi-match-query.html).

Let's compare `match` and `multi_match` using another query:

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {
         "title": {
            "query": "renew my passport",
            "analyzer": "query_with_old_synonyms"
         }
      }
   }
}
```

This returns 4182 results, with the most useful result in position 2.
- Consul in Italy warns Brits not to let their passport expire
- Renew or replace your adult passport
- Letting your passport expire can cost more than you think

Now, with the description field included:

```
GET detailed,mainstream,government/_search
{
   "query": {
      "multi_match": {
         "query": "renew my passport",
         "fields": [
            "title",
            "description"
         ],
         "analyzer": "query_with_old_synonyms"
      }
   }
}
```

This gives 13916 results, but the top results are less relevant:

- Consul in Italy warns Brits not to let their passport expire
- Letting your passport expire can cost more than you think
- Passports, travel and living abroad

## How is it scored?

By viewing the explain plan we can understand how the different scores are combined:

```
GET detailed,mainstream,government/_search
{
  "explain": true,
   "query": {
      "multi_match": {
         "query": "renew my passport",
         "fields": [
            "title",
            "description"
         ],
         "analyzer": "query_with_old_synonyms"
      }
   }
}
```

At the outermost level there is a `max of` two things.

```json
{
  "_explanation": {
    "value": 2.1252842,
    "description": "max of:",
    "details": [{}, {}]
  }
}
```

This is the default behaviour of `multi_match` when you don't specify a `type`. It's equivalent to specifying the type as [best_match](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/_single_query_string.html#know-your-data).

> When searching for words that represent a concept, such as “brown fox,” the words mean more together than they do individually. Fields like the title and body, while related, can be considered to be in competition with each other. Documents should have as many words as possible in the same field, and the score should come from the best-matching field.

There are [other ways to combine field scores](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-multi-match-query.html#multi-match-types).

If you expand the explain plan for one of the fields, you should see `coord(2/3)`. This is the [coordinating factor](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/practical-scoring-function.html#coord). It boosts documents based on what fraction of the search terms match.


```json
     {
        "value": 2.1252842,
        "description": "product of:",
        "details": [
           {
              "value": 3.187926,
              "description": "sum of:",
              "details": [
                 {},
                 {}
              ]
           },
           {
              "value": 0.6666667,
              "description": "coord(2/3)"
           }
        ]
     },
},
```

This is applied to the sum of the scores from the individual terms, which are scored the same way as the single field example.

You can include a `tie_breaker` to use the non-best fields as a tie breaker
when documents score the same on their best fields:

```
GET detailed,mainstream,government/_search
{
  "explain": true,
   "query": {
      "multi_match": {
         "query": "renew my passport",
         "fields": [
            "title",
            "description"
         ],
         "analyzer": "query_with_old_synonyms",
         "tie_breaker": 0.3
      }
   }
}
```

In this case to get the score elasticsearch adds up all the scores for each
field, but first multiplies all except the best by 0.3.

## Boosting

Multi match has a concise syntax for boosting individual fields. For example,
to value `title` more, you can do:

```
GET detailed,mainstream,government/_search
{
   "query": {
      "multi_match": {
         "query": "renew my passport",
         "fields": [
            "title^10",
            "description"
         ],
         "analyzer": "query_with_old_synonyms",
         "tie_breaker": 0.3
      }
   }
}
```

This still gives 13916 results, but the top results are now the same as
for the single field query:
- Consul in Italy warns Brits not to let their passport expire
- Renew or replace your adult passport
- Letting your passport expire can cost more than you think

Note: The `^10` doesn't mean title will be 10x as important as description, just
that the title field's score will be boosted by 10.

Each field has its own statistics for term frequency, document frequency, and
field norms, so field scores are not directly comparable.

## Concatenated fields

There are some fields that contain text from multiple sources.

`_all` is a built in field, that contains various other fields concatenated together. Fields can be configured to not be included in `_all`.

`all_searchable_text`, `all_searchable_text.synonym`, and `all_searchable_text.id_codes` are similar but with custom analyzers.  

`indexable_content` is controlled by the publishing app. It normally contains the body text with some additional text concatenated on the end (such as section summaries for multi part documents).

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {
        "indexable_content": {
          "query": "renew my passport",
          "analyzer": "query_with_old_synonyms"
        }
      }
   }
}
```

This gives us 102481 results, starting with:
- New passport design hits the streets
- Beat the New Year rush for passports
- Apply for or renew a British passport if you're visiting the UK
