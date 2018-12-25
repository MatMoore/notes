# Combining queries

You can combine queries using the [bool query](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-bool-query.html):

For example:

```
GET detailed,mainstream,government/_search
{
   "explain": true,
   "query": {
      "bool": {
         "must": {
            "multi_match": {
               "query": "register for postal voting",
               "fields": [
                  "title^10",
                  "indexable_content"
               ],
               "analyzer": "query_with_old_synonyms",
               "tie_breaker": 0.3
            }
         },
         "should": [
            {
               "match_phrase": {
                  "searchable_text": {
                     "query": "register for postal voting"
                  }
               }
            },
            {
               "match": {
                  "title.shingles": {
                     "type": "boolean",
                     "query": "register for postal voting",
                     "operator": "or"
                  }
               }
            }
         ]
      }
   }
}
```

- `must` queries have to match the document for it to be returned
- `must_not` has to not match the document
- `should` may or may not match, but if it matches it will contribute to the score

You can also add [boost attributes](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/_boosting_query_clauses.html) to subqueries to weight them differently in the overall score.

## Query vs filter context
In the examples so far, we used query clauses to affect the score.

In the case of `bool`, the `must` and `must_not` subqueries either select or reject
documents, but the subquery influences the score of whatever's left.

An alternative is to use `filters`, which just select/reject without affecting
the score.

In Elasticsearch 1.x, filters are a [separate part of the DSL](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-filters.html)

From Elasticsearch 2.0 this was simplified. Now, the only difference between a filter and a query is the [context](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html) it appears in. `bool` queries just accept a `filter` clause, similar to `should`, `must`, and `must_not`.

## Incorporating other signals

Besides text matching, there are lots of other ways you can use information about documents to influence a search query. For example:

- [Term queries](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-term-query.html) allow for exact matching. We use this for "identifiers" like organisations. At indexing time we configure these fields to be "not analyzed" so that we can compare the exact text.

- [Range queries](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-range-query.html) allow you to search over a range of dates or numbers.

- [Function score](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/function-score-query.html) lets you calculate a score based on a function, which can be an arbitrary script - we're using this for date and popularity weighting.

Here's an example incorporating [popularity boosting](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/boosting-by-popularity.html):

```
GET detailed,mainstream,government/_search
{
  "query": {
    "function_score": {
      "query": {
        "multi_match": {
           "query": "register for postal voting",
           "fields": [
              "title^10",
              "indexable_content"
           ],
           "analyzer": "query_with_old_synonyms",
           "tie_breaker": 0.3
        }
      },
      "field_value_factor": {
        "field":    "popularity",
        "modifier": "log1p",
      }
    }
  }
}
```
