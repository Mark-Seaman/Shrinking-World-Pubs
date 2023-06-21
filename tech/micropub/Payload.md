# Micropub Product Deliverables

Perhaps the most interesting aspect of micropublishing is the ability to work on information that
can be published at several different levels of detail.  Publishing content begins with constructing
the full information network for the body of knowledge.  Imagine building a web from the set of pages in 
a book by finding all of the related interconnections.  

From this info web a set of products can be created at the desired level of detail.  This can range
from a book to a single message. The same information can be published at very different levels of
granularity.


## Payloads

There are several levels of publishing payloads that are composed by nesting them together.  Each
level holds roughly four times the content of the previous level.   Live lectures, videos, and written
materials all can be represented in these payloads.  

- Message  - 50 words - 1 min video
- Post     - 1 page   - 5 min video
- Article  - 5 pages  - 20 min video
- Micropub - 20 pages - 1 hour video
- Minipub  - 80 pages - 4 hour video
- FullPub  - 320 pages - 20 hour video


<img alt="Micropub Payloads" src="/static/images/shrinking-world.com/tech/Payloads.png" width='600'/>


## Payload Details

Each level in the information hierarchy represents an expansion of roughly four times the amount of
information.  Each level can be published in either written or video forms, or both.  At the
low end, a single Message of 50 words can be equated to a 1-minute video explaining the same idea.
At the high end, a book with 320 pages is roughly equivalent to a video course consisting of 50,
30-minute sessions.

* [Message Payload](micropub-Message)
* [Post Payload](micropub-Post)
* [Article Payload](micropub-Article)
* [Seminar Payload](micropub-Seminar)
* [Minicourse Payload](micropub-Minicourse)
* [Course Payload](micropub-Course)

