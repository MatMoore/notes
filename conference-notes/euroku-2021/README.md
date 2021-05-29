# Euroku 2021

# Keynote - Matz

Matz talked about the changes in ruby 3.0 and whats next after that.

## Performance improvements

_Fibers_ are like the event loop in node.js, use them for IO bound work

_Ractors_ are an isolated object space, communicate via channels, don't share objects. Use them for CPU bound work.

`Ractor.new { computation }`

Ractors are 4x faster than single threaded code.

## Gradual typing

Want to get benefits of static typing without introducing syntax

`RBS` (ruby signatures) are like d.ts in typescript.

It's a new language to define types in a seperate file.

This will lead to type checkers and better IDEs. Ruby3.0 won't neccessarily have the tools but will make them possible to implement.

`TypeProf` does naive type checks and generates rbs for you!!

## Pattern matching

There was a nice example of using this for json parsing

## Numbered block parameters

This is nice syntactic sugar for blocks with one or two arguments

## Direction of travel

Today tools are more important than language. Better tools -> better UX.

- Solargraph benefits from RST etc
- Sorbet is a static type checker
- Rubucop

The focus for 3.1 is stability - not much language enhancements, but improve ractors.

Matz has lots of "silly ideas" for the future. He mentioned that he would like to fix packaging to be more like python/java. I.e. isolate constant/variable namespaces and explicitly import the names you want.

# Accessibilty - Eeva

