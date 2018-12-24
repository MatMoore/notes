Taxonomy Bootcamp 2016
======================

Designing Future Friendly Content
---------------------------------

### IA as design
- IA is "the design behind the design"
- BBC was a bottom up effort
- we design "places made of information"
- May have different designs for different devices/interfaces, but they are all "windows on the same vista"
- IAs are like "backend designers"

What many people do is "Emptying out the virtual filing cabinet of PDFs onto the internet" (sounds familiar).

*CRAP design principles:*
- Contrast - to show differences
- Repetition - consistency communicates patterns
- Alignment - can show a consistent linear progression (vs unrelated things)
- Proximity - thematically related stuff should be close together

We can order the layers of a publishing platform by their tendency to change (from less to more often):
- Subject domain
- **Content structure**
- "evergreen" content
- other content
- curation
- interface design

### Definitions
- An ontology is "the things that we mean when we say what we say"
- A taxonomy is "the arrangement of those things"
- Content leadership means you educate and explain, and relate to business value.


### Building a CMS
When talking to subject matter experts (SMEs):
- Pick out important words
- Ask questions about how they relate

This helps you build an entity relationship model of the domain.

The result is a ubiquitous language the team can agree on. This should be used everywhere to avoid miscommunication!
- database tables
- css classes
- etc...

The domain model will inform the content types you need for your CMS.

