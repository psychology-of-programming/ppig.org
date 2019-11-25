---
title: "August 2003 Newsletter"
date: 2003-08-01
newsletter: "august-2003"
---

Editor: **Chris Douce**

# Contents

[Editorial]( {{< localref "#editorial" >}} )

**[Workshop Review]( {{< localref "#workshop-review" >}} )** **Jim Buckley** compiles a witness report on PPIG 2003.

**[PPIG '04]( {{< localref "#ppig-04" >}} )** **Enda Dunican** provides us with some preliminary information regarding next years workshop.

**[Book and Journal Reviews]( {{< localref "#book-and-journal-reviews" >}} )** - **Chris Douce** reviews *The Elements of Java Style* by **Allan Vermeulen et. al**.

**[Conferences, Workshops and Call for Papers]( {{< localref "#conferences-workshops-and-call-for-papers" >}} )**

**[Newsletter Paper]( {{< localref "#newsletter-paper" >}} )** The Intangible System: What does an Executing Software System Look Like? by **Pamela O'Shea**.

**[Spotlight on PPIGers]( {{< localref "#spotlight-on-ppigers" >}} )** where you are and what you are doing.

**[Musings from the Trenches]( {{< localref "#musings-from-the-trenches" >}} )** - **Chris Douce** puts fingers-to-keys to contemplate slices of life as a professional software developer.

**[Links beyond]( {{< localref "#links-beyond" >}} )** A number web links that may be of interest to PPIG members

**[It's Doddery Fodder ...but is it Art?]( {{< localref "#it-s-doddery-fodder" >}} )** Another foray into the humourous, bizarre and interesting by **Frank Wales**.

---

# Editorial

Welcome to the Summer 2003 edition of the Psychology of Programming newsletter.  

It was nice to see so many of you at this years workshop. Many thanks go to the workshop organisers at Keele University for doing a fantastic job, creating an entertaining, energetic and successful event.

In this issue, Jim Buckley presents a brief description of the last workshop.  This is then followed by some information about  PPIG '04, to be hosted by Enda Dunican.  More information will be available in due course.

Pamela O'Shea, like Jim, also from the University of Limerick presents her PhD research proposal. Her article discusses some of the main issues with Software Visualisation Tools and some reasons why they may not have been widely adopted in industry.

This issue also sees the return of two previous columns: spotlight on PPIGers, and musings from the trenches.  We can also find (now) old favorites, reading as fresh and as entertaining as ever.  Again, many thanks goes to Frank for his doddery fodder.  I personally think that his latest contribution is his is his funniest yet.

Many thanks also go to the other contributors.  Remember, this is your newsletter. If you have read a paper, book or discover a new journal that you feel may be of interest to the PPIG community, please do tell us.

We would especially like to hear from the psychologists, sociologists, linguists and architects among you. This is a field that is fascinatingly interdisciplinary. Do tell us of your methodologies, views and opinions. We would love to hear from you. Sometimes it feels as if the programming '_P_' within PPIG speaks louder than the psychology '_P_'. Both are of interest, and both undeniably important.

We are also interested to hear of how old PPIG members are getting along, even if you have drifted away into other academic avenues of endeavor. If you remember us at all, do get in touch.

As I wrote within the last newsletter, please feel free to send me inclusions, comments (and corrections?) at any time. I am always happy to hear from you.

Looking forward to seeing you all next year!

**Chris Douce** \
_Chrisd(at)fdbk.co.uk_

---

# Workshop Review

## Psychology of Programming Interest Group (PPIG) 2003

_8-10 April 2003, University of Keele, UK._

By **Jim Buckley**, University of Limerick, Ireland.

PPIG 2003 was co-located with EASE this year in the very pleasant surroundings of Keele University. The papers ranged from keynote talks through full technical papers, to 'work-in-progress' papers that described an exciting array of current work.

_Chris Hundhausen_ gave the first keynote speech of the workshop. He described his work on ALVIS: an ALgorithm VIsualization Storyboarder, and the empirical studies that underpinned its development.

These empirical studies showed that traditional algorithm visualization software typically 'requires students to put inordinate amounts of time into... irrelevant activities', and 'discourages students and instructors from engaging in meaningful conversations about algorithms'.

ALVIS, in contrast, facilitates rapid construction of low-fidelity, interactive visualizations of algorithms. Because the tool is of low-fidelity, users are less reluctant to change the visualizations during discussion of the algorithm.

In _Judith Segal_'s keynote talk, she argued convincingly that the empirical software engineering community should learn from the HCI community and consider more qualitative studies, in an attempt to better model practice. She proposed that such studies should be used to complement, if not supplant the 'traditional scientific method' of formal controlled experiments in order to get a more realistic understanding of practice.

All of the technical papers were of a very high standard. In particular, [Sharp et al.]'s portrayal of the tensions that can arise when adopting a software quality system was particularly interesting.

Also notable were [Good and Brna]'s proposed measuring schema for assessing programmers' comprehension of their systems and [Kuittinen and Sajaniemi]'s discussion of variable roles in teaching programming.

Of the work-in-progress papers [Clarke and Becker]'s was perhaps the most intriguing. It described their studies at Microsoft's usability laboratory relating experienced programmers' usage of class APIs with the cognitive dimensions. Specifically, they related the APIs to the cognitive dimensions associated with certain 'programmer-types', and thus tried to improve the API for its intended users.

Also notable were [Tucker]'s description of the problems students have when learning, [Jadud]'s pedagogical experiences when using language design for Lego Mindstorm robots, and [Petre]'s elaboration of the insights experienced designers have when addressing difficult design problems.

All in all, PPIG this year was a very worthwhile experience, with interesting talks, interesting people and really good food. In fact, the after-dinner drinks weren't bad either!  Many thanks must go to _Marian Petre_, and the programme committee for organizing such a successful event.

---

# PPIG '04

Enda Dunican will be hosting the next PPIG workshop. It is proposed that the workshop will be held at the Institute of Technology, Carlow, Ireland. The proposed dates are between Monday 5th April 2004 and Wednesday 7th April.

More information regarding his institute and the surrounding area can be found by visiting the following links:

*   [Institute of Technology, Carlow, Ireland](http://www.itcarlow.ie/)

*   [About Carlow and surrounding area](http://www.carlowtourism.com/)

Further  details about the next PPIG workshop will be made available through the _announce_ mailing list when more information is available.

---

# Book and Journal Reviews

By **Chris Douce**

## *The Elements of Java Style*

***The Elements of Java Style*** \
by **Allan Vermeulen et. al.** \
Cambridge University Press, 2000 \
ISBN 0-521-77768-2

The title of this short pocket book has been derived from Kernighan and Plauger's classic 'Elements of Programming Style' published back in 1978. Despite a second edition of the book being published in eighty-nine, I found that it was an incredibly difficult book to get hold of.

The issue of programming style was one of the many that led me to the area of the psychology of programming. Very early in my programming career I discovered that a number of developers around me were using different formatting conventions. Like many before me, I became incredibly irritable when presented with the rigors of Fortran which required certain characters to be in particular column positions - something to do with punched cards, apparently.

I decided  there were a number of dimensions of style: naming, white space, function size, use of declarations. Was there such an issue as an 'optimal' style, I wondered? Is there a form that allows programming error to be minimised?

Styles are like habits. They can be formed by technology, by sweat through syntactic rigor. I am sure that many of us would have heard of software folklore stories (see also Lindsay Marshall's PPIG'02 paper) about an old programmer who insisted on writing line numbers, even though the compiler no longer supported them.

Recently, I found myself challenged. 'Why don't you put your assignments and declarations together? This reduces lines of code!' Embarrassed, I came to realise that this was due to my Pascal upbringing, and the pickiness of its compiler for efficiency reasons. My style, it seemed, was to some degree static due to programming indoctrination, my sense of aesthetics not moving with the programming times.

This is a book that can be read in around two hours, but its digestion will take considerably longer. It begins with truisms like, 'use familiar names' and 'question excessively long names', to good object-oriented advice such as 'use nouns when naming classes' and 'make object methods carry out only one operation'.

There are some elements that I take objection to - the use of curly braces, for example, and the adoption of two space characters per indent instead of one tab (an explanation is offered, but one that I'm not convinced about!). Using _this_ offends my senses. I prefer my own idiom.

The authors are pragmatic about comments. They ask you to use comments so that automatic documentation can be formed from source code through the documentation of classes and interfaces. They also insist that comments should reflect codebase reality, using the third-person narrative form, and to illustrate (with references, perhaps) why the code is doing what it is doing, not _what_ it is doing.

A number of familiar references are provided, along with a range of web links. _Writing Solid Code_ by _Maguire_ and _Code Complete_ by _McConnell_ both make an appearance.

_The Elements of Java Style_ strikes me as a miniature _refactoring_ text, especially when it addresses some object-oriented issues. Whilst getting hot under the collar about their bracketing (and naming) conventions, I remember what a colleague said to me a couple of weeks ago when he asked me to review some Java code that he was battling with: 'I don't care what the programming style is - as long as it is consistent', and don't come across comments like, 'this appears to work, but I do not know why'.

Second hand copies of the The Elements of Programming Style can now be found on Amazon.

**Have you read a book that you think that others may find interesting? If so, please do tell us about it. We're crying out for some reviews of psychology books! Send all reviews and ideas to chrisd(at)fdbk.co.uk**

---

# Conferences, Workshops and Call for Papers

## Step Workshop

Following on from the highly successful joint PPIG/EASE workshop in Keele at Easter, why not join with the Empirical Software Engineering community to discuss issues pertaining to evidence?

The PPIG community has done important work on the tools used by software engineers, for example, on programming languages and notations. However, PPIG shares a concern with the Empirical Software Engineering community that this work is not sufficiently informing software engineering practice.

One reason might be that the work is not sufficiently visible to practitioners; another might be scepticism as to the external validity of our results. Academic studies may seem to the practitioner to be far removed from the rich context of practice. How, then, do we design studies which are relevant to practitioners and which produce evidence which is both convincing and applicable in practice?

Do come and share your ideas at the workshop that we are running in Amsterdam on Friday 19th September as part of the [Software Technology and Engineering Practice Conference](http://www.step2003.uwaterloo.ca/).

David Budgen

## Agile Development Conference

June 25-26, 2004

Salt Lake City, Utah, USA

The Agile Development Conference is an integrated, 4-day conversation about techniques and technologies, attitudes and policies, research and experience, the management and development sides of agile software development.

The agile approach focuses on delivering business value early in the project lifetime and being able to incorporate late-breaking changes in requirements by accentuating the use of rich, informal communication channels and frequent delivery of running, tested systems, and attending to the human component of software development.

The Agile Development Conference gives attendees access to the latest thinking in this domain and bridges communities that rarely get a proper chance to exchange ideas and thoughts, bringing together researchers from labs and academia with executives, managers, and developers in the trenches of software development. The Agile Development Conference is not about a single methodology or approach, but rather provides a forum for the exchange of information regarding all agile development technologies.

We invite you to share your knowledge and experience via the submission of Research Papers and Experience Reports for the 2004 Agile Development Conference. Research Papers present significant contributions to the field of agile software development, advancing the state of the art, influencing the framework of thought in the field, or, perhaps, criticizing current agile development methodologies in a reasoned fashion. Experience Reports contain first-hand information and reflection, offering valuable knowledge gained through hands-on experience in real projects. Papers may present a view of what works, what doesn't, and why, in employing agile methods in software development projects.

The following are example paper topics, but submissions are by no means limited to themes listed here:

*   Research on new, or existing, agile development (AD) methodologies and approaches, including Adaptive, Crystal, DSDM, FDD, Scrum, XP.

*   Case studies, empirical studies involving agile development or a particular technique, tool, or approach; What has worked; What hasn't? What sort of gains (if any) was seen in projects employing an agile approach?

*   Does AD scale? to development in the large (including multi-person/multi-year/multi-component projects)? to safety-critical, life-critical, mission-critical systems?

*   Critical comparisons/evaluations of alternative AD methodologies; is there a 'more perfect world' that involves picking and choosing the best from each?

*   Business analyses – e.g., is AD cost-effective and justified?

*   Management of AD projects, teams, and individuals therein

*   Relationships between AD and user-centered design (UCD)

*   Cognitive aspects of AD; Cognitive aspects of software development (psychology of programming and design) and consequences for AD

*   Patterns and AD; Patterns for AD

*   Introducing AD into existing IT organizations; reactions of developers and executives to AD

*   Sociology of AD; Are there people-oriented problems involved in applying AD methods, and how can they be solved? Sociology of software development and consequences for AD

*   Relationships between CSCW (computer supported cooperative work) and AD

*   Tools for AD, computer-based and others.

More information can be found at the conference [website](http://www.agiledevelopmentconference.com/). Authors are invited to submit papers by January 30, 2004.

**Conference Chair:** Todd Little, Landmark Graphics

**Research Papers Chair:** Sherman R. Alpert, IBM Watson Research Center

**Experience Reports Chair:** Andy Pols, Pols Consulting Ltd



# Newsletter Paper

#### The Intangible System: What does an Executing Software System Look Like?

An Approach to improving Program Comprehension using Software Visualisation within the Debugging Environment

**Pamela O'Shea**
Software Visualisation and Cognition Research Group \
Department of Computer Science and Information Systems \
University of Limerick, Ireland

pamela.oshea(at)ul.ie \
Supervisor: Dr. Chris Exton

**Abstract**

For decades the same limited set of questions have been asked within debuggers, but what about all those other questions that are asked but cannot be answered within the context of today's debuggers? For example, what does the data flow for this project look like in real-time? Or what are the variable values that affect the value of variable X here?

The debugging environment has been stepped-over and ignored for years without taking into consideration the needs of current software engineers. This research re-focuses on the needs of modern software engineers and plans an investigation into whether Software Visualisation is supportive in answering such questions using abstractions of the software system.

**1. Introduction**

At present, there is no standard such as the Unified Modelling Language (UML) that can be used to describe how an executing software system should be represented on screen. The dynamics of an Object-Oriented system reveal quite a lot about the nature of the system and much of this information cannot be gathered until runtime [Smith and Munro 2002], [DePauw et al 1998], [Gargiulo and Mancoridis 2001].

Software Visualisation has the most potential in the dynamic representation of an executing system. The fact that this avenue of research is generally unexplored is discussed by [Smith and Munro 2002], where the authors make the argument that "Software is inherently dynamic, yet much of the analysis and comprehension processes focus entirely on the static source code of the software".

As a result, the software engineer is currently missing a large piece of the puzzle by only having static information and minor profiling information available when debugging. This article discusses Software Visualisation (SV) as a potential solution to this problem, where integration of static and dynamic views is prioritised along with support for switching between comprehension strategies.

It is interesting to note that many of the SV papers that describe tools, do not make any claims on program comprehension. This is surprising, since the goal of software visualisation is to aid understanding and reduce the burden of comprehension.

Why then are somany unsupported claims made regarding the benefits of software visualisation? It can hardly be considered not relevant but instead program comprehension may not be seen as a priority when in fact it should be used to influence the requirements phase of the SV tool and again upon tool completion to validate its effectiveness.

This research plans to take the less travelled road by not only implementing the proposed SV tool but by also conducting an empirical study that will be performed before the tool is written, along with a second study once the tool is complete. In this way, the experimental results will influence the design of the tool ensuring that program comprehension is kept in mind at all stages and not ignored during the valuable requirements phase.

**1.1 Issues with current SV Tools**

Software Visualisation tools are quite abundant both commercially and academically. However, when a closer examination is taken it can be seen that there is a lot of noise in the results. For example, many tools fail to meet one or more of the following criteria which may be acceptable for their own purposes but make them unsuitable when the target audience is professional software engineers.

*   Source code alterations are needed to create the visualisation, e.g. calls to a custom built visualisation library provided by the tool.
*   The tool does not scale well to larger industrial sized programs.
*   The tool only applies to a language that is not popularly used in industry, for example, Pascal, LISP, etc. While these languages have their niches, they are not targeting the average programmer in industry who uses C, C++, Java, Python etc.
*   No dynamic or runtime information is provided.
*   Only one aspect of the system is considered, for example, the tool may concentrate on control flow or software architecture and ignore data flow and source code views etc.
*   Occlusion can occur easily.
*   The tool is difficult to install and/or requires a specific library or operating system.
*   The tool is stand-alone and not integrated into a debugger or integrated development environment and as a result the user must not only switch views but also programs and the two have no means of being synchronised together, for example, as the user steps through the debugger the visualisation cannot be updated.

To examine an executing software system in its entirety, a large number of SV tools would have to be used together. That is, SV tools are specialised, performing one job or another. For example, Tool A will present control flow information, Tool B will present data flow and source code views, and another Tool C will present the software architecture view. While there are many excellent SV tools available, integration problems arise as each tool supports different languages and platforms, while others for example, are propriety.

It is perfectly natural that each tool is built to perform a certain job, after all one tool alone cannot be expected to do all and decide to show both static and dynamic information of an executing system at varying degrees of abstraction, such as, source code, control flow, data flow, state, functional, runtime relationships, software architecture etc.

However, the professional software engineer is receiving a very muddled picture of software visualisation at present and this may be one of the reasons for its lack of adoption in industry. At least academically, researchers should be combining their effort into an open-framework that is integrated into an environment currently used by software engineers, such as Eclipse [Eclipse] or Netbeans [Netbeans]. This would allow for tool designers to concentrate on implementing their view of a system and to release it as another SV view within the context of the debugger. That is, the user should be able to choose from a variety of views within the one environment.

A proposed solution will be described in the next section where a monitoring framework for Java is integrated into the Netbeans IDE and can be build upon to provide the levels of abstractions over time.

**2. Proposal: SV Abstractions**

**2.1 Background**

**2.1.1 What types of Queries are typically required during Maintenance and Debugging?**

[Pennington 1987a], [Pennington 1987b] outlined program summaries as a means for assessing program comprehension. These categorisation of statements have been expanded by [Good 1999a], [Good and Brna 2003]. The original categorisations from Pennington can be used as a starting point to investigate which queries are commonly used by software engineers.

*   _Function_, the overall goal of the program, e.g. "What is the purpose of the program ?", "What does the program do ?".
*   _Control Flow_, information on the temporal sequence of events occurring in the program, e.g. "What happens after X occurs ?", "What has occurred just before X ?".
*   _Data Flow_, transformation which data objects undergo during execution, including data dependencies and data structure, e.g. "Does variable X contribute to the final value of Y?".
*   _Operations_, information about specific actions which take place in the code, generally corresponds to a single line of code or less, e.g. "Does a variable become instantiated with a particular value ?".
*   _State_, time-slice descriptions of the state of objects and events in the program, e.g. "When the program is in state X, is event Y taking place, or has object Z been created/modified ?".

**2.1.2 Can Software Visualisation Help ?**

It is essential that the various comprehension strategies should be supported in a development tool. The following section highlights the calls made by researchers for support of these comprehension strategies.

[Storey et al 2000], states that a software maintenance tool needs to:

*   Support a combination of comprehension strategies
*   Provide a means to easily switch between strategies while solving a task
*   Reduce cognitive overhead as the program is explored

[von Mayrhauser and Vans 1993], also states that all comprehension strategies must be supported as well having the ability to switch between each of them.

[Mullholland 1997], found that the following should be supported:

*   mapping between Control Flow information in the SV and the code
*   mapping between Data Flow information in the SV and the code
*   gaining a clear temporal perspective of the execution within the SV
*   keeping track of Control Flow even during complex phases

This leads to support for SV abstractions, the following is a brief overview. SV abstractions define a number of levels or views of an executing software system. Pennington's work is used as a foundation to define the basic views such as, control flow, data flow, state. Other views are added to incorporate dynamic information such as the system in execution view.

All of these views are built upon the source code view, which is the lowest abstraction. The control flow view is the next and so on until the view furthest away from the source code is reached, which is the most abstract view called the software architecture view.

It should be noted that these views are just an outline and many more exist that have not been described. An empirical study will be performed in other to gather data on the most commonly used abstractions during maintenance, it is hoped that other views will be found and identified. The abstraction views/levels are not numbered as there are many gaps that need to be filled through empirical studies, as can be seen in Figure 1. A more detail description is provided in the next Section.

**2.2 Description**

{{< figure src="img/2003-aug-newsletter-abstractions.jpg" caption="Figure 1: SV abstractions" class="tc">}}

From Figure 1, a software system (source code files shown on the left) can be examined at many levels of abstraction. For instance, the highest abstraction is the software architecture overview, next is the system in execution in realtime, further down the abstractions is the data flow view and control flow views.

All of these views are hidden in the documentation and source code. In the case of source code, all this information is located within the same file(s), for example, control flow abstraction and data flow abstraction can only be separated in the mind of the software engineer after reading the source or by using tools, for example, such as aiCall [aiCall], to gather control flow information and a separate tool such as Jinsight [Jinsight] for the data flow. Even this poses problems, as both these tools support different languages!

Software Visualisation can be used to abstract away these layers of the system and present them to the user for further investigation. The Abstractions will be extracted from the source and the instrumented Java Virtual Machine (JVM) in order to present the views to the user.

In this way, both static and dynamic information can be integrated to provide a more complete picture. Since the views increase in their level of abstraction from the source code, switching between the comprehension strategies will be made possible. For example, top-down comprehenders have the option to explore the system from the software architecture view and bottom-up comprehenders have the option to explore the system from the source code and control flow views.

The question is, which abstraction or abstractions are best suited to aid the comprehension for the industrial software engineer? With this knowledge, SV tools can be developed or adapted to emphasise this abstraction and ensure it presents the information in the most appropriate form.

As the abstractions increase upwards, the distance from the source code is increased. For example, the control flow abstraction can contain parts of the source when presenting its information, whereas the software architecture abstraction is the most abstract containing no source code. Each abstraction must support user defined queries and allow interactive exploration of the system.

For the planned investigation, it is hypothesised that the levels nearest the source code will provide the most comprehension of the system. For example, if this is the case then it is worthwhile building a tool to allow chunking [Shneiderman and Mayer 1979] and annotations of the source code etc.

**2.3 Empirical**

**2.3.1 Measuring Comprehension**

The coding scheme from [Good 1999a] and [Good 1999b] will be used as a measure of comprehension. This measurement of comprehension was chosen due to its ability to measure levels of abstraction which is highly appropriate for this research. For example, Data Flow and Control Flow statements can be measured and compared, the same is true for other abstraction levels.

**2.4 Designing for the Software Engineer**

A preliminary investigation will be carried out in order to gather requirements for the tool. Program summaries, Video and sketches will be among the data gathered. Program summaries will be used as a measure of comprehension while the sketches are to aid in empirically establishing the abstraction levels.

The tool will then be implemented using the abstraction levels identified from the study along with support for switching between these. For example, if the study shows that there is a lot of switching from source code descriptions to control flow descriptions, then both these levels will be integrated to allow for such switching.

The implementation will consist of a monitoring framework for Java programs which has already been implemented using the JPDA [JPDA] as a means of keeping track of the executing system. Java was chosen due to the ability to monitor events in its virtual machine and due to its popularity in industry. This will be integrated into an open IDE such as Eclipse or Netbeans, where future abstractions can be added and tested as they are implemented.

Once the tool is complete, a post study will take place where the tool can be evaluated using professional software engineers. These results will verify if the tool produces any improvement in program comprehension in comparison to existing tools.

**3. Conclusion**

As discussed previously, the software visualisation field has a gap in the question of how to represent an executing system. The authors approach, abstractions, has been discussed and a number of these abstractions will be implemented and integrated into the NetBeans IDE.

The abstractions will allow the software engineer to examine slices of the system, for example, to examine the control flow or the data flow or both or any other combination of the abstractions.

Once the most commonly used abstractions have been established a large proportion of the research will involve establishing appropriate techniques for those abstractions, for example, while a SeeSoft-like view may be appropriate for the source code level, it is not entirely appropriate for the software architecture view.

The need for more empirical evidence was also discussed, especially in the area of dynamic software visualisation. A contribution will be made to this empirical body of research where the results will feed the requirements phase for the visualisations, then another study will be performed on professional software engineers in order to verify the effect of the visualisations.

Finally, your feedback and criticisms are very much welcomed, especially in identifying other commonly used abstractions that should be implemented, or your ideas on which techniques are suitable for a particular abstraction.

**Bibliography**

[aiCall] aiCall Software Visualisation Tool, Available, "http://www.absint.com/aicall/".

[DePauw et al 1998] DePauw, W., Lorenz, D., Vlissides, J., Wegman, M., "Execution Patterns in Object-Oriented Visualization", USENIX, 1998.

[Eclipse] Eclipse IDE, Available, "http://www.eclipse.org/".

[Gargiulo and Mancoridis 2001] Gargiulo J., and Mancoridis, S., "Gadget: A tool for Extracting the Dynamic Structure of Java Programs", SEKE, 2001.

[Good 1999a] Good, J., "Programming Paradigms, Information Types and Graphical Representations: Empirical Investigations of Novice Comprehension" Ph.D. Thesis, University of Edinburgh, 1999.

[Good 1999b] Good, J., "VPLs and Novice Program Comprehension: How do Different Languages Compare ?", IEEE Symposium on Visual Languages, Tokyo, Japan, September 13-16, 1999.

[Good and Brna 2003] Good, J., Brna, P., "Toward Authentic Measures of Program Comprehension", In Proceedings of Joint Conference of EASE & PPIG, Keele University, April 8-10th, 2003, pp. 29-49, 2003.

[Jinsight] Jinsight, IBM Research, Available: http://www.research.ibm.com/jinsight/.

[JPDA] Java Platform Debugger Architecture (JPDA), Available: "http://java.sun.com/products/jpda".

[Mullholland 1997] Mullholland, P., "Using A Fine-Grained Comparative Evaluation Technique to Understand and Design Software Visualization Tools", Empirical Studies of Programmers, Seventh Workshop, pp. 91-108, Ablex Publishing, 1997.

[Netbeans] Netbeans IDE, Available, "http://www.netbeans.org/".

[Pennington 1987a] Pennington, N., "Stimulus Structures and Mental Representations in Expert Comprehension of Computer Programs", Cognitive Psychology, Vol. 19, pp. 295-341, 1987.

[Pennington 1987b] Pennington, N., "Comprehension Strategies in Programming", Empirical Studies of Programmers: Second Workshop, pp. 100-113, 1987.

[Smith and Munro 2002] Smith, M. P., and Munro, M., "Runtime Visualisation of Object Oriented Software", 1st International Workshop on Visualizing Software for Understanding and Analysis, Paris, France, pp. 81-89, June 26, 2002.

[Storey et al 2000] Storey, M.-A. D., Wong, K., Muller, H. A., "How Do Program Understanding Tools Affect How Programmers Understand Programs ?", Science of Computer Programming Journal, Vol 36, Issues 2-3, pp. 183-207, 2000 (paper first appeared 1998).

[von Mayrhauser and Vans 1993] von Mayrhauser, A., and Vans, A., "From code understanding needs to reverse engineering tool capabilities", 6th International Conference on Computer-Aided Software Engineering (CASE), Singapore, July 19-23, 1993.

---

# Spotlight on PPIGers

*   [Enda Dunican]( {{< localref "#enda-dunican" >}} )
*   [Linda McIver]( {{< localref "#linda-mciver" >}} )
*   [Rebecca Smith]( {{< localref "#rebecca-smithe" >}} )
*   [Ray Waddington]( {{< localref "#ray-waddington" >}} )

**Would you like to tell other PPIGers how you are and what you are doing through the newsletter?** If so, please e-mail _chrisd(at)fdbk.co.uk_.

## Enda Dunican

We have a project starting in IT Carlow funded by the Higher Education Authority, the body in charge of all third-level education in Ireland.

The project is in the area of student retention. The funding provides a special office/lab with a number of PCs, and functions as a drop-in centre for students with problems in computer programming.

At this drop-in centre students can come to lecturers with programming problems. It occurs to me that this may be a very valuable resource in gathering details and categorising the main problems first year students have with computer programming.

If PPIG colleagues have an experience of dealing with students in this manner or if they have specialised in addressing novice programming problems they can contact me. Perhaps there may even be an opportunity for some collaboration with other educational institutes. I am open to suggestions.

Enda can be contacted by sending him a message using _dunicane(at)itcarlow.ie_

## Linda McIver

Linda McIver missed the PPIG workshop this year, but in a good cause! Zoe Dianne McIver was born on March 25th at 8:36am. She was 4.35kg (9lbs 9oz), and has been thriving ever since (sitting comfortably on the high side of the growth curve, just like her mum!).

She's a happy smiley baby, and she has Andrew and I under good control.

## Rebecca Smith

Dear All,

Anyone who has heard me asking about how to get money for my research will be pleased to hear that I have finally received some funding, in the form of a University of Glasgow faculty studentship. Here's a big thank you to Thomas Green who had some very useful suggestions for my application. And Thomas will be pleased to know that I have now read several of the papers he suggested I use as references!

Best wishes, Rebecca Smith.

## Ray Waddington

I finished my visiting professor post at the University of Guelph, Ontario, Canada in 1992. For 10 years I worked in the software industry as a consultant, doing everything from y2k, project management to programming.

I have recently gone back to the academic world, taking an adjunct faculty position at Strayer University, where I teach computer science courses.

Most recently I founded The Peoples of The World Foundation, where I am a photoethnographer. The Foundation's web site is at [Peoples of the World](http://www.peoplesoftheworld.org/)

I am sure some of your readers will remember me.

Regards, Ray Waddington.

---

# Musings from the Trenches

## The unbearable lightness of errors

By **Chris Douce**

Due to various policy decisions recently made by a major operating system vendor, a number of different integrated development environments (IDE's) were evaluated. These ranged ranged from those that were open source and freely available for use, through to very expensive (and supported) commercial equivalents.

One of the most striking differences between IDEs and their compilers was not the immediate differences in the screen layout - a change in design of a code explorer window - or the differences in the short-cut keys, but the differences in the compilation messages that were produced when code is compiled.

Leaving one IDE for another can be either a painful or enlightening experience. Not only do you loose the location of toolbar icons and menus learnt over several years, but also your ability to interpret the error messages that a new environment or compiler generates.

Rather than a producing a message stating, '_semicolon missing at line n_', compilers often generate scroll-boxes filled with messages that have little bearing on what amounts to a very minor syntactical lapse.

I remember, as a beginner, being absolutely terrified by the screen scrolling past, generating acres of pages in response to an incredibly trivial error. My mentor sitting behind me would chuckle, wander over to my PC, move the cursor to a line that was close to the first error message and add my omitted semicolon, much to my astonishment.

Bracketing and braces are also common causes of a catastrophic cacophony of errors. A message telling you of an unexpected closing brace, really means that you have forgotten to put down an opening brace somewhere. Miss off a parameter and you may be told that you have an 'unexpected ")"' Cognitive psychology texts tell us that negative information is more difficult to comprehend.

When often presented with hundreds of small, all intricately related error messages, I get a 'feeling' for the original error, based upon the form that the messages take.

Changing your IDE changes the way you respond to your own mistakes. Your 'error schemas' which fire when seeing the keywords similar to 'unbounded' or 'inheritance' may have to be reformed as you feel your way around your new IDE. At the same time you may even changing your model the language that you use.

Working with a compiler and responding to compilation messages can be viewed in terms of having a 'conversation' with a body of source code. On some occasions I have felt it helpful to deliberately introduce errors to observe the effects on some alien code.

I have renamed objects, classes and even files in moments of frustration to attempt to get snippets (or slices) of information about the inner workings of some undocumented software project undergoing maintenance.

When an IDE or compiler changes, so does its personality, so does a developers mode of communication with his or her unknown mass of symbols and instructions.

**Are you working in industry and would like to tell us about an issue that you feel particularly strongly about? Is there something that you feel that the academic computer science, software engineering or human-factors communities should be addressing? If so, please do tell us!**

---

# Links Beyond

There are a huge number of conferences, journals and workshops that may be of interest to PPIG members. Since so many are relevant it may be difficult to know where to start searching. This section presents a few links to some of the journals that I have found useful.

Contemplating the cognitive needs of a programmer led me directly to the following journal:

*   [Journal of Cognitive Psychology](http://www.elsevier.com/locate/issn/0010-0285)

This journal would prove to be rather fascinating. For a simple software engineer like myself who would become befuddled with reading articles about systems it would be refreshing to read about experiments performed on real people rather than machines:

*   [Journal of Experimental Psychology: Learning, Memory, and Cognition](http://www.apa.org/journals/xlm.html)

Human-Computer Interaction is a popular topic amongst PPIGers for a number of reasons. Software development environments can be used to construct easy-to-use software packages, which may possess their own issues of usability.

Programming language (and software library!) design is also an issue that can lie within the area of HCI:

*   [International Journal of Human-Computer Interaction](http://www.catchword.com/erlbaum/10447318/contp1-1.htm)

It would be impossible (and silly) to miss the famous (and nebulous) Communications of the ACM, a source of inspiration and information for a huge array of fields surrounding what may be termed 'computer science':

*   [Association of Computing Machinery](https://www.acm.org/)

For those who have an interest in how engineering approaches could potentially be used to understand more about the application, use and development of computer systems and software development, the below transactions will be very familiar:

*   [IEEE Transactions on Software Engineering](http://www.computer.org/tse/index.htm)

This journal appears to be obviously related to some of the Psychology of Programming topics, since a growing number of POP studies use existing systems and empirically analyse how programmers navigate, use and modify them.

In the journal below, the empirical studies may differ in methodology, but perhaps some of the observations and conclusions may be similar:

*   [Empirical Software Engineering](http://www.kluweronline.com/issn/1382-3256)

Here we have an interesting journal that brings disciplines together. In some cases software engineers and programmers are used to construct models to further understand what cognition is. There is more to Cognitive Science than initially meets the eye. If you are interested, please read on:

*   [Cognitive Science Journal](http://www.cognitivesciencesociety.org/about.html)

One enterprising soul has devised a 'top 10' of classic Cognitive Science papers. Some are especially interesting, since they relate to novice-expert differences and diagrammatic reasoning, a topic that is of interest to those working with modeling languages such as UML, and those using 'visual programming languages':

*   [Cognitive Science Journal Top 10](http://cognitrn.psych.indiana.edu/rgoldsto/cogsci/classics.html)

Other journal titles that may also of interest includes _Cognition_, _Brain and Cognition_ and Social Cognition.

Finally, spare a moment for those poor souls who have to straddle both the 'code face' and the 'chalk face'. Computer science education is an activity that has to be undertaken throughout the life of a professional programmer. Perhaps here we will find some insights into what our students need:

*   [Computer Science Education](http://www.szp.swets.nl/szp/journals/cs.htm)

Do you know of a journal that may be of interest to fellow PPIG members? If so, please tell us about it. Interested in writing a review, or perhaps you are an editor and would like to introduce your journal to us? Please feel free to send a message to chrisd(at)fdbk.co.uk

<table width="940px">
<tbody>
<tr>
<td width="640px">
<h2 id="it-s-doddery-fodder">It's Doddery Fodder...but is it Art?</h2>
<p>By <b>Frank Wales</b></p>
</td>
<td width="300px">
<h2 id="supplementary-notes">Supplementary Notes<a name="sdfootnote1anc" href="{{< localref "#sdfootnote1sym" >}}"><i>[1]</i></a></h2>
<p id="sdfootnote1" class="footnote">
<a class="sdfootnotesym" name="sdfootnote1sym" href="{{< localref "#sdfootnote1anc" >}}">[1]</a>
These are like the kitchen of the academic discourse party;
they're where all the interesting quips hang out.</p>
</td>
</tr>

<tr>
<td>
<p>For some years now, I have been haunted<a name="sdfootnote2anc" href="{{< localref "#sdfootnote2sym" >}}"><i>[2]</i></a>
by a question I was asked once by a fellow PPIGlet: "Have you
ever written a paper entitled '<i>Post-modernism explained by a
software engineer'</i>? Because I'd like to cite it if you have."<a name="sdfootnote3anc" href="{{< localref "#sdfootnote3sym" >}}"><i>[3]</i></a>
Since then, I've wondered what this paper might be about, and if I
ever wrote it, whether it would be any good.
</p>
<p>I was reminded of this pending omission from my future emissions by
these two essays which both compare programmers favourably with
artists. The first article actually has "psychology of
programming" in its title, so it must be right, while "<i>Hackers and Painters</i>" by Paul Graham
contributes to the debate on whether programming is art or
engineering firmly on the art side:</p>

<ul><li>
<a href="http://www.devx.com/devx/editorial/11659">
Understanding the
Psychology of Programming</a></li>
<li><a href="http://www.paulgraham.com/hp.html">
Hackers and Painters</a></li></ul>
</td>
<td>
<p id="sdfootnote2" class="footnote"><a class="sdfootnotesym" name="sdfootnote2sym" href="{{< localref "#sdfootnote2anc" >}}">[2]</a>
Well, not haunted exactly, since I don't believe in ghosts. Perhaps
	stalked. Or at least followed around from time to time and leered at
	in a funny way.</p>

<p id="sdfootnote3" class="footnote"><a class="sdfootnotesym" name="sdfootnote3sym" href="{{< localref "#sdfootnote3anc" >}}">[3]</a>
    To protect the identity of this person, who now seems to have forgotten
	asking such a question, I won't use his real name. Instead, I'll
	refer to him as "Allan Blackwell".</p>
</td>
</tr>


<tr>
<td>
<p>If I can ever find someone at least vaguely authoritative who can
explain <i>Post-modernism</i> to me without first apologising for why
their definition isn't a very good one, I might be able to make
progress in writing my paper. But funnily enough, as I study art
more<a name="sdfootnote4anc" href="{{< localref "#sdfootnote4sym" >}}"><i>[4]</i></a>,
I find "<i>vague authority</i>" seems to sum up much of
modern art pretty well anyway, so maybe I'm being just too
<i>enlightenment-oriented</i> when I expect a simple answer that I can understand.
</p>
</td>
<td>
<p id="sdfootnote4" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote4sym" href="{{< localref "#sdfootnote4anc" >}}">[4]</a> And
	yes, in my spare time I really am an arts student. "Know thine
	enemy", as someone once said.</p>
</td>
</tr>


<tr>
<td>
<p>After all, the history of art is a series of oscillations
between <i>simplification &amp; distillation</i> and <i>exploration &amp;
complexification</i>, with the Classical and Modernist eras examples
of the former, and the Baroque and Post-modern examples of the
latter. <a name="sdfootnote5anc" href="{{< localref "#sdfootnote5sym" >}}"><i>[5]</i></a></p>

</td>
<td>
<p id="sdfootnote5" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote5sym" href="{{< localref "#sdfootnote5anc" >}}">[5]</a> In
	physics, this important technique is called "proof by blatant
	assertion".</p>
</td>
</tr>


<tr>
<td>
<p>It is very tempting to try to fit the history of programming
into this model, with (say) structured programming and design
patterns analogous to Classicism and Modernism, and things like the
Web and Perl representing the Baroque and Post-modern<a name="sdfootnote6anc" href="{{< localref "#sdfootnote6sym" >}}"><i>[6]</i></a>.
</p>

<p>Maybe we could even pretend that <i>Sourceforge</i> represents the
world's largest collection of found art<a name="sdfootnote7anc" href="{{< localref "#sdfootnote7sym" >}}"><i>[7]</i></a>,
while <i>Google</i> is the world's biggest collection of repurposed
content<a name="sdfootnote8anc" href="{{< localref "#sdfootnote8sym" >}}"><i>[8]</i></a>.
And maybe this site, dedicated to discussing tiny pieces of free code,
will act as a microcosm of that pretense:</p>
<ul><li><a href="http://osnippets.org/index.php">Open Snippets ::
GPLed Source Snippets, Served Daily</a></li></ul>
</td>
<td>
<p id="sdfootnote6" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote6sym" href="{{< localref "#sdfootnote6anc" >}}">[6]</a> Hence
	the phrase "If it ain't Baroquen, don't fix it."</p>
<p id="sdfootnote7" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote7sym" href="{{< localref "#sdfootnote7anc" >}}">[7]</a> "Found
	art" appears to be a declaration by an artist that his
	immediate surroundings had more talent than he did.</p>
<p id="sdfootnote8" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote8sym" href="{{< localref "#sdfootnote8anc" >}}">[8]</a>"Re-purposed
	content"appears to be a declaration by a developer that her
	immediate predecessors had more talent than she did.</p>
</td>
</tr>

<tr>
<td>
<p>More interestingly, sites like this perhaps show the essential
Post-modernism of the whole free software movement, which avowedly
encourages copying, adaptation and recombination.</p>

<p>Speaking of recombination, this announcement from the Royal
College of Art mooting some biological software muckaboutery fits
right in:</p>

<ul><li><a href="http://www.rca.ac.uk/images/lib/107.pdf">Transplant Biopresence</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>Perhaps it's just me, but the idea of inserting the entire human
genome into that of a tree strikes me as both massively ill-conceived
and perhaps even ludicrously dangerous<a name="sdfootnote9anc" href="{{< localref "#sdfootnote9sym" >}}"><i>[9]</i></a>.
</p>
<p>Anyway, I'm thinking that I should just appropriate<a name="sdfootnote10anc" href="{{< localref "#sdfootnote10sym" >}}"><i>[10]</i></a>
Larry Wall's paper "<i>Perl: the first post-modern programming
language</i>" to get me started, and then toss in some verbiage
from the <i>Post-modernism generator</i> to lend gravitas, or
at least promote a sense of
intellectually-outclassed bewilderment in the reader<a name="sdfootnote11anc" href="{{< localref "#sdfootnote11sym" >}}"><i>[11]</i></a>:</p>
<ul><li><a href="http://www.wall.org/~larry/pm.html">Perl, the first
postmodern computer language</a></li>
<li><a href="http://www.elsewhere.org/cgi-bin/postmodern/">The
Postmodernism Generator: Communications From Elsewhere</a></li></ul>
</td>
<td>
<p id="sdfootnote9" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote9sym" href="{{< localref "#sdfootnote9anc" >}}">[9]</a>
        But then, perhaps I know just enough about genetics and software to
	imagine the failure scenarios, but not enough about conceptual art to see why
	this isn't just genetic engineering by cut-and-paste.
	</p>
<p id="sdfootnote10" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote10sym" href="{{< localref "#sdfootnote10anc" >}}">[10]</a>
    "Appropriation"
	is the art-world term for what most intellectual property lawyers
	would call "stealing". See:
	<a href="http://www.google.com/search?q=%22jeff%20koons%22%20%22string%20of%20puppies%22">these links</a>
</p><p id="sdfootnote11" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote11sym" href="{{< localref "#sdfootnote11anc" >}}">[11]</a>
        Cynicism like this is very Post-modern too, I'm told.</p>
</td>
</tr>

<tr>
<td>
<p>Many programmers seem attracted to perl by its maxim "<i>There's
more than one way to do it</i>", which is antipathetic to many
specialised languages, which might have the maxim "<i>There's
nearly one way to do it, but not quite.</i>". Perl,
along with other scripting languages, certainly polarises the
armchair software engineers who've wandered over from the web
development world:</p>
<ul><li><a href="http://www.onlamp.com/pub/a/onlamp/2003/05/12/languagephilosophy.html">ONLamp.com:
What I Hate About Your Programming Language</a></li>
<li><a href="http://ask.slashdot.org/article.pl?sid=03/02/24/1956237">Slashdot:
Do Scripters Suffer Discrimination?</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>Whether perl's imminent re-design will enhance the language or
dehance<a name="sdfootnote12anc" href="{{< localref "#sdfootnote12sym" >}}"><i>[12]</i></a>
it remains to be seen, but it'll clearly provide much fodder for
future arguments between aficionados of dense syntax and fans of
semantically significant quantities of white-space:</p>
<ul><li><a href="http://www.perl.com/pub/a/2003/06/25/perl6essentials.html">Perl
6 Design Philosophy</a></li></ul>
<p>One of perl's clear strong points is its lack of shame in stealing
(sorry, <i>appropriating</i>) ideas and ways of doing things from
other languages, and it's perhaps this that's led it to become an
important glue language, especially in these web-enabled times when
the hard problems seem to be festering in the cracks and crevices of
the virtual world.
</p>
</td>
<td>
<p id="sdfootnote12" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote12sym" href="{{< localref "#sdfootnote12anc" >}}">[12]</a>
    What
	do you mean, 'dehance' isn't a word? You understood it, right? Next,
	you'll be telling me that 'pessimal' isn't the opposite of
	'optimal'.</p>
</td>
</tr>
<tr>
<td>
<p>Which brings me back to XML again<a name="sdfootnote13anc" href="{{< localref "#sdfootnote13sym" >}}"><i>[13]</i></a>.</p>
<p>This presentation opines that XML is awful, but inevitable despite
its awfulness:</p>
<ul><li><a href="http://xmlsucks.org/but_you_have_to_use_it_anyway/does-xml-suck.pdf">Does
XML Suck?</a></li></ul>
</td>
<td>
<p id="sdfootnote13" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote13sym" href="{{< localref "#sdfootnote13anc" >}}">[13]</a>
    Which, due to a technical oversight, was completely missing from my
	previous column</p>
</td>
</tr>


<tr>
<td>
<p>And its author is not alone in finding fault with this programming
generation's most over-achieving technology:</p>
<ul><li><a href="http://xmlsucks.org/">XML Sucks</a></li>
<li><a href="http://c2.com/cgi/wiki?XmlSucks">Xml Sucks</a></li>
<li><a href="http://www.tbray.org/ongoing/When/200x/2003/03/16/XML-Prog">XML Is Too Hard For Programmers</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>But so far, I haven't found a document about XML that matches the
comprehensive pasting given to Unix (and its known associates) in <i>The Unix-Haters Handbook</i>,
now available in its entirety online<a name="sdfootnote14anc" href="{{< localref "#sdfootnote14sym" >}}"><i>[14]</i></a>:</p>
<p></p><ul><li><a href="http://research.microsoft.com/~daniel/unix-haters.html">"The
Unix-Haters Handbook" WWW Page</a></li></ul>
<p>But that's enough non sequiturs for today.</p>
</td>
<td>
<p id="sdfootnote14" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote14sym" href="{{< localref "#sdfootnote14anc" >}}">[14]</a>
    Apart from the <i>Unix barf bag</i>&nbsp;that came with the original book.</p>
</td>
</tr>

<tr>
<td>
<p>One of the reasons for disliking the "programming as art"
opinion is that it makes the interviewing process a lot harder. But
there are still some software domains where the environment applies
enough selection pressure to make questions with right answers
useful, such as embedded systems development:</p>
<ul><li><a href="http://www.embedded.com/2000/0005/0005feat2.htm">A
'C' Test: The 0x10 Best Questions for Would-be Embedded
Programmers</a></li></ul>
<p>To test those eager candidates who've memorised the <i>Frequently
Asked Questions</i> from comp.lang.c, here are the Infrequently Asked
Questions:</p>
<ul><li><a href="http://www.plethora.net/~seebs/faqs/c-iaq.html">Infrequently
Asked Questions in comp.lang.c</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>And if you find that your interview candidates have low SAT
scores, perhaps they're just showing off how much they <b>do</b> know by
deliberately answering everything wrong, like this guy did:</p>
<ul><li><a href="http://www.colinfahey.com/2003apr5_sat/2003apr5_sat.htm">Scholastic
Aptitude Test (SAT) : Answering All Questions Incorrectly!</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>Still, I know a few managers who much prefer to treat software
developers as interchangeable code-monkeys, so they might be dismayed
to find out that code monkeys aren't so interchangeable after all. At
least, if Primate Programming Inc is to be believed:</p>
<ul><li><a href="http://www.newtechusa.com/ppi/talent.asp">Primate
Programming(tm) Inc - Talent</a></li></ul>
<p>Now that people outside of software development are actually taking the
whole "software as art" thing more seriously, maybe this
shows that programming is sinking into the heads of enough
artists to start some genuinely new things:</p>
<ul><li><a href="http://m-cult.org/read_me/index.php">read_me
2.3</a></li>
<li><a href="http://runme.org/feature/read/+postmodgen/+57/">runme.org -
say it with software art!</a></li>
<li><a href="http://netartreview.net/">net_art_review</a></li></ul>
</td>
<td>
</td>
</tr>

<tr>
<td>
<p>Perhaps one way to resolve the art versus engineering dichotomy is
to consider it as false as the dichotomy between plumbing <a name="sdfootnote15anc" href="{{< localref "#sdfootnote15sym" >}}"><i>[15]</i></a>
and fashion <a name="sdfootnote16anc" href="{{< localref "#sdfootnote16sym" >}}"><i>[16]</i></a>,
and instead accept that there are different aspects to programming <a name="sdfootnote17anc" href="{{< localref "#sdfootnote17sym" >}}"><i>[17]</i></a>
that sometimes look arty, and sometimes engineeringy<a name="sdfootnote18anc" href="{{< localref "#sdfootnote18sym" >}}"><i>[18]</i></a>.
</p>
</td>
<td>
<p id="sdfootnote15" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote15sym" href="{{< localref "#sdfootnote15anc" >}}">[15]</a>
    Essential, hidden, stable.</p>
<p id="sdfootnote16" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote16sym" href="{{< localref "#sdfootnote16anc" >}}">[16]</a>
    Inessential,
	visible, transitory.</p>
<p id="sdfootnote17" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote17sym" href="{{< localref "#sdfootnote17anc" >}}">[17]</a>
        As opposed to aspect-oriented programming, which is now
	apparently patented, and therefore potentially a lot harder to use: <a href="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&amp;Sect2=HITOFF&amp;d=PALL&amp;p=1&amp;u=/netahtml/srchnum.htm&amp;r=1&amp;f=G&amp;l=50&amp;s1=6,467,086.WKU.&amp;OS=PN/6,467,086&amp;RS=PN/6,467,086">United States Patent: 6,467,086</a>
</p><p id="sdfootnote18" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote18sym" href="{{< localref "#sdfootnote18anc" >}}">[18]</a>
    You	want precision? Ask an engineer. You want vagueness? Ask an artist.
	You want both? Ask a programmer about deadlines.</p>
</td>
</tr>

<tr>
<td>
<p>While technologists can clearly learn many things from artists, there are at least
some fundamental things they still have to learn from us.  For example, that
the primary colours are <i>not</i> red, blue and yellow<a name="sdfootnote19anc" href="{{< localref "#sdfootnote19sym" >}}"><i>[19]</i></a>.
</p>
<ul><li><a href="http://www.sanford-artedventures.com/study/g_primary.html">Primary Colors</a></li></ul>
</td>
<td>
<p id="sdfootnote19" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote19sym" href="{{< localref "#sdfootnote19anc" >}}">[19]</a>
    For	those of you who think this is right, take a close look at the dyes
	in a full-colour CMYK print cartridge. And if you think 'cyan' and
	'magenta' are really just different shades of 'blue' and 'red', then
	you need more help than I can offer.</p>
</td>
</tr>

<tr>
<td>
<p>But with the Net now pretty well-established as the mediator of,
and the reason for, many of the most interesting developments in
programming, maybe I should be planning to write a paper about
"Post-modemism"<a name="sdfootnote20anc" href="{{< localref "#sdfootnote20sym" >}}"><i>[20]</i></a>
instead. After all, I just have to make this thrilling new concept
vague enough to be understood clearly by anyone, and my place in
History<a name="sdfootnote21anc" href="{{< localref "#sdfootnote21sym" >}}"><i>[21]</i></a>
will be assured.
</p>
</td>
<td>
<p id="sdfootnote20" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote20sym" href="{{< localref "#sdfootnote20anc" >}}">[20]</a>
	If you	think this says "Post-modernism", you need to look
	at it more closely.   I hereby declare this to be the world's first typogronym, which is a
	new word that, when printed with the right typeface, closely resembles another word. Maybe
	I should patent it.
</p><p id="sdfootnote21" class="footnote">
	<a class="sdfootnotesym" name="sdfootnote21sym" href="{{< localref "#sdfootnote21anc" >}}">[21]</a>
    Or at least my place in Geography.</p>
</td>
</tr>
</tbody></table>

**Frank Wales** \
frank(at)limov.com \
[www.limov.com/frank.lml](http://www.limov.com/frank.lml)



## Acknowledgements

Many thanks go to Frank Wales for the assistance he has given during the production of this newsletter.
