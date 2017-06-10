# The Lead Developer UK - 2007

> The Lead Developer UK 2017 is a 2-day conference featuring practical advice from experts on leading and motivating your team and high-level sessions on new and disruptive technologies.

See the [collection of resources](https://docs.google.com/document/d/1IbBTETFZ7C5li7vVjWOzTnnQrtftsKNldNIG-7VHK18/edit#heading=h.sn8v26a4d3z0) mentioned by speakers and in the slack channel.

## The Constant Life of a Tech Lead
Patrick Kua

Tech leads have to balance:
- Tech
- People
- Systems

### Tech
The tech will change. Even if you keep never make any changes to a product, the infrastructure that supports it will change.

What doesn't change is the principles we bring with us when the tech changes. Spend time on this rather than learning new tools for their own sake.

When learning new things think about what you could apply in different contexts.

For example, [the D.L. Parmas paper](https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf) - written in the 70s - is relevant to how we design microservice architectures today. [Martin Fowler's refactoring book](https://martinfowler.com/books/refactoring.html) is pretty old now but the ideas in it are still useful.

### People
People are different. Good teams are diverse.

- Different [strengths](http://strengths.gallup.com/110440/About-StrengthsFinder-20.aspx), like achiever vs strategiser
- Different [cultural dimensions](https://en.wikipedia.org/wiki/Hofstede%27s_cultural_dimensions_theory), like valuing flexibility vs minimising uncertainty
- [Pioneers/Settlers/Town planners](http://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html)


### Systems

Think about:
- Quality
- Capability
- Feedback
- Knowledge distribution

Prioritise tasks using the [Eisenhower matrix](http://jamesclear.com/eisenhower-box).

[Double loop learning](https://en.wikipedia.org/wiki/Double_loop_learning) = use feedback to reflect on your mental models as well as behaviour.

## Things You Wish You Shared With Your Team Before They Agreed on That Deadline
Dominika Rogala

In the UK, there are 252 working days in a year.

So,
- < 20 working days in a Months
- < 5 in a week

And each day is < 8h of productive time.

Don't fall into the "I'll do it in the meantime" trap.

![meantime: a mystical land where 99% of human focus is stored](https://pbs.twimg.com/media/DBykeS7XsAA---y.jpg)

Example: I just need to wait for this to thing to run. But in reality, there's set up time, fixing a bug in the thing when it doesn't run, etc.

Everyone has a default priority (low cost, time, quality). Make sure team are aligned.

## How to Talk to Earthlings?
Adrian Howard

Treat 1-1 conversations with members of your team like user research.

- Shut up
- Stay quiet. When the other person stops talking wait 4 or 5 seconds before saying something.
- "Can you tell me more about X?" - Ask reflective questions using their own words, to clarify points and focus conversation on interesting stuff.  
- Ask for stories. What happens on best/worst days?
- Avoid leading questions, ask open questions.
- Be polite and look interested.

Write up your notes. Separate observations, actions, and insights.

It's not your job to jump in and solve every problem. [Be like Alfred, not Batman](https://en.wikipedia.org/wiki/Servant_leadership).

Books: [Practical Empathy](https://www.goodreads.com/book/show/24507142-practical-empathy?from_search=true), [Interviewing Users](https://www.goodreads.com/book/show/17869520-interviewing-users).

## Ask vs. Guess Culture Communication
Katherine Wu

Concept is from an old [ask metafilter thread](http://ask.metafilter.com/55153/Whats-the-middle-ground-between-FU-and-Welcome#830421).

People assume that if the boss assigned it, it's expected.

Prefix requests to make it clear there's an alternative. Like "I understand if you're busy..." or "it's ok to say no..."

Provide positive reinforcement for saying no.

Don't default processes to people needing to ask.
Ask things like "What questions do you have for me?"

## Time to Focus on Your Goals
Maria Gutierrez -
[slides](https://speakerdeck.com/mariagutierrez/lead-dev-london-2017-time-to-focus-on-your-goals)

Take time out to set and track personal goals.

Maria follows this schedule:
- 1 day a year set aside for quiet time
- 15m every sunday (a bit longer once a month)
- 5m every day (talking with her kid about what they learned that day)

When setting goals:

1. What do you want to achieve, why?
2. Take stock of current situation, job role profiles, feedback.
3. Choose a limited number of things to improve. Keep working on some strengths.
4. Identify time bound opportunities

Ask colleagues to talk about things you want to learn more about.

## 5 Features of a Good API
HTTP RFCs: [RFC 7230](https://tools.ietf.org/html/rfc7230), [RFC 7231](https://tools.ietf.org/html/rfc7231)

Error entities should be first class. Use something like problem details ([RFC 7807](https://tools.ietf.org/html/rfc7807)).

Pretty print error JSON. Humans care more about error responses than success responses.

Link to documentation in responses. Can be a header. [RFC 6906](https://tools.ietf.org/html/rfc6906) (Profile links).

You need user identification, app identification. It's worth setting up rate limiting from the beginning even if the limit is set really high.

## Leadership Lessons from the Agile Manifesto
Anjuan Simmons

A mentor is someone who already completed "the hero's journey" and offers advice.

Lead based on influence, not reward/punishment. Motivation comes from [autonomy, mastery, purpose](https://en.wikipedia.org/wiki/Drive:_The_Surprising_Truth_About_What_Motivates_Us).

"Preserve dignity at all costs"

## YOLO Releases Considered Harmful - Running An Effective Mobile Engineering Team
Cate Huston

- Prioritisation, scope, regular releases > deadlines.
- Understand your biggest UX catastrophes, eg content loss.
- "We have a style guide so we never have to talk about it again"
- Be transparent about what you're spending time on.
- Ask people to share what they want to get done over a longer period.
- Think in the medium term.

## Forty-Two Months of Microservices. Stairway to Heaven or Highway to Hell?
Sander Hoogendoorn

## Better: Fearless Feedback for Software Teams
Erika Carlson

Purpose of feedback is:
- increasing awareness
- shaping behaviour

Types of feedback:
- Affirmative (reinforce behaviour)
- Constructive (change behaviour)
- Passive (not responding to something sends the message that it's not important)

You can schedule mutual 1-1s (both people give feedback).

### Responding to feedback
Confirm understanding "what I'm hearing you say is...".

Positive feedback:
- "Thank you"

Constructive feedback:
- Confirm
- "Thank you for you feedback"
- "I really appreciate"
- Don't respond straight away, take time to think
- Maybe schedule time to follow up

The responding part:
1. I feel ___ about this feedback
2. If strong emotions, wait for them to go away
3. Decide how to act

### Giving feedback

Be direct and structure feedback
- situation
- behaviour
- outcome

Constructive feedback:
- Assume positive intent.
- Be specific, focus on a behaviour.
- Ask before giving unsolicited constructive feedback. Give receiver options for how and when they receive the feedback.
- Confirm understanding

## The Original Skunk Works
Nickolas Means

Hire smart people and give them autonomy.

## Fail Fast, Fail Smart, Succeed
Kevin Goldsmith

Run post-mortems on successful projects.

To celebrate failure, spotify have a "fail wall".

## We're Agile, We Don't Do Documentation
Birgitta Boeckeler

![I just heard Alice explain that complex thing. AGAIN.](https://pbs.twimg.com/media/DB3rB30VYAMJuhq.jpg:large)

### Shared understanding within team and direct stakeholders

"Working on software without guidance can be anxiety producing"

Wall of common understanding
- Everything you think everyone on the team should know about the code
- Tech stack, environments, components, up for grabs
- Infographics
- Complex things you don't tough frequently

Widget kits
- Words for entities, screens
- Can have a conversation around them

Flow chart of business logic
- Create empathy between product and development
- Make the complexity of whats going on visible
- Sticky notes

### Help future selves make better decisions

Lightweight architecture decision records
- Date, status, context, decision, consequences
- Describe the problem, not the solution.
- Make it easy with templates and [tooling](https://github.com/npryce/adr-tools).

### How to make it not go out of date
- More or less up to date is fine
- Throwing stuff away is fine; keep it small
- Make it visible; include in rituals
- Create ownership through collaboration (don't just write it all yourself)

## Building and Scaling a Distributed and Inclusive Team
Mathias Meyer

Books: [The open organisation](https://www.redhat.com/en/explore/the-open-organization-book), [Turn the Ship Around!](http://www.davidmarquet.com/)

## Big Rewrite Strikes Again
Sabrina Leandro

Getting support for a rewrite:
- Make business plan
- Create excitement about what will be possible afterwards
- Make the vision clear without tech detail
- Can use metaphors like "hoarder's house"
- Repeat yourself
- Vision doesn't have to be perfect
- Make allies outside immediate team

Use the [strangler pattern](https://www.martinfowler.com/bliki/StranglerApplication.html) to deliver continuously.

Prioritise and cut features to move faster. Find biggest blocker; remove it; repeat.

"If we were to start over today, what would we build, knowing what we know now?"

Fun stuff:
- Write an obituary for the old thing
- Use gamification to celebrate progress (like badges with party poppers attached)

## Continuous A11y - Automate the Hell Out of It
Patrik Karisch

## Mentoring Junior Engineers @ Slack HQ
Carly Robinson - [slides](https://speakerdeck.com/carlyhasredhair/mentoring-junior-engineers-at-slack-the-lead-developer-uk-2017)

### Initial meeting

Goals:
- Create clear accountability.
- Discuss strengths and weaknesses and develop a plan.
- Communicate your own teaching/communication style

Questions to ask:
- How do you prefer to be communicated with?
- What does good mentorship look like to you?
- What are your goals?
- What are your expectations from me?

### Mentor's role

Make expectations clear for next 3, 6, 12 months. First 6 months is imposter syndrome danger zone.

Be a resource for questions, advocate for best pratices, communicate standards.

You should set goals for the quarter, track progress and celebrate success.

### Learning

Give juniors stretch projects (more autonomy, potential for failure than you are comfortable with).

Create a culture of learning, not academia (don't act like everyone knows everything already).

## Implementers, Solvers, and Finders: Rethinking the Developer Career Path
Randall Koutnik

## Tech Hiring is Sometimes an F- Experience
Crystal Huff

## The Inclusive Leader: Tips for Developing Diverse Teams
Jill Wetzler

About safety, feedback, advocacy.

- [Managering in terrible times](http://larahogan.me/blog/being-a-manager-in-terrible-times/)
- Allow person who has suffered harm to determine the response

### Giving hard feedback
- Factual, indisputable observation -> impact -> expectation -> assistance
- If they are upset, respond "are you ok?"
- Check before giving feedback: would you give the same feedback to someone with a different gender, race etc.
- Are you asking someone to be something they're not
- Should you be giving others feedback too

## Centralising the Right Things
Tom Booth

## Leading by Speaking
Lara Hogan

### Preparing a talk
- Set expectations: what are you going to cover and why?
- Build a narrative structure
- Weave in stuff to keep engagement (eg funny stories) - this shouldn't distract from the structure
- Practice in a small group to get feedback
- Have backup plan for laptop dying, bad internet

### Dealing with hard questions
- "I don't know"
- "I can get back to you after"
- "Interesting, who else in the audience knows the answer to this"
- "I hadn't thought about that"

### Getting good feedback
- Prime people with questions like "is this complex?", "does the argument hold?", "how is the pacing?".
- Practice surviving a fumble
- It's ok to request comments separately from the talk itself
- Ask them to imagine creative ways to misunderstand the points to prepare for questions that come out of nowhere
