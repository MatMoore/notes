# Domain Driven Design

## The domain vs the model
The *domain* is "the subject area to which a user applies the program"

Creating software requires a body of knowledge related to the users' activities

A *model* is "a rigorously organized and selective abstraction of that knowledge"

It is selected to serve a purpose (analogy to documentary making on p3)

It can be communicated in different ways:

- diagrams
- carefully written code
- writing

## Ubiquitous language

Includes

- classes and common operations
- rules that have been made explicit in the model
- high level organising principles imposed on the model
- patterns applied to the model

Excludes

- things from the jargon of the field, when using terms would be ambigious/contradictory (e.g. "course")
- subtle features created in the code that aren't thought of as part of the domain model

Use

- code
- diagrams
- speech

A change to the ubiquitous language is a change to the model. "Find easier ways to say what you need to say, and then take those new ideas back down the diagrams and code"

### Relation to design documents
- The ubiquitous language should lead to documents becoming more concise and less ambiguous
- If the ubiquitous language is evolving but not being reflected in the document, it's probably not important enough to update. Archive the document to avoid confusion
- If terms used in the document don't become part of the ubiquitous language, people are either not reading it or not finding it compelling

## Kinds of models
- One model should underlie design, implementation and team communication
  - scope is pared down to the minimum needed to fulfil functional requirements
  - UML object models
- Education aids can include models unrelated to software design
  - to provide more context / communicate general knowledge about the domain
  - multiple, diverse explanations
  - doesn't have to be UML (e.g. shipping timeline on p42)

## Model driven design
This means you don't have one model for analysis of the domain and design of the system. You have one model that works for both. (p49)

- It should reflect the domain ideas
- It shouldn't ignore software design principles

Terminology and the basic responsibilities from the model should be expressed in the code

Only one model should apply to one particular part of the system

The design should feed back into the model. Specialised roles for analysis, modelling, design interfere with that because feedback is slow, stuff is lost in communication. Model choices could affect operation performance when implemented - when this happens you want to just make minor changes to the model and not abandon it. People who write code need to feel responsible for the model.

Anyone touching the model should spend time touching the code. Anyone touching the code should be involved in modelling and have contact with domain experts.

## Ideas

- "Binding the model and the implementation" - Prototyping with just a test framework and no UI enables interactive discussion with domain experts about the model and its consequences (p11)
- "knowledge crunching is not a solitary activity" - raw material comes from domain experts, users of existing systems, prior experience of tech team. Without collaboration with domain experts, the knowledge built up is shallow, and the software is disconnected from their way of thinking.
- "Business activities and rules are as central to a domain as are the entities involved" (p17, p18 overbooking policy example)
- "If sophisticated domain experts don't understand the model, there's something wrong with the model" (p33)
- You can used informal UML diagrams to anchor a discussion, but don't try and include everything. "Sketch a diagram of three to five objects central to the issue at hand" "Comprehensive diagrams of the entire object model overwhelm the reader" (p36)
- Diagrams in a design document can be hand drawn - they should feel casual and temporary (p39)
- Don't mislead users by hiding the model - example of favourites in IE being modelled as files with filename restrictions (p57)
