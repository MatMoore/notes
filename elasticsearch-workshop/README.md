# Elasticsearch workshop

## Setup

These instructions assume you have a GOV.UK development VM running Elasticsearch
1.7.

### Install the unofficial Sense browser plugin

The [sense plugin](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig?hl=en) gives you a nice interactive environment for testing queries.

You should see a simple starting query:

```
GET _search
{
   "query": {
      "match_all": {}
   }
}
```

Set the server to `dev.gov.uk:9200` and press the play button to send the query.

Ignore any warnings about GET requests not being supported.

Alternatively you can use the head plugin UI at [http://dev.gov.uk:9200/_plugin/head]() (click on the "any request" tab).

## Exercises

- [Query the content indexes](01_query_content_indexes.md)
- [Match a single field](02_match_single_field.md)
- [Debug analysis](03_debug_analysis.md)
- Match multiple fields
- Combine clauses
- Match phrases
- Ignore common terms
- Incorporate non-text signals
