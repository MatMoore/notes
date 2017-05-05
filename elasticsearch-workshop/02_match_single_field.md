# Matching a single field

Let's run a simple query using [match](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/query-dsl-match-query.html).

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match": {"title": "vote"}
   }
}
```

I got these top 3 results:

```json
{
   "_index": "mainstream-2017-03-14t14:17:02z-00000000-0000-0000-0000-000000000000",
   "_type": "edition",
   "_id": "/browse/citizenship/voting",
   "_score": 9.16803,
},
{
   "_index": "mainstream-2017-03-14t14:17:02z-00000000-0000-0000-0000-000000000000",
   "_type": "edition",
   "_id": "/register-to-vote",
   "_score": 5.7300186,
},
{
   "_index": "mainstream-2017-03-14t14:17:02z-00000000-0000-0000-0000-000000000000",
   "_type": "edition",
   "_id": "/voting-in-the-uk",
   "_score": 5.7300186,
},
```

With these titles:

- Voting
- Register to vote
- An overview of voting in the UK, including when to register to vote, voting in person, postal and proxy voting

On the other hand, result #10 is "Ministry of Defence Votes A 2015 to 2016: supplementary votes"

```json
{
  "_index": "government-2017-03-14t13:42:36z-00000000-0000-0000-0000-000000000000",
  "_type": "edition",
  "_id": "/government/publications/ministry-of-defence-votes-a-2015-to-2016-supplementary-votes",
  "_score": 4.1644645,
}
```

## Understanding the scores

We can add explain output to see why these documents were scored this way.

```
GET detailed,mainstream,government/_search
{
   "explain": true,
   "query": {
      "match": {"title": "vote"}
   }
}
```

You should see something like `weight(title:vote in 174) [PerFieldSimilarity], result of:` with some nested components for:
- Term Frequency
- Inverse Document Frequency
- Field Norm

See [theory behind relevance scoring](https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html) for more info.

Let's compare the top two.

| Measure                          | Voting browse page | Register to vote |
| -------------------------------- | ------------------ | ---------------- |
| Term Frequency (TF)              | 1                  | 1                |
| Inverse Document Frequency (IDF) | 9.16803            | 9.16803          |
| FieldNorm                        |  1                 | 0.625            |

In this case:
- the term frequency was 1 in both cases (both titles are considered to have one occurrence of "vote")
- the document frequency looks at how often "vote" appears in all content, so this is the same for both results
- FieldNorm is the only difference. Elasticsearch prefers "Voting" because it's shorter than "Register to Vote".