Structuring your data around a rich domain model lets machines save us time. The example compared a simple CMS to one written for conference websites, which made predictable data changes (like changing a speaker's name) easier. You can change the name of a person, but you can't change the name of body text.

Governance:
- Structured design requires more work up front but needs buy in from your stakeholders

- Standards, policies, and principles are just as important as the content structures themselves

- When working within a team you need to agree strategy but argue tactics

### Other routes to content
- On the web, content is shared, and curated everywhere, not just your site
- Think of google, facebook as shortcuts to the content

Q. Cancer as an example of "structuring too deep": grouping many different diseases together as "cancer" has been problematic for cancer research.

Aside
------
February 18th is World IA Day

A common subject classification for content publication on nature.com
---

Background:
- Most content had no subject assigned
- Some journals had their own classification schemes
- Wanted to classify using a single vocabulary for all content

The taxonomy:
- Structured using SKOS
- Up to 8 levels deep
- Journal editors wrote the descriptions for each topic
- Authors or editors tagged the content
- Used clear naming for terms, plus synonyms to help discoverability
- Multiple distinct synonymous terms forbidden
- Multiple inheritance doesn't infer specificity on a term
- Terms are linked to external models, this helps with taxonomy development
- Questions to answer: what subject areas do you cover and how granular should the taxonomy be?

Tagging guidance:
- Describe the article using taxonomy terms. You should use 2-5 terms (preferably the upper end of that).
- Internal users are trained on what the terms are and how they relate to each other.

Subject pages:
- RSS & atom feeds
- SEO
- If you search for a synonym or a subject term, you get a subject box displayed in an aside.

Taxonomy management:
- A taxonomy manager collaborates with subject matter experts
- Taxonomy changes go through a steering group
- Poolparty is the management tool
- Integrates with production system
- Terms can be deprecated: they go in a separate branch of the taxonomy and are mapped to an alternate term
- Partially automated tagging: manual intervention to move in/out of a subject. Uses google dimensions.

Linked data:
- NPG Linked data platform
- Nature Ontology platform
- Scigraph (coming soon)

Helen from DFE
---
Background:
- DFE have had a subject thesaurus since mid 1980s
- Project: use a subset of the terms to build a taxonomy
- Goal: consistent information about work over separate IT systems (CRM and sharepoint)
- Problem: difficult to find where in the department a query should be answered

Taxonomy:
- 3 levels due to technical constraints
- Some subjects are far too broad to tag to
- Some people have strange ideas that you have to say no to (school governers guidance is not a type of school governers)
- Uses multites tool
- Can generate reports of terms with broader terms and optionally all narrower terms
- Can generate deltas of terms following machinery of government changes
- On a staff profile, it's mandatory to tag to responsibilities
- The logger of a CRM query assigns subjects
- Query routed to a team with that expertise

Misallocations can happen when:
- logger misread the query
- not enough details
- wrong team is set for the term

One team per term is not perfect. Workarounds like "Data analysis (adoption)" and "Data analysis (fostering)"

Would like to add related terms eg nutrition -> school meals.

General advice: don't agree to terms in meetings - they might not fit.

GOV.UK integration:
- When anonymous feedback comes in from GOV.UK, they tag it to a subject, so it can be dealt with effectively.
- Can map trends in subjects and plan for seasonal queries.
- Note that DFE vocabulary is for departmental use, some terms are not meaningful to users eg "Graduate premium"



Day 2
======

Patrick Lambe - Knowledge mapping or content modelling
--------

Conference red flags:
- experts
- real world
- SME

Expert "can disagree with fine detail with another expert in the field"
Keep them away unless they're a user. Engage at the end of the project. For fact, accuracy, completeness. "Can I combine this", "is this another word for this".

Key ideas:

- **PURPOSE**
- **CONSTRAINTS**
- **PRINCIPLES**
- **SCOPE**

Purpose needs to be actionable from design pov. "We need to be more collaborative" not good enough.

A *knowledge audit* maps knowledge assets for activities, and pain points. Highlights access problems. "I have to talk to X to view Y because I don't have permission", "I can't find the thing so I need to talk to someone who remembers it". Highlights high demand and high risk (can walk out the door) knowledge assets.

Constraints and affordances shape methods and tools

(Q. Should we be using taxonomy principles "is a kind of/broader term/narrower term" to frame taxonomy user research)

Warrant = the evidence behind design
- Content
- Users
- Standards-warrant (exchanging with other bodies, or long-term consistency)

Scenario based testing: from activities in knowledge audit.

*Content model* approach focuses more on the content:
Use cases ->
Content model (entity relationship) -> Entity model with facets (values from word buckets of use cases)

Ontology driven...
------

Navigational aids help you when you don't know how to explain what you're looking for (people call things different things)


DEEP TEXT book

Who will use your taxonomy and how:
- Taxonomy curators
- Content curators
- Human and machine aided indexers
- Search and discovery

Catonomy "captures some of the stuff from machine categorisation"

Consider prototaxonomies (eg from KM audits)

"Existence of the taxonomy itself is a form of governance" (it imposes order on content)

Using an external ontology...
such as dbpedia

Predicate = relationship OR property.

Building a SKOS vocab (thesaurus or taxonomy)

Pick predicates from the ontologies.

Taxonomies for Structured Content
-------------
Multiplying...

Content often less granular

Example: recipes from Kenwood

Integrating the taxonomy management system into publisher
Recognises taxonomy terms, shows bt and nt
Connect the term to taxonomy term
User clicks a thing to get contextual information

Make tagging nice experience
Like facebook talking about your friends

Uses schema.org markup

Shaping information blog

Journey from excel spreadsheet
------------------------------
Semantic publishing system

Fred Alexander IA

Automated tags - difficult to spot what it doesn't pick up.

Aggregation encouraged more people to read the details.

Fast track taxonomy
-------------------
Taxonomy warehouse is being updated

Build vs buy depends on how unique your domain is.

Linked data:

Trusted authorities and DBPedia

Old world: database identifiers are not portable

Hyperlinks are signposts

New world: HTTP URI

Library of Congress Geonames

Links have semantic meaning
The semantic meaning can be looked up in an ontology

Linked data can be open or internal

Use cases:

Describing artworks. Getty AAT controlled vocab.

Uses "depicts" to index a painting to "Lute"
Links symbolic meaning to getty and iconclass concepts

Love at first sight "there's a concept for that"

(? If we marked up people better and refer to concepts, news/press releases can be aggregated)

"Using other people's vocabulary is a gateway"

Builds chains for exploring other peoples information.

Can connect artwork that has same concepts.

Mapping to Linked Open Data for semantic enrichment:
- Built internal vocabulary of public figures
- Click button to crawl SPARQL endpoints
- Make an assertion that our Obama is DBPedia's Obama
- Can access additional data such as DOB
- System stores the provenance (using the URIs) and can refresh it at any time

"The world is your database"

Taxonomies and the systems they reside
-----------------------
Tech agnostic = ignore capabilities, design taxonomy, then change tech

"like building your dream house"

Catonomy = define the rules autocategorisation uses at each level of the taxonomy

Balance between technology agnostic and system focus

Lessons Learned Implementing an enterprise taxonomy
-----
IFC
international finance...

Asking users to review applicability  vocabulary.worldbank.org terms
low response rate

Taxonomy workshop
No accountability, wrong people in the room

one on one meetings better.

Compared with current taxonomy to see outdated, or too broad terms.

Launched a new LMS with the taxonomy -> impact more visible

Tales from the trenches Multidisciplinary team
---
Try to work with people who produce/own the content

Big meetings high level strategy

"Swarms" D:

Need information to get started.

Ask around about other people in organisation doing similar stuff

At the bbc editors don't like losing control to automation

Some products don't want to be associated with smaller products

**Don't ask meteorologists about the weather**

Audit before the audit

Introduction to the taxonomy for new starters helpful

Sometimes scope of taxonomy different from project. Versioning things. Governance should be set up early.

The PLOS thesaurus and machine aided indexing
---
PLOS is an open access publisher

PLOS one accepts regardless of novelty. Encourages negative results and replication, interdisciplinary research.

Article level metrics: shares, views, citations, saves.

Thought: (how do we store synonyms in the publishing platform? equivalent terms, related terms, acronyms?)

Data harmony tool

Machine aided indexing
Base layer NLP reads text, sentences, proximity of words.
17,000 rules apply terms to a chunk of text


TTM: climate change
USE: climate change

TTM: climat*
USE: what exactly?

DSL:
NEAR/WITH/AROUND/MENTIONS IF/ELSE/AND/OR/NOT

Many rules are loooong pseudocode

Some concepts are not phrases in the search itself. Some acronyms clash with concepts.

User can click on a tag and is prompted. If they say its not correct it goes into a report ranked by number of users flagging it. Feeds into thesaurus work.

Quarterly cycles. Re-MAI and re-Solr.

Subject landing page
Multisubject TOC emails

People are also indexed. Used to select reviewers. (Can also nominate someone)

Pretty tree maps for trend analysis. Thesuarus is posted on github.

Basel Register of Thesauri, Ontologies & Classifications (BARTOC)
---
"Start your taxonomy adventure!"

bartoc.org

Founded for the same reasons as all the other 70 registries but better.
