---
title: "February 2003 Newsletter"
date: 2003-02-01
newsletter: "february-2003"
---

Editor: **Chris Douce**

# Contents

[Editorial]( {{< localref "#editorial" >}} )

**[Workshop Review]( {{< localref "#workshop-reviews" >}} )** **Marian Petre** reports on HCC and ESP.

**[Book and Journal Reviews]( {{< localref "#book-and-journal-reviews" >}} )** - **Chris Douce** reviews *The Pragmatic Programmer* by **Andrew Hunt** and **David Thomas**.

**[Conferences, Workshops and Call for Papers]( {{< localref "#conferences-workshops-and-call-for-papers" >}} )**

**[Bibliographies]( {{< localref "#bibliographies" >}} )** - A journey into literature surrounding theories and models of programming by **Chris Douce**

**[Books]( {{< localref "#books" >}} )** - **Derek Jones** presents a number of books that will be of interest to those new to the Psychology of Programming.

**[Doddery Fodder 3: Going Over the Limit]( {{< localref "#doddery-fodder-3-going-over-the-limit" >}} )** *Another eclectic selection of related sites* by **Frank Wales**.

---

# Editorial

Welcome to the Winter 2003 edition of the Psychology of Programming newsletter.

This issue contains the first PPIG related bibliography. It reflects one of my research interests - cognitive models of programming. These days I am primarily a 'pragmatic programmer' (see book review) and have not had much opportunity to keep up with current (and also previous!) publications as I would have liked.

I am hoping that the inclusion of the bibliography section will set a precedent, inspiring others to write their own. Other topics could include 'the programming team', 'programmer education', 'debugging' or 'programming tools' and 'language design'. The more interdisciplinary they are, the more fun they are to read!

