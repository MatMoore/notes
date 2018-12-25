# Querying the content indexes

`/_search` searches across all indexes and all document types.

On GOV.UK, we have these indexes:

- detailed
- government
- mainstream
- maslow
- metasearch
- page-traffic
- service-manual

`detailed`, `government` and `mainstream` are the ones containing GOV.UK content, so we'll restrict all our queries to those.

```
GET detailed,mainstream,government/_search
{
   "query": {
      "match_all": {}
   }
}
```

You should see a total of around 320,000 hits.
