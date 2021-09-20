# Leaddev/Staffplus 2021

This was the first time Leaddev did a staffplus track. There were 3 tracks but I only followed the Staffplus one as it seemed more interesting to me.

## What is a Staffplus role?

I went in not really understanding these roles very well. Staffplus describes the senior end of the "individual contributor path" after senior engineer, which includes titles like Staff Engineer, Senior Staff Engineer, Principal Staff Engineer, Distinguished Engineer.

It seems like it's hard to talk about these roles in a general way because it varies so much between organisations, and this path "tops out" at different places in different organisations.
Many of the speakers were from quite large engineering organisations.

One of the speakers said the way you can leverage experience as a staff engineer is by bringing hard-earned knowledge of *safety engineering* to teams that are only thinking about *product engineering*.
Safety engineering becomes more important in larger organisations where people are less willing to take big risks. Basically you are "adult supervision" for people who get excited about stuff. You think about thinks might fail.

Life experience is also valuable for empathising with how your software impacts real people.

The "I" in IC seems to be getting less relevant these days. 

Your "domain" or scope of responsibility naturally increases as you move into more senior positions. You also need to be more aware of the larger business context your area of responsibility sits within.
This can be hard if your organisation is bad at communicating and you have people filtering that information from you. A staffplus role should expose you to the problems of the business.

Silvia Botros said that "my job is to help the company go in a stategic direction" where there is a multi-year strategy. Resolves misalignment problems by escalating them.

### Skills and behaviours
Senior roles can be seen as a balance of 4 jobs:

1. A core technical skill you specialise in (for me, software engineering)
2. Product management
3. Project management
4. People management

You will be a co-leader with other people with a different balance of these skills.

You will have some degree of competence in all of them but will play to your strengths and lean on other people to fill in the gaps. Lots of talk in slack about T shaped skills and "Broken Comb" shapes.


### Contrast with Hyperspecialist
Staffplus is not a hyperspecialist. It's more of a senior generalist role.

Anecodotally hyperspecialist is still a possible career path but it seems to be less in demand these days.

If you specialise in multiple technical skills you can act as a bridge between roles.

### Similarities to roles I have done in the past
- The focus on mentoring and building capability in the organisation is very similar to my experience as a senior engineer and TL, especially when I was in the civil service
- Partnering with a manager at the same level (probably a manager of managers) is a bit like working with product managers and delievery managers. I have also worked in partnership with people at this level while I was at a lower level.
- Working at the intersection of tech and people systems reminds me of contributing to working groups at MOJ (incident response and data standards) and community projects at GDS (learning pathways, conf talks we love) which I enjoyed a lot

### Differences from roles I have done in the past
- Most people in these roles sit across many teams instead of just one.
- You don't do all these things in addition to an engineer role, you do this *instead of* shipping code.
- Lots of time is spent on the design of techno-social systems (or whatever the word is)
- Lots more delegating
- Your influence tends to be sideways rather than up and down


## How to influence (without authority)
- Keep asking questions
- Talk about unsaid parts of decision making - decisions can be biased by organisational incentives
- Senior sponsors can get you a seat at the table, but you still have to do the work
- If you reach a different decision, you could have different information or different values. Start by checking you have the same information.
- Long form writing is a superpower. You can look inwards at what can be done better.
- Find out who cares about what.
- The goal is to be neutral. Diane Tang (distinguished engineer) spends much of her time with teams that don't report to her. She is user focused and can recommend solutions and shape conversations.

## Widening your influence
- Your role may be clear within a team but unclear outside of it. You need to broadcast that information out
- When you are setting your own goals, you can disseminate that to people you intend to work with and explain how you can work together

## Global vs local optimisation
- When setting standards/processes you can think of it like a distributed system - there are a range of approaches that trade off a consistent experience and the ability to work in parallel
- Where you fall depends on organisation size

## Persuasion and information gathering
- Turn statements into questions
- Talk less, listen more
- Explicitly ask "what do you care about" "what top of mind" "what keeps you up at night"
- Make it data-driven
- Provide summarised information

## Technical writing
- Undervalued becaused the feedback loop is slower than writing code but *WRITING IS THINKING*
- Record constraints and options not picked
- Define a clear audience
- Pin docs in slack for common questions - this frees up your time for higher leverage stuff

## Calling out the current situation
- "we don't know - let's figure it out"
- "the way x+y is working together means we can't move forward"
- "this solution doesn't meet this requirement - how do we address that?"

## Developer experience = productivity
- Observability
- Reliability
- Making sure documentation is up to date
- Make sure technical debt is paid down

## Leadership
- Anarchists Guide book
- Team Topologies - good for delivering a complicated project

## How Google Meet coped with COVID demand
They had 3 objectives

1. Avoid outages (and failing that, degrade gracefully)
2. Increase serving capacity
3. Forecast demand

This talk was interesting because they described an incident response where
- the incident was ongoing rather than returning to normal within a day
- they pre-emptively declared an incident rather than waiting for things to break
- people were not expected to be 100% available

They set up standby roles for all executive roles in the incident response, who shadowed all meetings and were ready to jump in at any point. Some people in the chat questioned the cost of this, but it reminded me of job sharing arrangements, which seem more resiliant than depending on a single person.

They set up very structured workstreams for the duration of the incident so that different workstreams could continue in parallel.

- Dependency issues
- Bottlenecks
- Control knobs to ease capacity (e.g. degrading video quality, switching off captions)
- Productionising (automating ad-hoc solutions)

This sounded like it would reduce the pressure of trying to balance multiple things at once. The dependency stream can focus on building relationships with other teams and influencing their work. Bottlenecks stream can focus on investigation. Control knobs stream can focus on quick implementation. Productionising stream can think about efficiency and reliability without having to rush to get *something* live.

The workstreams approach reminded me a bit of how we approached ExpertTrack when we were under tight deadlines. Except that in this case they acknowledged it as an incident rather than business as usual.

Things that helped structure the work:
- Agreeing shared terminology
- Setting up google groups for each workstream

## Technical strategy power chords
### Pick only one goal
e.g. lower error rates to < 1%, run migrations through an automatic pipeline, increase throughput of X to Y%

You want to avoid tension between goals and allow simple solutions to be found. You can't do this if you have multiple goals that can conflict

**The approach can be multifaceted but the outcome should be simple**

### List the facts that would change your mind
i.e. the key underpinning assumptions

### Solve only the hard problem you absolutely need to

### Work backwards
Strategy is not just a start/end state - it has to be executable like a recipe.

Don't overspecify the end state, because your context will change

### Killing it with fire
This is a high consequence decision that can affect teams for years and has ripple effects throughout the organisation

There are many options

- Turndown
- Migration
- Modernisation
- Live with it

You also need to consider external dependencies beyond the owning team

When considering migrations you might need prototyping or additional staffing during the migration period.

You should articulate your principles that should guide the migration e.g. risk appetite (users should not be impacted)
