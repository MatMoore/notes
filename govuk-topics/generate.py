import time
from requests_cache import CachedSession
from collections import namedtuple as NamedTuple
from enum import Enum
from graphviz import Digraph

session = CachedSession(cache_name='govuk_cache')

Topic = NamedTuple('Topic', ('name', 'base_path', 'document_type'))
dot = Digraph(comment='GOV.UK Topic-ish Pages', format='png')
dot.body.extend(['rankdir=RL'])

SEARCH_URL = 'https://www.gov.uk/api/search.json'


class DocumentType(Enum):
    """
    Document type of a topic-ish page
    """
    mainstream_browse_page = 'mainstream_browse_page'
    topic = 'topic'
    document_collection = 'document_collection'


SHAPES = {
    DocumentType.mainstream_browse_page: 'box',
    DocumentType.topic: 'oval',
    DocumentType.document_collection: 'folder',
}


def content_store_url(base_path):
    """
    API URL for a content item
    """
    if not base_path.startswith('/'):
        base_path = '/' + base_path

    return 'https://www.gov.uk/api/content' + base_path


def pages_tagged_to_browse_page(topic, fmt):
    """
    Get pages with a particular format that are tagged to a browse page
    """
    response = session.get(
        SEARCH_URL,
        params={
            'filter_format': fmt,
            'filter_mainstream_browse_pages': topic.base_path,
            'fields': ['title', 'slug', 'format']
        }
    )
    print(response.text[:100])
    return parse_rummager_topics(response.json()['results'])


def pages_tagged_to_topic_page(topic, fmt):
    """
    Get pages with a particular format that are tagged to a topic page
    """
    response = session.get(SEARCH_URL, params={'format': fmt, 'filter_topics': topic.base_path})
    return parse_rummager_topics(response.json()['results'])


def parse_rummager_topics(results):
    """
    Parse topics from rummager results
    """
    pages = []

    for result in results:
        pages.append(
            Topic(
                name=result['title'],
                base_path=result['base_path'],
                document_type=DocumentType[result['format']]
            )
        )

    return pages


def topic_children(topic):
    """
    Get subtopics of a topic
    """
    response = session.get(content_store_url(topic.base_path))
    return parse_content_store_topics(response.json()['expanded_links']['children'])


def browse_page_children(topic):
    """
    Get second-level browse pages for a top level browse page
    """
    if topic.base_path == '/browse':
        key = 'top_level_browse_pages'
    else:
        key = 'second_level_browse_pages'

    response = session.get(content_store_url(topic.base_path))
    return parse_content_store_topics(response.json()['expanded_links'][key])


def parse_content_store_topics(children):
    pages = []
    for child in children:
        document_type_name = child['document_type']

        try:
            document_type = DocumentType[document_type_name]
        except KeyError:
            print('Ignoring document type {}'.format(document_type))
            continue

        topic = Topic(
            name=child['title'],
            base_path=child['base_path'],
            document_type=document_type
        )
        pages.append(topic)

    return pages

seen = set()
def node(topic, **kwargs):
    if topic in seen:
        return

    dot.node(
        topic.name,
        shape=SHAPES[topic.document_type],
        **kwargs
    )
    seen.add(topic)


def edge(tail, head, **kwargs):
    dot.edge(tail_name=tail.name, head_name=head.name, **kwargs)


def is_second_level(topic):
    """
    Check if a browse page is second level

    /browse/education         -> top level
    /browse/education/schools -> second level
    """
    return len(topic.base_path.strip('/').split('/')) > 2


def crawl(start, depth=1):
    node(start)

    if depth <= 0:
        return

    if start.document_type == DocumentType.mainstream_browse_page:
        if not is_second_level(start):
            for child in browse_page_children(start):
                edge(child, start, label='Belongs to')
                crawl(child, depth=depth-1)

        for tagged in pages_tagged_to_browse_page(start, DocumentType.topic):
            edge(child, start, label='Is about')
            crawl(tagged, depth=depth-1)

        for tagged in pages_tagged_to_browse_page(start, DocumentType.document_collection):
            edge(child, start, label='Is about')
            crawl(tagged, depth=depth-1)

    elif start.document_type == DocumentType.topic:
        for child in browse_page_children(start):
            edge(child, start, label='Belongs to')
            crawl(child, depth=depth-1)

        for tagged in pages_tagged_to_topic(start, DocumentType.document_collection):
            edge(child, start, label='Is about')
            crawl(tagged, depth=depth-1)

    else:
        return


start = Topic('GOV.UK Homepage', base_path='/browse', document_type=DocumentType.mainstream_browse_page)
crawl(start)

print(dot.source)
dot.render('output/govuk-topic-graph', view=True)

