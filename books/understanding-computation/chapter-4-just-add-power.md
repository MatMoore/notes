# Just Add Power

https://learning.oreilly.com/library/view/understanding-computation/9781449330071/ch04.html

This follows on from chapter 3: Finite Automata.

## Computational power
My interpretation: this is about what it's possible to compute

*non-deterministic finite automata* have the same power as *deterministic finite automata*

Finite automata have limited power because:
- they are both limited to accepting/rejecting input
- you can create a `language` that they can't recognise

## Bracket nesting level

Problem: determine if brackets in a string are balanced `'(()(()()))'`

You can create an NFA that works for a limited number of brackets, but not for the general case.

> a finite automaton has only limited storage in the form of its fixed collection of states, which means it has **no way to keep track of an arbitrary amount of information**

## Regular expressions and HTML
To pattern match HTML you need to know if tags are closed, which is like the bracket nesting problem

So the formal definition of regex is not powerful enough to tell if your HTML is valid

[Stack overflow rant](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)

But ruby's Regex can technically solve these kinds of problems, because of extensions that allow recursion

```
balanced =
  /
    \A              # match beginning of string
    (?<brackets>    # begin subexpression called "brackets"
      \(            # match a literal opening bracket
      \g<brackets>* # match "brackets" subexpression zero or more times.   <------ RECURSION
      \)            # match a literal closing bracket
    )               # end subexpression
    *               # repeat the whole pattern zero or more times
    \z              # match end of string
  /x
 ```

## Deterministic Pushdown Automata

DPA is an extension of DFA and NFA to add *external memory* (a stack, with unlimited size)

Stack properties: last-in, first out.

```ruby
stack = [1,2,3]
stack.push(4) 
stack.pop       # --> 4
```

- With DFA and NFA each transition was based only on the input character.
- Now it's based on the input character and what's in the stack.

## Defining the rules
My interpretation: this section defines the minimal ingredients of a rule that still maximises what you can express

We keep from the DFA/NFA rules these things:

- The current state of the machine (node in the graph)
- The character that must be read from the input (optional)
- The next state of the machine 

But add these:

- The character that must be popped off the stack
- The sequence of characters to push onto the stack after the top character has been popped off

NB: You can always replace the character that was popped.

There is a special character used to mark the bottom of the stack ($). If we pop this it means the stack is empty.

## Horrific notation
`a;b/cd` means:

```
a   ;   b   /   cd

^       ^        ^
|       |        |__ push c and d back to the stack
|       |___________ if we popped b from the stack
|___________________ and read a from input
 
```