Many thanks to Derek Jones for his list of books for those of us who are new (and old) to the Psychology of Programming. There were many books that I recognised (and some that I didn't). I feel his list will be useful for many newsletter readers. Well done Derek!

Remember, this is your newsletter. If you read a paper, book or discover a new journal that you feel may be of interest to the PPIG community, please do tell us. We are always interested to hear about how PPIG members are. Please do tell us how you are and how they are getting along.

Please feel free to send me inclusions, comments (and corrections?) at any time. I am always happy to hear from you.

Looking forward to seeing you all in June!

Hope you enjoy the newsletter.

**Chris Douce** \
_Chrisd@fdbk.co.uk_

---

# Workshop Reviews

## Human Centric Computing Languages and Environments (HCC) and Empirical Studies of Programmers (ESP)

_2-6 September 2002, Arlington, VA_

By **Marian Petre**

The good news is that 'ESP is back' - this time as one of three symposia at Human Centric Computing Languages and Environments (formerly Visual Languages), an IEEE-sponsored conference.

HCC is organised into distinct symposia, each with its own, largely autonomous committee. (Susan Weidenbeck, of Drexel University, and I chaired this year's ESP.) Submissions to ESP were strong, and there were good interactions with the other symposia: Visual/Multimedia Programming and Software Engineering, and End-User Programming.

Although HCC is suffering - like most US conferences - from lowered attendance, the conference was vigorous and interesting, with international attendance of about 60, including familiar faces from both the ESP and PPIG communities.

HCC featured three provocative keynote talks, all of potential interest to PPIG members:

*   Ben Bederson, Human-Computer Interaction Lab, University of Maryland: \
    *Interfaces for staying in the flow*

Ben introduced interface design guidelines relating to the principle of encouraging 'flow', or 'optimal experiences' in interactions. The gist was to minimise cognitive load while maximising subjective satisfaction.

He of course showed some nifty examples, such as 'flow menus' (Guimbretiere et al.) and 'photo menus' (on his web site). And there was some interesting discussion about how 'flow' relates to different sorts of experiences: team working, generative tasks, and responsive/reactive tasks.

*   Randy Pausch, Carnegie Mellon University: \
    *Alice - a system using 3D graphics to teach computer programming*

Alice is a largely drag-and-drop programming environment for animating 3D models, aimed at 'middle school' students. It has undergone years of development and a variety of evaluations, and it has sex appeal.

It's hard to beat Randy Pausch as a quotation generator (and quoter), e.g.: *'Code continues to be the best way to express program logic, even for novices'.*, *'If' statements aren't that hard; the syntax for anything is hard...the intellectual effort in a typical intro programming course is more than half teaching syntax to a particular language.'*, *'Parallel programming is child's play; synchronisation is hard.'*

*   Clayton Lewis, University of Colorado at Boulder: \
    *HCI – where are we now, where might we go from here?*

Clayton is, deservedly, a PPIG hero. He presented a survey of 'influential talks' and key developments in HCI, and he considered 'What now?' Recurrent themes included that 'We've learned that empirical, feedback-driven methods will produce useful and usable systems' and 'The critical issue isn't technology, it's engagement with the details of the problems' and 'Engaging the specifics requires crossing discipline lines.'

He made an appeal that researchers engage the underlying, human problems - the problems behind many of the problems we study. He predicted that within 10 years 'advances in the science of human nature will contribute in fundamental ways to the work we do.'

Susan Wiedenbeck and I led a panel/discussion session on Empirical studies of programming-in-the-large which generated considerable energy and interest. This was a reprise of a similar session at IWPC a couple of years ago and drew in results from a highly-informal PPIG survey at that time.

Its focal questions were: What are the questions that can only be addressed by studying programming-in-the-large? and What are the big questions in software engineering / programming that should be addressed by empirical research? We expect to collaborate on a paper based on those discussions.

My most memorable image from the conference is from Randy Pausch: a photo of one of his programmers doing user testing _sitting on his hands_. Their rule is that the programmer can't help the users without admitting: *I'm sorry I wrote such a crappy system; let me help you overcome it.*

The Proceedings are published by IEEE, ISBN 0-7695-1644-0.

---

# Book and Journal Reviews

By **Chris Douce**

## *The Pragmatic Programmer: From Journeyman to Master*, Andrew Hunt and David Thomas

***The Pragmatic Programmer: From Journeyman to Master*** \
by **Andrew Hunt** and **David Thomas** \
Addison Wesley, 1997 \
ISBN 0-201-61622

I have been threatening to read this edition of the *Programmatic Programmer* ever since it was published. There are, of course, many different 'types' of programmer - applications programmer, systems programmer, firmware programmer, 'web' programmer. The Pragmatic Programmer has been written and should be of interest to all types.

The Pragmatic Programmer provides sensible pragmatic advice in an easy to read, bite (or byte?) sized sections in a style that is easy to digest. I personally found the style agreeable. They add humour to what can be a difficult and dry topic, adding useful (and fun) explanatory anecdotes.

Many topics are familiar - the software development group, the application of design patterns and the performance of continual refactoring to enhance existing code and the use of light weight 'extreme' methologies.

For very many programmers, a significant amount of their time is spent maintaining legacy systems. Older systems are touched upon, regarding the number of digits used within dates, the importance of considering your data structures and how they could be manipulated. The focus of the text lies very much with the contemporary, Java, C++ and Python all feature. The index does not extend to assembly language, Cobol or Fortran.

The advice given is sound and sensible. I found myself on a number of occasions thinking, 'I agree, that _is_ the way to do it...', having been bitten by my own misconceived and misjudged actions during my day-to-day tasks.

Each section is complemented by a number of challenges or questions that aim to solidify the 'tips' that are given. These challenges would make useful discussion points within computer science courses, software engineering courses, or even amongst a small programming team.

Occasionally, the authors touch upon topics that are central to the psychology of programming community. Key issues include language design, naming of identifiers and comments. Language design is examined from a purely 'pragmatic' perspective. It is suggested that programmers may find it easier to solve certain types of problem if they are to design a language for a specific task.

Hunt and Thomas even go as far as showing us how very simple languages can be developed using tools such as _Bison_, also providing a simple implementation.

Identifiers are discussed in connection with the 'stoop' effect, that the names of colours are harder to read if they are written using a different colour ink. This was used as an analogy for function names, or, indeed, any form of identifier.

The authors clearly believe that programming is a craft. Look after your tools, they write. Learn your text manipulation languages, such as _Perl_, _sed_ and _awk_ well and they will serve you well in return, helping you do your job efficiently and effectively. Like a craftsman, they advise you to use your basic tools to craft other tools, such as jigs, allowing you to repeatedly carry out simple tasks that can be repeated with certainty.

Regarding documentation, the authors are especially pragmatic. About comments, they write, 'commenting source code gives you the perfect opportunity to document those elusive bits of a project that can't be documented anywhere else: engineering trade-offs, why decisions were made, what other alternatives were discarded'. They also caution about over commenting, stating that it is a maintenance overhead that can be done without

A recurring topic is education. The authors encourage the programmer to 'explore' and study the tools that they have available, such as text editors and scripting languages. They also encourage programmers to keep abreast of developments in programming practice, technological developments, approaches and methodologies. Read a book a technical book a month and try to think critically about what is written, they suggest.

There is one thing that I am not happy with, and this is the title. Whilst programming remains the core to the book, I cannot help but think that perhaps they could of called it 'the pragmatic software developer', or 'the pragmatic software architect'. Another title may have been, 'the well rounded programmer'.

Programming is, of course, much more than simply writing code. It is eliciting requirements from users, selling your concepts to your co-workers and management, writing accessible documentation, designing test cases and test strategies, explaining important concepts to the marketing department and listening to others concerns and reservations.

*The Pragmatic Programmer* reminds me a little like *Programming Pearls*, especially when it comes to the end of section questions, and the fact that *Jon Bentley (ACM Press)* describes laziness as one of the key qualities of a good programmer. *The Pragmatic Programmer* also reminds me of another text that I have been threatening to read for ages, *The Practice of Programming* by Kernighan and Pike. Another book that address similar ideas is *Code Complete* (and perhaps Writing Solid Code) by McConnell.

Some readers may find the authors style of writing a little hard to digest. I find its style appealing, primarily because it aims for accessibility. It's not a big book and can be read over a couple of hours an afternoon with the television turned on (apart from the chapter on algorithm complexity)

Whilst battling for hours over mysteriously disappearing numbers, I shall try to remember their sensible words: *"If you think it is the compiler or the operating system, it isn't likely to be either"*.

<br>

Have you read a book that you think that others may find interesting? If so, please do tell us about it. We're crying out for some reviews of some psychology books! Send all reviews and ideas to chrisd@fdbk.co.uk

---

# Conferences, Workshops and Call for Papers

## 15th Annual Workshop of the Psychology of Programming Interest Group

For the first time, PPIG will be co-located with the [Empirical Assessment of Software Engineering](http://www.keele.ac.uk/depts/cs/ease/ease2003/EASE2003Call.htm) conference.

As I am sure you are aware, the annual PPIG workshop is a forum in which researchers concerned with cognitive factors in software engineering can present and discuss recent results, findings and developments.

A feature of the PPIG workshops has been their openness to a wide spectrum of concerns related to programming and software engineering, from the design of programming languages to communication issues in software teams, and from computing education to high-performance professional practice.

Similarly, PPIG entertains a broad spectrum of research approaches, from theoretical perspectives drawing on psychological theory to empirical perspectives grounded in real-world experience.

Despite its name, PPIG aims to bring together people working in a variety of disciplines and to break down cross-disciplinary barriers.

Two guest speakers have kindly agreed to attend:

*   Dr. Chris Hundhausen \
    _Information and Computer Sciences Department, University of Hawaii_ \
    Dr. Hundhausen has research interests in computer-based visualisation systems, end-user computing, and collaborative software engineering.

*   Prof. Keith Stenning \
    _Human Communication Research Centre, University of Edinburgh_ \
    Professor Stenning's research interests lie in representation, and the learning of formal knowledge and its deployment.

The EASE-invited speaker is:

*   Prof. Anthony Finklestein \
    _Department of Computer Science, University College London_ \
    Professor Finklestein's research interests lie in software systems engineering, especially requirements engineering, software processes and software architecture.

During the morning of 8 April, and at intervals during the rest of the workshop, PPIG and EASE will be hosting activities aimed at research students from both communities. Both PPIG and EASE have always welcomed research students; this is a great community for contacts and discussion.

More detailed information about this fantastic event can always be found from the workshop page on the [PPIG website](http://www.ppig.org/workshops/15th.html).

Further announcements regarding PPIG and EASE will be made on the mailing list.

## Agile Development Conference

Agile Development is a conference aimed at exploring the human and social issues involved in software development and the consequences of the agile approach to developing software. A number of techniques and processes have been identified in the use of agile approaches, and we expect more to be found.

The purpose of this conference is to examine the proposed processes and techniques, to report the outcome of studies on human issues affecting the speed and quality of the development, and to collect field reports from projects using agile approaches.

The social-technical goal of the conference is to increase the exchange on these issues between researchers and practitioners, between managers and developers, between social specialists and computer specialists.

The _Agile Development Conference_ will be held between June 25 and June 28 in Salt Lake City, Utah, USA.

More information about the conference can be found at:

[Agile Development Conference](http://www.agiledevelopmentconference.com/submissions/index.html)

## IEEE Symposium on End-User and Domain-Specific Programming

The Symposium on End-User and Domain-Specific Programming is the premier international forum on the theory, design and application of languages for end users.

End-User programming emphasises the needs of users who are not professional programmers, but must engage in some form of programming to accomplish their tasks.

We distinguish domain-specific languages from general purpose languages in that they address the needs of users in a particular field. Both of these research topics emphasise the human requirements of programming tools.

Research in this area almost always requires evaluation - either analytical or empirical - to support claims of benefits to be gained from prototype systems or theoretical research. Empirical studies of programming are particularly welcome at EUP'03.

Specific topics of interest include:

*   Analytical investigations of the needs of end-users
*   Studies of contexts where domain-specific programming is needed
*   Descriptions of novel programming languages and environments
*   Empirical studies of end-user or domain-specific programming
*   Evaluation of commercial or research programming systems

The symposium will take place in Auckland, New Zealand between October 28 and 31\. It's a long way, but organisers promise to make local costs so low that even with the airfare, it won't be much more expensive than attending conferences in the USA.

NSF funding is anticipated to fund travel by a few graduate student researchers working on certain types of end-user programming.

More information can be found by visiting the : [workshop website](http://www.cs.dal.ca/HCC03/EUP/)

## International Workshop on Program Comprehension

IWPC 2003, 11th International Workshop on Program Comprehension will be held between May 10 and May 11 in Portland, Oregon.

More information about the event and the forthcoming programme can be found by visiting the [IWPC website](http://www.iwpc2003.uvic.ca/)

## Workshop on Expertise in Design

The forthcoming Workshop on _Expertise in Design_, is to be held in Sydney, Australia, between 17 and 19 October 2003.

The workshop will focus on what we understand about the nature and practice of expertise in design across all domains of design practice.

More information can be found by visiting the [workshop website](http://http//www.designthinkingresearch.com)

## Computer Science Education Journal

Moti will be editing the March 2004 issue of the journal Computer Science Education, which will be a special issue devoted to CSE in high schools. Key topics include:

*   The pedagogy of CS subjects for high school students
*   The cognition of CS students in high schools
*   Social aspects of teaching and learning CS in high schools
*   Technology of CSE in high schools: laboratories, systems, languages, tools

Preference will be given to papers describing empirical experiments or otherwise presenting evidence of experience, and to papers concerning the teaching of 'academic' computer science subjects.

More information about this special issue can be seen by viewing the web-based [call for papers](http://stwww.weizmann.ac.il/g-cs/benari/cfp.htm).

---

# Bibliographies

This column presents a 'snapshot' of my journey through some psychology of programming (and other!) literature. At the same time that this journey was unfolding, there were others occurring simultaneously. If you so feel inclined, please tell us yours!

## Models of Programming

By **Chris Douce**

### Introduction

The topic of program comprehension became an interest of mine ever since I had my first 'proper' programming position - a temporary summer vacation job carrying out maintenance of a simple inventory system.

In that same year I stumbled across Weinberg's The psychology of Computer Programming which piqued my interest and subsequently my reading. This bibliography is a 'meandering' around the topic of 'models of programming'.

Studying this element of program comprehension took me into the realm of software engineering where I was presented with their metrics and methodologies, and outwards towards fascinating area of cognitive psychology. When I discovered that cognitive psychology was discipline of its own, my thoughts were, 'why didn't I know of this earlier?'

It's a shame that I don't have more time these days to read as many papers as I used to now that I am a programming practitioner. I have to say that my interest in the programmer and the activity of programming has not diminished with 'practice'. It has increased.

I hope you enjoy this as much as I enjoyed putting it together. It is also my hope that others may make create different connections between the papers than I have made. If one of these papers reminds me of another relevant paper or book that you think is related (or even one that isn't!), I would like to hear from you.

### A Bibliographic Journey

After reading *The Psychology of Computer Programming*, whilst perusing the shelves of my university library several years later I stumbled across:

> Shneiderman, B. (1980). Software psychology: human factors in computer and information systems. Cambridge, MA., Winthrop.

carefully tucked away next to Jean Sammets' masterwork on programming languages. After some questioning at the university library, *Software Psychology* lead me towards a paper that described a simple model of programmers memory. It was a model that I could immediately understand and appreciate:

> Shneiderman, B. and R. E. Mayer (1979). Syntactic/semantic interactions in programmer behaviour: a model and experimental results. International Journal of Computer and Information Sciences 8: 219-238.

This was especially interesting, since his co-author, Richard Mayer, was an author of a set text that I had to use whilst studying a problem solving and 'intelligence' class at university:

> Mayer, R. E. (1991). Thinking, problem solving and cognition, W.H.Freeman and Company.

Associations between models of computer programming and cognitive psychology was firmly established with this discovery. This lead me towards the fantastic:

> Eysenck, M. W. and M. T. Keane (1996). Cognitive psychology: a students handbook. Hove, Psychology Press.

Whilst wading through sections of this weighty tome, memory and computer programming appeared to be of interest to the authors, since the activity of programming was used to study the notion of 'expertise'.

Inspired by this purchase, I decided to leaf through the politically incorrectly named *International Journal of Man-Machine Studies*, only to stumble upon:

> Brooks, R. (1977). Towards a theory of the cognitive processes in computer programming. International Journal of Man-Machine Studies 9: 737.

and a sister paper:

> Brooks, R. (1983). Towards a theory of the comprehension of computer programs. International Journal of Man-Machine Studies 18: 543-554.

This was, in my eyes, a significant find. It illustrated clearly that the term 'model' was not as straight forward as I had thought. These papers introduced the concept that a production system could be used as a model, and the 'direction' of comprehension - the mysterious word called 'strategy' - and the concept of a 'programming beacon'.

Continuing my perusal of IJMMS, I made a further discovery:

> Davies, S. P. (1993). Models and theories of programming strategy. International Journal of Man-Machine Studies 39: 237-267

This paper discussed my previous discoveries, and more. In a way, I felt a little cheated. Someone appeared to be making my discoveries for me. Also, this was reassuring since someone else was contemplating the same issues I was examining.

There were many papers that were new to me. One of them being:

> Pennington, N. (1987). Comprehension strategies in programming. Empirical Studies of programmers : second workshop. G. M. Olson, S. Sheppard and E. Soloway. Norwood, New Jersey, Ablex: 100-113.

I believe this was my first knowledge of an organisation called Empirical Studies of Programmers. I liked Pennington's work a lot, especially her use of 'knowledge' categories. I also admired her methodology. Soon afterwards, through Davies's references, I then discovered this kind gentleman:

> Green, T. R. G. (1980). Programming as a cognitive activity. Human Interaction with Computers. H. T. Smith and T. R. G. Green. London, Academic Press: 271-320.

This lead me onwards to discover further work about mini-languages and a discipline called 'psycholinguistics' through:

> Green, T. R. G. (1989). Cognitive dimensions of notations. People and Computers V. Sutcliffe and Macaulay. Cambridge, Cambridge University Press.

Another paper I found through the Davies paper was:

> Rist, R. S. (1986). Plans in programming: definition, demonstration and development. Empirical Studies of Programmers. Empirical Studies of programmers. E. Soloway and S. Iyengar. Norwood, New Jersey, Ablex: 28-47.

which presented a more rigorous treatment of the concept of a 'plan'. I was becoming awfully confused. I was faced with general cognitive theories, production systems, discourses regarding memory from the somewhat different (and also intrinsically related) fields of experimental psychology and cognitive science.

Of course, let's not forget to mention micro-languages about 'hungry hares'.

At this point, after a little more discovery into models of general cognition (directed by Eysneck and Keyne), I learnt of:

> Anderson, J. R. (1983). The architecture of cognition. Cambridge, MA, Harvard University Press.

and:

> Newell, A. (1990). Unified theories of cognition. Cambridge, MA, Harvard University Press.

It was at this point I decided to take a holiday.

It became clear that I was making a round trip, since I also discovered that Dr Anderson had a particular liking for LISP (and possibly its use of bracketing? See paper regarding notations!):

> Kessler, C. M. and J. R. Anderson (1986). A model of novice debugging in LISP. Empirical Studies of Programmers, Norwood, New Jersey, Ablex: 198-212.

Through his earlier work, I had learnt that he had an interest in modelling the programmer through the use of production systems. It also appeared that he also had an interest in the use and failings of memory:

> Anderson, J. R. and R. Jeffries (1985). Novice LISP errors: undetected losses of information from working memory. Human-Computer Interaction 1: 107-131.

All these strands were slowly beginning to merge together. I was simultaneously following leads on papers discussing object-oriented programming, notations, cognitive models, expertise and memory. Much to my disapproval (and delight!), I made another Davies discovery:

> Davies, S. P., D. J. Gilmore, et al. (1995). Are object that important? Effects of expertise and familiarity on classification of object-oriented code. Human-Computer Interaction 10: 227-248.

Which is related to an earlier paper:

> McKeithen, K. B., J. S. Reitman, et al. (1981). Knowledge organisation and skill differences in computer programmers. Cognitive Psychology 13: 307-325.

During my reading, I acquired a fondness for the psychology section of the library. I found it much more peaceful than the hustle and bustle of the computer science area with all its journals advocating data mining algorithms, shading techniques and recent web breakthroughs.

Sometimes these journals would yield interesting results, showing that psychology of programming is truly inter-disciplinary:

> von Mayrhauser, A. and A. M. Vans (1996). Identification of dynamic comprehension processes during large scale maintenance. IEEE Transactions on Software Engineering SE-22(6): 424-437.

Whilst returning to hide amongst the psychology journals to contemplate the complexities of object-oriented programming in peace, I could not help but begin to wander down a rather interesting path of 'categorisation':

> Rosch, E. (1975). Cognitive representations of semantic categories. Journal of Experimental Psychology 104(3): 192-233.

I began to reason that an _object_ is an instance of a _class_, like a _chair_ is an instance of a piece of _furniture_.

I concluded that I was in need of a second holiday.

Nothing had prepared me for how much material could be of use to someone trying to understand the often mysterious and challenging activity of programming. I became embroiled in the debates surrounding psychology (and engineering) methodology, issues regarding group working, software metrics and arguments surrounding their validity.

In the end, my interest settled to a certain sub area: _memory_. The types of memory and how they are used by programmers. Just this week I said, 'I know that I had a concern about this program and I have written it down somewhere in the outline specification…'. My memory of 'comprehended' source code had affected the testing of a software product twelve months later.

Within experimental and cognitive psychology, memory research appeared to have a substantial amount of published literature. As a simple computer scientist, I found myself _forgetting_ the titles of some of the paper that I had read, even photocopying some papers twice!

One memory book particularly caught my eye:

> Cohen, G. (1989). Memory in the real world. Hove, Lawence Erlbaum Associates.

Programming is a task that relies on knowledge existing in the 'world', since software artefacts are so intangible. This was a good start. More recent texts that I particularly admire are:

> Groeger, J. A. (1997). Memory and remembering : everyday memory in context. Harlow, England, Addison-Wesley Longman.

and:

> Baddeley, A. D. (1997). Human memory : theory and practice - revised edition. Hove, Psychology Press.

All good text books have to potential to take you on journeys of fascination. Through their text and their references they can show you misty peaks of knowledge sitting powerfully in the distance, outlining a journey that you may consider making in the future. Baddeley was no exception:

> Baddeley, A. D. (1984). Neuropsychological evidence and the semantic/episodic distinction. Behavioural and Brain Sciences 7: 238-239.

I was stepping into an area that could potentially be called, 'the cognitive-neuropsychology of computer programming'. My journey was becoming weirder.

As I sat on the floor of a university library surrounded by mysterious sounding medical journals, I wondered whether I was reading this paper because of a paper that I had deliberately sought out at the start of my journey:

> Shneiderman, B. and R. E. Mayer (1979). Syntactic/semantic interactions in programmer behaviour: a model and experimental results. International Journal of Computer and Information Sciences 8: 219-238.

It almost felt as if I had returned to the beginning. I stopped here for a while and wondered where I had been and where I was going to go next.

It struck me that programming is an activity that is, on one hand, something special. But on the other, it is an activity that is not special, since it uses faculties that we all possess.

_Real_ programming - software development to solve _real problems_ can be _deliciously_ challenging and _incredibly_ frustrating. This is what makes programming special. By studying what occurs during the creation of imaginary cathedrals we may be able to learn a little bit more about ourselves, and how our creations could be built that little bit better.

---

# Books

## Psychology Texts

By **Derek Jones**

What psychology books should somebody new to the psychology of programming read? The following list briefly reviews books that I found to be useful:

> Cognitive Psychology and its Implications by J. R. Anderson. \
> ISBN 0-7167-3678-0

A very readable book now in its fifth edition. Let down by a poor index (and some of the references appear to be inaccurate).

> Cognitive Psychology: A students handbook by M. W. Eysenck and M. T. Keane. \
> ISBN 0-86377-551-9

A very readable book now in its fourth edition. A better index than Anderson (based on looking up entries in both).

Which would I choose? To read I preferred Anderson. But then this is the first modern introductory book on cognitive psychology I have read, which may have coloured my view. I liked his attempt to explain the purpose behind everything (having a physics/engineering background this appealed to me).

But then looking around several university bookshops and the Amazon ranking system, Eysenck & Keane win hands down. So perhaps their book appeals to a more general audience.

Those wanting a more concrete, practical applications approach to psychology might like to try:

> Engineering Psychology and Human Performance by C. D. Wickens and J.G. Hollands. \
> ISBN 0-321-04711-7

So, what about books dealing with more specific subjects? The following list of books has some connection with software development and are probably still in print:

> The Number Sense by S. Dehaene. \
> ISBN 0-14-026134-6

Aimed at the educated lay reader this book contains plenty of interesting and surprising material on how people perform arithmetic.

> Comprehension: A paradigm for cognition by W. Kintsch. \
> ISBN 0-521-62986-1

An up to date theory of text comprehension by one of the major researchers in the field (hard work in places).

> Reasoning and Thinking by K. Manktelow. \
> ISBN 0-86377-709-0

A readable introduction (compared to other many books on the topic) to empirical findings and theories that have been proposed to explain them.

> Human Error by J. Reason. \
> ISBN 0-521-31419-4

The standard reference on the topic and readable to boot.

> The Adaptive Decision Maker by J. Payne, J. R. Bettman, E. J. Johnson. \
> ISBN 0-521-42526-3

Designing programs is about making lots of decisions and here is a book that discusses how people make them.

> The Psychology of Language by T. Harley. \
> ISBN 0-86377-867-4

provides a comprehensive, readable account of the subject.

Writing maintaining software involves a lot of learning (about the application and its implementation). The following provides a more detailed, but very readable, discussion of this specialist topic.

> Learning and memory by J. R. Anderson. \
> ISBN 0-471-24925-4

A good source for locating second hand books is: [AddAll](http://www.addall.com/Used/)

# Doddery Fodder 3: Going Over the Limit

By **Frank Wales**

Does the study of the psychology of programming encompass the psychological burdens of being a programmer? I ask, because the other day I came across what a Java compiler blithely calls an "implementation restriction" which was so unexpected, and so dumb, that I could gleefully have strangled whoever was responsible for taking the decisions that led to it. And I'm quite a restrained person; ask anyone I haven't strangled yet.

The thing that annoyed me was the discovery that Java identifiers and the object code for methods have something in common, namely that both are restricted to about 65,536 bytes in length. Now, this is jolly long for an identifier, and good enough for me. But 65,536 bytes as the maximum length of a method's object code? Even Bill Gates's famous underestimate of the amount of memory a PC would ever need was ten times more than that.

Note, by the way, that the restriction is in the standardised file format for Java classes, and not inherent in the language itself, which is why it's more of a surprise when you encounter it, and also why you can't just work around it by diddling with compiler options. Given that these restrictions were imposed well into the Age of Bloatware, it's hard to know what their devisors were thinking, other than _not ahead_. \
[java.sun.com/docs/books/vmspec/2nd-edition/html/ClassFile.doc.html#88659](http://java.sun.com/docs/books/vmspec/2nd-edition/html/ClassFile.doc.html#88659)

Still, supposedly a committee somewhere is pondering how to deal with this long-standing problem, especially as it affects people like me who aren't directly writing the offending Java, but instead are working in other languages that generate the Java that then can't be compiled. In the meantime, I'm stuck with making apparently nonsensical changes to my code so that the underlying Java generator creates output that the compiler can, in its turn, compile into something that can then be saved into the aforementioned overly-restrictive file format, so that it can eventually be loaded and run.

## Running backwards?

Trying to find a workaround for this sent me on a hunt for Java tools, where I came across **RetroVue**, lauded by father of Java James Gosling as: "a strong opportunity to dramatically improve the software development process." \
[www.visicomp.com](http://www.visicomp.com/)

This tool claims to let you run the clock backwards on your Java application, retracing its steps from _"Why did it do that?"_ to _"Oops, looks like we shouldn't have invoked the `system.haltAndCatchFire()` method._"

I'll be interested to see if there is any empirical research on the merits of doing this, especially as a similar feature in a debugger that I worked on in the 1980s was rejected by its users, partly because of the feature's impact on execution speed, and partly because it was so unlike any other tool they had.

Back in the monotonically increasing world, the desire to remove the cruft from software development has produced the _Agile Alliance_, whose motto seems to be: "lead, follow, or get out of the way." \
[www.agilealliance.com/home](http://www.agilealliance.com/home)

No doubt their lack of enthusiasm for processes, tools, planning, documentation and contracts will scare the pants off some members of the audience.

## Simpler days

My run-in with papered-over Java also had me yearning for the Simpler Days when I didn't have _n_ loosely-coupled technologies between me and the actual computer, where _n_ is too large, and quite possibly fractal. You know, the days when digital watches still had Nixie tube displays: \
[www.amug.org/~jthomas/watch.html](http://www.amug.org/~jthomas/watch.html)

Apparently, I'm not the only one who thinks this way, and there are still languages being devised that are trying to either reorganise all this surprising complexity, or even side-step it completely:

*   **colorForth** is a stand-alone redesign of that old favourite minimalist language, Forth, and appears to be an attempt to see how much can be thrown out from programming languages and operating systems while still being able to get anything done: \
    [www.colorforth.com/cf.html](http://www.colorforth.com/cf.html)
*   **Joy** claims to be a pure functional cousin of Forth, and seems to do without such fripperies as named formal parameters to functions, named variables, and infix notation: \
    [www.latrobe.edu.au/philosophy/phimvt/joy.html](http://www.latrobe.edu.au/philosophy/phimvt/joy.html)

*   And **Cow** disposes of the programmer in favour of a cow, which is probably going a little too far, at least as far as I'm concerned. \
    [www.bigzaphod.org/cow](http://www.bigzaphod.org/cow/)

In its favour, **Cow**'s implementation of the stereotypical Fibonacci number generator is quite small:

```MoO moO MoO mOo MOO OOM MMM moO moO MMM mOo mOo moO MMM mOo MMM moO moO MOO MOo mOo MoO moO moo mOo mOo moo```

**Cow** probably also sounds better on the radio than the source code to the Linux kernel, presently being broadcast on **Free Radio Linux**: \
[radioqualia.va.com.au/freeradiolinux/](http://radioqualia.va.com.au/freeradiolinux/)

If they want to attract non-geeky listeners, I think they need to include fewer network drivers and more racing car drivers. But that's just my taste.

_ED:_ I wonder whether there will be a textbook for _Joy_ called _The Joy of Joy_.

## Getting serious

Still, serious problems need serious languages, and **D** looks like a serious attempt to take all the good bits from C, C++ and other languages, while leaving out at least some of the horrible nightmares. The approach is driven from experience in writing compilers, and selects or omits features based on what is practical to implement efficiently and correctly, rather than what theoreticians think is neat: \
[ww.digitalmars.com/d](http://www.digitalmars.com/d/)

If all this talk of new languages has made you want to remind yourself of the merits of functional programming or the lambda calculus, you'll be pleased to know that the classic MIT textbook *Structure and Interpretation of Computer Programs* is now available entirely online: \
[mitpress.mit.edu/sicp/full-text/book/book.html](http://mitpress.mit.edu/sicp/full-text/book/book.html)

And if you can't cope with all that LISPy code, you could always consider using Don Knuth's latest pedagogical language, **MMIX**: \
[www-cs-faculty.stanford.edu/~knuth/mmix.html](http://www-cs-faculty.stanford.edu/~knuth/mmix.html)

Don explains more about its design here: \
[technetcast.ddj.com/tnc_program.html?program_id=71](http://technetcast.ddj.com/tnc_program.html?program_id=71)

He defends his continuing use of an assembly-level language in *The Art of Computer Programming*, saying: "People who are more than casually interested in computers should have at least some idea of what the underlying hardware is like. Otherwise the programs they write will be pretty weird."

Finally, if you want to get up to date with trendy application development for the web, look no further than *Creating Applications with Mozilla*, which is also available entirely online: \
[books.mozdev.org](http://books.mozdev.org/)

## Seeking counsel

Until more certified accountants barge their way into the field, meta-level compilation seems like a good way to find bugs in systems that are, quite frankly, too boring for many programmers to look for: \
[metacomp.stanford.edu](http://metacomp.stanford.edu/)

An offshoot from this project is now starting to correllate what might be called sloppy or accidental code features with real defects. It identifies such things as unused variables and code, irrelevant conditionals and other code that pointlessly repeats itself, and finds an increase in the likelihood that bugs are lurking nearby. The premise, which on the face of it seems reasonable, is that these features show that the last person to change the code either didn't understand it well enough to be tidy, or didn't care enough to be: \
[www.stanford.edu/~engler/p401-xie.ps](http://www.stanford.edu/~engler/p401-xie.ps) [.ps]

Of course, optimising compilers have been handling this kind of poor code for a while, but perhaps now instead of Band-aiding the code, the compilers will be stopping and saying: "_Oi! Programmer!_ You clearly don't understand the consequences of what you're doing here!" And the quality of code in the world might be increased by a notch, especially if intermediate code-generators have to output code that is at least average in quality.

If only there were a way to apply such principles to design specifications. If only there were a way to run the clock backwards to when such specifications were being written, for the purposes of strategic strangling. If only there were a computer that doubled as a drinks cabinet. Oh, wait, there is: \
[www.lpl.arizona.edu/~vance/www/vaxbar.html](http://www.lpl.arizona.edu/~vance/www/vaxbar.html)

Until I'm able to seek counsel for my frustrations from a psychologist for programmers, I guess some beers will have to do.

**Frank Wales** \
frank@limov.com \
www.limov.com

## Acknowledgements

Many thanks go to Frank Wales for the assistance he has given during the production of this newsletter.