- [eevis.codes](https://eevis.codes/)
- [@eevispanula on twitter](https://twitter.com/eevispanula?lang=en)

This was about manually testing accessibility. At the start Eeva mentioned that automated tools can only catch between 15 to 40 or 50% of failures.
(This seems to match findings from https://alphagov.github.io/accessibility-tool-audit/)

So, half of problems cannot be found this way.

Some manual checks:

1. Keyboard navigation
2. Color
3. Check the ability to zoom (on mobile)

In chrome there is an "emulate vision deficiencies" tool under "more tools".

There was a discussion in chat about how to get a budget for a11y teams.

> "every time an issue comes up that can be solved following an accessibility guideline (WCAG), mention it."

# PDF lightning talk

Prawn is the go to library in ruby. It's actively developed and has lots of extension gems.

Hexapdf is intended to be full fledged implementation of the spec.

- Fast and memory efficient
- High and low level interface

# How to stop breaking other people's things - Lisa Karlin Curtis

It's easy to break other peoples stuff.

"Things break because an assumption made by the integrator is no longer correct"

It's not productive to blame engineers, since

1. As a developer **you need to make assumptions**
2. If your integrators feel pain, you'll feel it too

## Some examples

### Example 1

- Integrator called slow endpoint in response to webhook events
- API acting as a rate limit
- Speeding up endpoint caused increased demand on integrator db -> outage

### Example 2

- An integrator relied on a service ignoring its accept-language header
- It broke when they started respecting the header

### Example 3

- When a status change was made, a log event was created in the same transaction
- Breaking apart the transaction meant integrator has to handle case where event doesn't exist yet
- They assumed that could never happen!

### Example 4

- Changing the timing of batch processing
- This means payments might be delayed

### MSDOS

- MSDOS has a bunch of undocumented APIs
- But people shared lists of them
- Then MS couldn't change anything.

## Explicit assumptions

These come from information you've provided to the integrator

- Documentation
- Support articles and blog posts
- Ad hoc communication (support tickets, friends who work at company etc)

## Implicit assumptions

These come from the integrator coming to their own conclusions

- Industry standards (e.g. meaning of headers, expectations around secrecy)
- Observed behaviour

Developers make lots of thinking errors:

- assume everyone else's code will behave consistently and stay the same forever
- aggressive pattern matching (correlation == causation)
- if it hasn't broken for a long time, we think it never will

## How to avoid bad assumptions

- Document edge cases
- Keep your own support articles and blog posts up to date, make sure it's easy to find
- Contact authors of out of date 3rd party content, point to official docs
- If you're repeatedly sharing the same information through ad-hoc comms, centralise it, and set expectations that it will change

### Naming things

Beware misleading names (for example, `account_number_ending` can contain letters)

Call out things you might want to change, and expose info that could change in your API so integrators don't have to hardcode it.

## Breaking/non breaking is a misleading binary

Beware saying "oh this isn't a breaking change". Almost anything can be breaking.

Use people in the organisation that are less familiar as rubber ducks
Talk to integrators
Dogfood your apis

## What about semver?

Use it for apis and webhooks where possible. Not everything can be applied on an opt in basis (e.g. timing)
Supporting multiple versions increases complexity, so it's a trade off

## Don't overcommunicate - no one will read it

- Pull comms (updating docs or changelog) <- least breaking changes
- Push comms (e.g. newsletter or email)
- Acked comms (wait for positive response from particular integrators) <- most breaking changes

## Mitigations for potentially breaking changes

- Can you make the change incremental? Give early warnings. E.g. apply to a percentage of requests/integrators.
- Release to a test/sandbox environment first
- Can you roll back?

## "Move fast and break things"

Both of these things affect trust.

Blogs are good as point in time communication out, bringing integrators on side. This is in contrast to "forever documentation" that you keep up to date.

## Developers don't read documentation

- If you start your docs with examples, the first thing you see is the name
- Often the only thing people read and internalise
- If you get it wrong, you have to do a lot of sign posting to correct it later

Documentation should focus on important things - ask what the impact is if you don't document it.

E.g. if the worst case scenario is creating a double payment, the documentation should help integrators avoid that.

You should communicate industry practices that you are following (e.g. we will add attributes to the responses so you should be able to deal with this)

You can generate client libraries (e.g. openapi) so that integrators don't have to write their own.

## "Act with integrity"

You want to avoid a culture of avoiding changes altogether, and also the opposite extreme where you are constantly breaking people's code.

Build tooling to make it easy to communicate. Have style guides, and processes to reduce friction.

Your deprecation policy should trades off the cost to the integrators to change their code vs the risk of you having several versions to maintain at once.

You should have a hard line; set an arbitrary day for deprecating stuff. "Unless the world is on fire this will go away"
You need to establish a culture where, specific teams do not have the power to stop things progressing just because they're busy.

# GraphQL performance - Dmitry

Recommendation: Production Ready GraphQL book. Some of the techniques from the book were covered in this talk.

## Query path

GrpahQLController -> Schema Executor -> Parse -> Validate the AST -> execute_field recursively -> execute_field_lazy -> to_json

## Find the bottlneck

Set up a tracer. (e.g. `GraphQL::Tracing::NewRelicTracing`)

With a custom tracer you can instrument each stage of query path

`yabeda` is a gem.

Use client headers (client name and version) to identify clients.

Directive profiling: you can write something that profiles when you use a directive in the query.

## Common issues

- Response building is slow, so use pagination for large collections
- Avoid N+1 issues in resolver. You can use lookahead to see whether you need to load additional associations (e.g. with includes)
- You can also use lazy_preload technique `ar_lazy_preload` gem

## Advanced techniques

### HTTP caching

- Cache-Control/Expires
- Last-Modified/If-modified-Since
- ETag

POST requests can't be cached, so you need to allow GET requests, but there are limitations on what you can fit in a query string.

Apollo persisted queries identify a query by hash.

> Technically, GrapQL also supports GET requests without that. You can do something like http://myapi/graphql?query={me{name}}. But I find this just really weird.

See https://graphql-ruby.org/guides#graphql-pro-operationstore-guides

With persisted queries you can cache the AST instead of the query ("compiled queries").

### Response caching

Queries can share some fragments, so you can cache parts of responses identified by a "fragment id". `graphql-cache` gem does this.

## Advantages of GraphQL vs REST

- up to date documentation out of the box - you have to define the schema
- frontend developers can write any query they want

# Adding byebug to the Professional Puts Debugger Tool Set by Zhi Ren Guoy

You can run `byebug demo.rb` without modifying the code

```
in ../demo.rb
break [line number]
break 3 if referral[user_id] # conditional breakpoint
var local # local variables
display referred # show variable each time debugger stops
set linetrace on # show variables after each line
step # can step into gem
where
```

In byebug you can also mutate variables on the fly.

`byebug` command is included by default in rails now.

## Other tips from chat

Messing with gems using puts debugging:

```
gem open foo
gem pristine foo
```

> My life changed when I learned about the hist command in pry. No more copy pasting lines when I want to re-execute them pry(main)> hist 1: puts "Euruko 2021" 2: puts "hello" 3: puts "world" pry(main)> hist --replay 2..3 hello world

> Sharing here too - one debugger that I like a lot is https://rubyjard.org/

> There's also UUIDv6 proposal, which is not widely adopted, but kinda addresses the sorting issues of UUIDv4 and somehow addresses problems of UUIDv1, but I don't remember which ones

Since rails 6, you can enable "stict loading" to warn about N+1 queries: https://github.com/rails/rails/pull/39491

# Going native with FFI - Juan Carlos Ruiz

This talk covered two options for writing native code extensions.

## MKMF

Example: https://github.com/JuanCrg90/my_ruby_ext

This tool generates a Makefile to compile and link a c extension.

We need to add extra C code to create the bindings.

## Foreign function interface (FFI)

Example:https://github.com/JuanCrg90/pgm_ffi

```
ffi_lib 'c'
attach_function :puts, [:string], :int
```

FFI extension is multi platform and multi-implementation.

> if you're using ffi in your gem should you bundle the sourve library in them gem?
> that maybe hard on what \*nix-ld system it should be used to prebundle compiled so's

# Optimizing Ruby's memory layout (Matt and Peter)

This talk covered a new approach for memory management/garbage collection in ruby.

This was quite in depth and I think I will need to watch it again to understand the whole thing. People in the chat recommended the "Ruby under a microscope" book for learning ruby internals, and compared it to what Project Valhalla targets to do in for java. [The Garbage Collection Handbook](https://gchandbook.org/) also covers the techniques ruby uses.

## How it works now

Memory in ruby is structures into _Heap pages_, which are 16kb memory regions.

There are 408-409 slots per page where you can stick data. Slots are contiguous.

Initially, all slots are set to a special value, _T_NONE_.

These pages are an internal concept to ruby, and should not be confused with system concepts like virtual memory.

There is a `Freelist` pointer which points to the next available slot in the page, and each slot has a next pointer pointing to the next slot.

### Garbage collection

Garbage collection in ruby follows a "Stop the world" approach with 3 steps.

#### Marking

- Mark the roots (globals, modules, constants)
- Marked objects get put on a "mark stack"
- Recursively mark children by popping from the mark stack and pushing the children

#### Sweeping

- Move the freelist pointer across the pages looking for unmarked objects

#### Compaction (optional)

This process has two steps.

##### Compact step

This uses a "Two-finger cursor" structure:

- The _Compact cursor_ starts at end and moves backwards until the last full slot
- The _Free cursor_ starts at the beginning and moves forwards until the first free slot
- Move the object to the free slot
- Keep going until the cursors meet

##### Reference updates

- Second step updates the references to the moved objects

## The problem: Large objects

In the CPU, level 1,2,3 caches are used when you fetch data from memory. This happens in units of cache lines (64B).

For large objects, Ruby sets the _NOEMBED_ bit. Then it mallocs seperate heap state and stores a pointer to it.

This is bad for _cache locality_ because you are fetching stuff from different places so you need to read more cache lines(?)

Also, malloc has performance overheads so you want to minimise calls to it. It also stores additional metadata.

## New approach

- Variable width allocation (not all heap pages will have the same slot size)
- RVALUE and its data will be closer together
- Simpler sweeping stage
- Current implementation does not support compaction, so suffers from memory fragmentation (there is enough memory in total, but there is no contiguous region big enough)

# Lockdown: the mother of invention - Amy

Ruby is great because you can realise ideas quickly

"I'm going to make this the most productive time"

## Simple to do list app

- Generate a schedule for a day

## On air alert system for boyfriend

- Purchased a smart light with a REST API
- Created a proof of concept
- Plan to extend to different meeting platforms

## Solargraph rails

- Looking for contributors

## Remote working tips

82% company leaders plan for remote to continue after the pandemic

Use group chat instead of 1:1 where possible

Virtual meeting that is open all the time for water cooler chat

# The 6 Characters that could bring down your app - Moncef Belyamani

The lightning talk is based on [this blog post](https://www.moncefbelyamani.com/the-6-characters-that-could-bring-down-your-rails-app/).

Look out for `.count.positive?` pr `.count > 0`

Moncef worked on benefits for veterans. The organisation modernised legacy systems from the 80s for tracking claims.

This issue caused a suddent problem they noticed through recurring sentry errors.

`.count` in rails generates `select count(*)` in postgres. This can be slow.

Code wasn't even using the count, just checking non-zero. So it could be replaced with `.any?`.

There are various methods in activerecord like `#any?`, `#exists?`, which can be confusing. There's an article comparing these.

> Sounds like there should be a Rubocop rule to catch .count (much like binding.pry)

# IDE development with ruby - Soutaro Matsumoto

Soutaro is a ruby core committer working on RBS. He developed the Steep type checker.

You can install a VSCode extension to get diagnostics reporting, completion, navigations, hover.

## What is an IDE?

### Examples

- Visual basic in 1995
- VS Code
- Eclipse
- Jetbrains
- Android Studio
- Even Vim/Emacs could also be considered IDEs.

### Features

- Syntax highlighting
- Folding
- Diagnostic reporting
- Navigations - jump to definition
- Completion
- Refactoring - e.g. extract method, help define new methods

This stuff depends on program analyses, including type checking.

### Program analyses levels

#### Text analyses

input = sequence of characters

#### Syntactic analyses

input = syntax tree of ruby program

#### Semantic analyses

analyze based on everything

The analyzers provide the same set of features regardless of IDE. The language server protocol (LSP) extracts the language specific analyses so it can be reused by IDE frontends.

IDEs communicate with the language server over a protocol that enables inter process communication. There are no assumptions about the server language so we can implement it in ruby.

### Language servers for ruby

- Steep
- Solargraph
- Sorbet
- vscode-ruby has its own language server implemented in typescript

### Designing the language server for Steep

Example of the notifications sent over the LSP:

```
-> DidChangeTextDocument
<- PublishDiagnostics
```

### Responsiveness

Running the type checking on every key hit blocks users interaction. Some tricks to make more responsive:

#### Incremental type checking

- When you change a ruby file it type checks only the file (500ms~1s)
- When you change RBS files, it runs full type checking (could take minutes)

#### Prioritising open files

Open files have priority in the type checking queue, for faster feedback.

#### Dropping code

Completion needs more responsiveness (< 300ms)), so in this case unrelated methods are dropped.

# Streaming data transformations with ruby

Implemented piperator gem.

Each step in pipeline is a lambda function that returns an enumerable

THe most useful thing in this gem is a `Piperator::IO` class, which is like StringIO -> converts an enumerator to IO.

Since ruby 2.7 you can use the function composition operator `>>` to accomplish the same thing.

# Delivering fast and slow - Ethics of quality - Lena Wiberg

The core message of this talk is to take responsibility for your actions and call out other people's bad decisions. Don't blame others.

Big disasters happen because of many small risk assessments and decisions.

## Boeing 737 Max 8s

- Software to compensate for moving the engines etc
- Rushed
- Skipped pilot training
- 300+ people dead

## Airbus

"turn the airplane off and again"

## Mars climate orbiter

- Mixed metric and imperial measurements
- $550M dollars lost in space

## Orebro University hospital

- Swedish hospital
- Software couldn't handle swedish characters

## How to behave ethically

### Understand your basic professional obligation (depending on role you are hired to do)

- Tester - discover information and pass it on
- Developer - develop safe, fast, well architected software

### Know your legal and contractual obligations. What are you expected to follow? (E.g. GDPR)

You need to know when you are implementing something that is not legal.

### Know your own ethical bottom line

What lies are you not willing to tell? Will you hide a potential bug if its not probably or you think noone would ever use that? What's the worst thing that could happen to you or someone else?

Whose interest are you serving?

If you are building a voting system, you are serving the voters and government, not the company that makes money.

### Know the harm your software could do, maintain critical awareness of your whole work situation

Today we use lots of components and algorithms we don't understand. We collect a huge amount of data.

What is the company prepared to do? E.g. volkswagen were prepared to hide CO2 emissions.

Need to be aware of biases, e.g. data bias

You can have "evil personas" and think about use cases related to those.

See also: [Assume worst intent (designing against the abusive ex)](https://alexwlchan.net/2018/09/assume-worst-intent/)

### Need to be good at saying no and speaking truth to power

Know your escalation path (e.g. managers manager, board room, newspaper)

Know your own tolerance for personal and career risk. If you are not willing to lose your job to make sure an airplane doesn't crash, you shouldn't be building airplanes.

> @Ramon: One way to say "no" is to say "yes, and", and I think that is a skill everyone should learn. You accept what is being asked of you and tell them what that means with respect to other constraints, and ask questions. For example, "yes, i can start working on this other project, and that means the current project will not be shipped and 6 months of work will be wasted. do you really want me to work on the new one? is it that urgent? can it not wait a month?"

## Being pushed to deliver more, faster, cheaper

- System 1 - fast unconcious thinking
- System 2 - slow concious thinking

System 1 likes assumptions, familiarity. It's not good for innovation.

## Cross functional teams

Cross function teams yes - cross functional individuals no

Like using a swiss army knife to build a house

> One thing we try to do is try to give newer developer ownership of one part of our software base as fast as possible so that they can pretty quickly feel legitimate in discussion of all level on their part of the product, and then we expand on that

# Shipping ruby and rails app as native Linux packages - Cyril Rohr

System packages are easy to distribute/install and can auto-upgrade without much fuss.

They may be the only option for large enterprises.

Published `pkgr` tool. Uses heroku buildpack and then outputs a deb or rpm package.

Automatically includes a configuration tool for setting environment variables, scaling processes you have declared in a procfile.

# Building a ruby web app using the ruby standard library - Maple Ong

- https://twitter.com/OngMaple

See also: [Peeling away the layers](https://peelingawaythelayers.net/)

## Networking

### `TCPServer` example

- Accept connections
- Echo messages
- Test with `nc localhost 9999`

### HTTP message anatomy

- Start line (request line or status line)
- Header fields
- Blank line
- Message body

### Accepting HTTP request example

- Parse request line
- Format HTTP response

### Handling form data

- Status code 303 See Other
- Parse headers into a hash
- Use Content-Length to know when the body ends
- Use `#decode_wwww_form` to decode form encoding

### Persisting the data

- `YAML::Store`

### What's next

- Make it a rack application
- Once its a rack application, you can hand off the HTTP logic to webservers
- Use a database

# Why a diverse team is crucial to startup success - Melissa Jurkoic

Diversity can be across many attributes - you need to define it in your context.

Start by diversifying leadership. They are the first faces people see. Influences the stategy and the market you're trying to attrack. Big problem of not providing pathways for leadership.

Language use is coded and can be encouraging or offputting. See http://gender-decoder.katmatfield.com/

We want to be able to see ourselves doing the job.

> Their results showed that women felt that job adverts with masculine-coded language were less appealing and that they belonged less in those occupations. For men, feminine-coded adverts were only slightly less appealing and there was no effect on how much the men felt they belonged in those roles.

Bringing diverse groups together can create conflict. But out of conflict comes great innovation.

Link from chat: https://geekfeminism.wikia.org/wiki/Category:Incidents

# Keynote - Linda Liukas

What even is a computer?

They are increasingly opaque.

Everything is input -> process -> output

We need more metaphors!

## Coding can be like cookiing

- Input -> Ingredients
- Algorithm -> Recipe
- Evaluating code -> Processing/cooking steps

Not all things can be easilly formulated as input -> process -> output model e.g. teaching a child.

## Should the technology grow or the person using it?

People writing code should

1. Write algorithms
2. Not too much
3. Mostly understandable ones

## Thinking about coding in different ways

Recipes and algorithms teach how, not why.

There's a disconnection between production and consumption of code has deepened.

Don't want everything to be plastic wrapped, processed code from big faceless tech companies

Want people to know the history - how did these people see the world?

Tech culture seems like a meme-ified smart snappy thing; it should be more like home cooking. Connect to ourselves and nature.

Developers are very focused on learning specific skills, whereas teaching kids is more about teaching curiousity and fearlessness.

Nowadays we have quite dystopian visions of the future. In 1960s had a lot of excitement about technology. We should imagine utopias. We're not at the height of technology right now.

## Unconventional computing

- https://www.amazon.com/Thoughts-unconventional-computing-Andrew-Adamatzky/dp/1905986122/ref=sr_1_2?dchild=1&keywords=andrew+adamatzky&qid=1622296053&s=books&sr=1-2
- https://royalsocietypublishing.org/doi/10.1098/rsfs.2018.0029
- https://en.wikipedia.org/wiki/Plant_to_plant_communication_via_mycorrhizal_networks

# Other resources discussed in chat

## Conferences

- https://www.emeaonrails.com/ (June 9)

## Tools

- [Color blindness simulator](https://michelf.ca/projects/sim-daltonism/)
- [Packwerk](https://github.com/Shopify/packwerk)
- [Git aliae](https://github.com/ConradIrwin/git-aliae/)

## Frameworks

- [Hanami](https://guides.hanamirb.org/)
- https://rom-rb.org/
- https://github.com/djellemah/philtre

## Blog posts

- [Consider static typing](https://codon.com/consider-static-typing)
- [Static Typing for Ruby](https://shopify.engineering/static-typing-ruby)
- [The Modular Monolith: Rails Architecture](https://medium.com/@dan_manges/the-modular-monolith-rails-architecture-fb1023826fc4)
- [Taming large rails applications with private ActiveRecord models](https://kellysutton.com/2019/10/29/taming-large-rails-codebases-with-private-activerecord-models.html)
- [Under deconstruction: the state of shopify's monolith](https://shopify.engineering/shopify-monolith)
- [Make rubocop 20x faster in 5 min](https://dev.to/doctolib/make-rubocop-20x-faster-in-5-min-4pjo) (for format on save)

## Books

- [Painless Rails without Overengineeriug](https://painlessrails.com/)
- [Growing rails applications in practice](https://pragprog.com/titles/d-kegrap/growing-rails-applications-in-practice/)
- [Sustainable web development with Ruby on Rails](https://sustainable-rails.com/)
- [Software people ... work from home](https://leanpub.com/softwarepeopleworkfromhome)
- [Gradual modularization for Ruby and Rails](https://leanpub.com/package-based-rails-applications)
- [Migrating to microservices](https://link.springer.com/chapter/10.1007/978-3-030-31646-4_3)

## Talks

- [Adopting Sorbet at Scale](https://www.youtube.com/watch?v=v9oYeSZGkUw)
- [Between monoliths and microservices](https://noti.st/palkan/VWPOSd/between-monoliths-and-microservices)
- [Counterintuitive Rails pt 1](https://www.youtube.com/watch?v=KtD32fO_owU)
- [the Taming monoliths without microservices](https://www.youtube.com/watch?v=-ovkkvvTiRM&list=PL9_jjLrTYxc3dTbvb8fIuzDFGTCaEdO3a&index=8)
