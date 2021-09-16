# Domain Driven Design

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

## Ideas

- "Binding the model and the implementation" - Prototyping with just a test framework and no UI enables interactive discussion with domain experts about the model and its consequences (p11)
- "knowledge crunching is not a solitary activity" - raw material comes from domain experts, users of existing systems, prior experience of tech team. Without collaboration with domain experts, the knowledge built up is shallow, and the software is disconnected from their way of thinking.
- "Business activities and rules are as central to a domain as are the entities involved" (p17, p18 overbooking policy example)
- "If sophisticated domain experts don't understand the model, there's something wrong with the model" (p33)