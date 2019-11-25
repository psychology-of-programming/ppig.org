---
title: "January 2002 Newsletter"
date: 2002-01-01
newsletter: "january-2002"
---

Editor: **Chris Douce**

# Contents

[Editorial]( {{< localref "#editorial" >}} )

**[Book Reviews]( {{< localref "#book-reviews" >}} )**
**Chris Douce** reviews *Refactoring: Improving the Design of Existing Code*.

**[Software Design - Cognitive Aspects]( {{< localref "#software-design-cognitive-aspects" >}} )** - **Françoise Détienne** introduces her new book.

**[Announcements]( {{< localref "#announcements" >}} )** - Find out more about the forthcoming PPIG'02 workshop including ESP and several other related workshops and conferences.

**[New Projects]( {{< localref "#new-projects" >}} )** *Hypothesis-Based Conceptual Mapping of Source Code*, **Nicolas Gold**.

**[Spotlight on PPIGers]( {{< localref "#spotlight-on-ppigers" >}} )** - Where you all are and what you are doing!

**[Doddery Fodder]( {{< localref "#doddery-fodder" >}} )** *A light-hearted selection of programming related web sites* by **Frank Wales**.

---

# Editorial

Welcome to the first PPIG newsletter of 2002. This newsletter contains preliminary details of the forthcoming PPIG workshop, as well as details about the new ESP (Empirical Studies of Programmers) symposium, which I know has been missed by many members of the PPIG community.

Remember, we all like to hear about what you have been doing, what you have been reading, and also what you have been publishing - whether it is a paper, book or a program that we can all have fun playing with. The PPIG newsletter is what you make it, so please feel free to submit articles and ideas for inclusion at any time.

Also, if you visit any of the workshops or conferences that you think may interest the PPIG community, please tell us all about it by sending a report to the conference newsletter telling us about what you thought was the best part.

I hope you enjoy what is my second newsletter. If you have any criticisms, please do tell. I'll love to hear from you.

Looking forward to meeting you all at the next workshop!

**Chris Douce** \
_Chrisd@fdbk.co.uk_

# Book Reviews

By **Chris Douce**

### Refactoring: Improving the Design of Existing Code

In my brief Java career it has happened to me twice. I have found myself faced with the weirdest, most incomprehensible object-oriented source code imaginable. When faced with beasts of such complexity, I have wondered whether there would ever be a sub-discipline called the pathology of programming.

It is quite interesting to view weird code, where the abstractions have grown organically into large classes and coupling between parts of a system have imploded into a web of dependencies. However, having to understand them and ultimately make them function as specified is another matter!

Making loosely-coupled object-oriented code which contains loosely commented and apparently randomly named interfaces and classes is a challenge and the Refactoring book, appearing in the middle of my second bout of Java torture appeared to tell me what I could begin to do to make my horrid software begin to function.

Refactoring is defined as 'a change made to the internal structure of a software system to make it easier to understand and cheaper to modify without changing its observable behaviour'. Using this definition, refactoring could be interpreted to be, in its most simplest form a change to a group of identifiers to make code easier to read. In essence, this is what refactoring is.

Refactoring is not a design methodology, but a redesign methodology which could be described as 'step-wise re-engineering'. The authors emphasise that to make a software system _better_, small changes should be made. By carrying out a potentially large number of small refactorings the developer can begin to uncover a design that can be not only comprehensible but also reusable and maintainable.

A list of refactorings can be found within the front cover. Some of the refactorings that are described _feel_ like common sense. One of my favourite refactorings is 'introduce parameter object'. For example, if you have a function that requires a large number of parameters used to provide resources that the function requires, these could be bunched together in a single object.

Using an object, this group of parameters can be labelled, and so form a simple and easy to comprehend abstraction, removing jarring commas on a parameter list that may detract from simple comprehension.

Other refactorings that are of interest include, 'collapse hierarchy', 'extract interface' and 'move method' and many others that aim to strengthen boundaries between classes and clarify design.

I suspect that there are many programmers who have discovered and applied refactorings to their own software independently of those proposed by Fowler et. al. Refactoring is, I believe an elegant and powerful idea that I personally have embraced as (currently) a professional programmer.

One of the key contributions I feel is the naming of small groups of software maintenance operations that can be applied. In this way, refactoring has some similarity with Design Patterns, which the authors reference. Like design patterns, the refactoring operations represent a description of a shared abstract concept, potentially increasing the vocabulary of software developers and helping them to communicate not only about the software, but how the software may be used in the future.

Refactoring is not something that is done to a software system once, but continually. As systems evolve and new requirements are introduced, the source code is adapted and class hierarchies changed.

Interestingly, there is little attention focussed towards the topic of documentation. While refactoring occurs, it is likely that the only documentation is the source code itself and, of course, a programmer's paper scribbles used to take load off working memory. During refactoring, comments can become obsolete as fast as member functions as classes are repositioned and renamed. However, this may potentially increase the worth of reverse engineering tools and design recovery tools.

Like so many issues in software development, the use of refactoring may depend upon the domain in which it is applied. I doubt that it will be used by those who have to work with hardware or safety critical systems, where designs are likely to be developed in a systematic and organised way. It is more likely to be applied in cases where the functioning software is rather old and has been 'inherited' by a number of different programmers, each potentially partially comprehending a system.

Also, it would be interesting to study how such a technique would affect programmers working in pairs or groups in comparison to programmers who have had no exposure to the terms and heuristics described within Refactoring.

***Refactoring: Improving the Design of Existing Code*** \
by **Martin Fowler**, **Kent Beck**, **John Brant**, **William Opdyke** and **Don Roberts** \
Addison-Wesley Object Technology Series, 1999 \
ISBN 0-201-48567-2

<br>

**Have you read a book that may be of interest to the PPIG community?** \
**Or maybe you have stumbled across a new journal that may interest us all?** If so, send all your reviews to *chrisd@fdbk.co.uk*.

# Software Design - Cognitive Aspects

By **Françoise Détienne**

Françoise Détienne introduces her new book, <cite>Software Design - Cognitive Aspects</cite>, published by Springer under the Practitioner Series. You can contact Françoise by e-mailing her at: _Francoise.Detienne@inria.fr_

The aim of this book is to present a critical synthesis of research in the field commonly known as the psychology of programming. This covers the activities involved in the different programming tasks, such as analysis, design, coding and maintenance.

### Themes

The book is centred around three themes: the design of software, the reuse of software, and the understanding of completed software for the purposes of modification, debugging, or reuse. More peripherally, we shall address program documentation. We shall call on the theoretical frameworks developed in cognitive psychology for the study of problem solving, reasoning by analogy, and the production and understanding of text.

### Structure of the book

Chapter 1 presents a history of research carried out in the psychology of programming from the mid-70s onwards.

We distinguish two periods. The first is characterised by the use of experimental paradigms and by the absence of a theoretical framework. The second sees the emergence of new experimental paradigms and borrows its theoretical frameworks freely from cognitive psychology.

In chapter 2, we investigate the nature of a computer program, on the one hand from a computational point of view and, on the other hand, from a psychological point of view.

Right through the book we shall be drawing a parallel between studies of the processing (production and understanding) of natural language text and the processing of program text.

In this context we shall be looking at two questions: what are the similarities and differences between a computer program and a natural language text and what are the similarities and differences between programming languages and natural language?

The rest of the book treats two different aspects of programming: the production of programs (chapters 3, 4 and 5) and the understanding of programs (chapters 6 and 7).

As far as programming is concerned, we present theoretical approaches to program design in chapter 3, and to reuse in design in chapter 4\. These theoretical approaches will be evaluated on the basis of the results of empirical studies.

The practical implications of this research will be discussed as well as the prospects for further research. More particularly, in chapter 5 we shall be interested in the effect of one programming paradigm, namely object orientation, on program production activities.

As far as understanding is concerned, in chapter 6 we present the theoretical approaches to understanding programs. Again we shall evaluate them on the basis of empirical results and discuss the practical implications and the prospects for future research. The effect that the task and the textual structure have on understanding will be developed in chapter 7.

In chapter 8, we sum up the contribution of the research in cognitive psychology and then discuss the conditions necessary if the ergonomic implications of the material presented here are really to be taken into account in the field of computing.

### Who is this book for?

This book is aimed at practitioners, research workers and students in a range of disciplines: computing, especially software engineering, cognitive psychology, and cognitive ergonomics.

#### Computing Specialists

Computing is both the subject of the research described here and an application area for its results. The results presented thus have an impact on the ergonomic specifications of programming tools, with the goal of improving the compatibility between the tools and their users, the programmers.

By tools here, we mean not only programming languages and programming environments but also the programming models developed in software engineering such as process models and structured methods. Throughout the book we shall emphasise the ergonomic implications of the theoretical approaches presented.

We are hoping to sensitise computer specialists to the psychology of programming and, more generally, to cognitive ergonomics. We have written this book in an attempt to transfer ideas from these fields into the computing community.

#### Cognitive Psychologists and Ergonomists

The work presented is strongly orientated towards cognitive ergonomics. This orientation is explained by the fact that the activities studied are situational, that is, they form part of a task.

There are many theoretical borrowings from cognitive psychology. Our interest is to test and extend the models coming out of psychology by applying them to situations that involve a number of activities related to realistic and professional tasks.

The models borrowed have come out of research into problem solving and into the production and understanding of text. Now, in the programming situation, these activities are determined by the task and the experience of the subjects is an important factor in the situation. Further, the complexity of the situations studied is often greater than that of properly experimental studies.

Part of the interest of this work, for the psychologist and the ergonomist, is to analyse how these models can be applied to such complex situations, to discuss their limitations and to open up new paths for research.

***Software Design - Cognitive Aspects*** \
by **Françoise Détienne** \
translated by Frank Bott \
Springer: Practitioner Series, 2002 \
ISBN: 1-85233-253-0

**Françoise Détienne** \
*Francoise.Detienne@inria.fr*

# Announcements

### PPIG'02

The next PPIG workshop will be held between Tuesday 18 June and Friday 21 June 2002 where it will be kindly hosted by [Brunel University](http://www.brunel.ac.uk/), London, UK. Important dates for the PPIG workshop are given below:

|||
|---: |--- |
|**15 March 2002**|Paper submissions|
|**3 May 2002**|Notification of acceptance|
|**17 May 2002**|Authors submit final version of accepted papers.|
|**31 May 2002**|Conference registrations and payments|
|**18-21 June 2002**|PPIG'02|


More information will be available through the PPIG web site in due course. Keep watching the mailing list for announcements! For further information, please contact Dr Jasna Kuljis at _Jasna.Kuljis@brunel.ac.uk_.

### ESP (Empirical Studies of Programmers)

The famed and missed ESP (Empirical Studies of Programmers) series returns as a symposium within HCC'02 (Human Centric Computing Languages and Environments) chaired by [Susan Weidenbeck](http://www.cis.drexel.edu/faculty/wiedenbeck/~swiedenbeck.htm) and [Marian Petre](http://computing.open.ac.uk/Staff/index.cfm?StaffID=%28%23L7%2A%24X%5CMY%2D%2B%24%0A).

The **deadline** of the submission of papers is **3 March 2002**, and authors are notified on 19 May 2002\. Further submission information can be found at the HCC web page.

ESP topics include but are not limited to:

*   Design, comprehension, debugging, and modification of programs.
*   Teaching, learning, and knowledge transfer in various programming languages and paradigms.
*   Study and comparison of tools and programming environments.
*   Empirical studies of end-user programming, programming by example and related issues.
*   Studies of programming in different environments, such as at home or while travelling.
*   Novice/expert differences in programming.
*   Studies of programming by specific populations, such as children and older adults.

More information about ESP can be found by visiting [its website](http://www2.cs.fau.de/HCC02/esp.html).

Similarly, more information can be found about HCC'02 by visiting [its page](http://www2.cs.fau.de/HCC02/cfp.html).

Other Symposia being held at HCC'02 include:

*   **Visual/Multimedia Programming and Software Engineering**
    ([VMPSE website](http://www2.cs.fau.de/HCC02/vmpse.html))
*   **End-User and Domain-Specific Programming**
    ([EUP website](http://www2.cs.fau.de/HCC02/eup.html))

### International Workshop on Program Comprehension

The 10<sup>th</sup> International Workshop on Program Comprehension will be held between **26-29 June** in La Sorbonne, **Paris**. This workshop will gather practitioners and researchers from academia, industry, and government, to review the current state of the practice, to report on program understanding experiments, and to present issues and solutions in the general area of program comprehension.

The workshop web site can be found by visiting: [www.ai.univ-paris8.fr/iwpc02](http://www.ai.univ-paris8.fr/iwpc02)

The program co-chairs are:

*   **Ettore Merlo**, École Polytechnique de Montreal (Canada) _ettore.merlo@polymtl.ca_
*   **Mark Harman**, Brunel University (UK) _mark.harman@brunel.ac.uk_

Two keynote speakers will give IWPC'02 attendees the opportunity to hear from exciting areas related to Program Comprehension:

*   **Mary Jean Harrold**, Georgia Institute of Technology, Atlanta (GA) will present her work on Visualizing Test Cases for Comprehension
*   **Jean-François Perrot**, Laboratoire d'Informatique de l'université Paris 6, Paris (France) will present his work on Reflexion and Meta-Programming

IWPC 2002 will have a co-located event, the workshop on **Visualising Software for Understanding and Analysis** which will be held on held on **26 June**. More information about VISSOFT can be find by visiting: [www.dur.ac.uk/vissoft.2002/](http://www.dur.ac.uk/vissoft.2002/).

### Second Program Visualization Workshop

The Second Program Visualization Workshop is held in cooperation with [ACM SIGCSE](http://www.acm.org/sigcse/) and will taken place at HornstrupCentret, **Denmark**, on **27-28 June 2002**, immediately following the ITiCSE 2000 conference in Aarhus, Denmark

Further information can be obtained by visiting [the workshop website](http://stwww.weizmann.ac.il/g-cs/benari/pvw).

Participation in the workshop is contingent upon acceptance of a paper relating to the topics of interest. The paper may be a short position paper, an extended abstract describing work in progress or a full paper.

Topics of interest include: software for visualizing algorithms and programs, visualizations of computer systems, visual debuggers and empirical evaluations of visualizations.

You are also welcome to e-mail Moti Ben-Ari, the chair of the Workshop and PPIG member at _moti.ben-ari@weizmann.ac.il_.

### ACM International Conference on Functional Programming (ICFP 2002)

**Margaret Burnett writes**: I have been appointed to the Program Committee for the ACM International Conference on Functional Programming (ICFP 2002). This year's committee is trying really hard to get some high quality papers about human aspects of programming languages, or at least functional and other declarative programming languages.

If you are working on human aspects of programming that are relevant to functional/declarative languages, this conference would really welcome your submission! And I'll be on the committee to make sure your paper gets a fair chance.

The conference will be held in Pittsburgh in October . The **deadline** for papers is **21 March 2002**. For more information see: [icfp2002.cs.brown.edu/](http://icfp2002.cs.brown.edu/)

**Margaret Burnett** \
_burnett@cs.orst.edu_

# New Projects

### Hypothesis-Based Conceptual Mapping of Source Code

[Nicolas Gold](http://www.co.umist.ac.uk/~ngold) introduces an EPSRC funded project entitled **Hypothesis-Based Conceptual Mapping of Source Code**.

Program comprehension is the acquisition of knowledge about programs and a key issue is to understand the link between business concepts and their implementation in source code. Concept recovery is the re-establishment of links between source code and business concepts. This is necessary since initial design knowledge is typically lost during the evolution of software systems.

Hypothesis-Based Concept Assignment (HB-CA) is a successful knowledge-based technique for assigning concepts (actions/objects of interest to the maintainer) to regions of source code that implement those concepts. It undertakes its analysis using informal indicators such as variable names, procedure names and comments.

The process begins by creating a conceptual map of the program being analysed, generating hypotheses for concepts whenever the appropriate indicators are found in code (the matching can be flexible using sub-strings and synonyms).

The resulting list is divided into segments, initially using subroutine boundaries. A particular feature of the method is its use of a self-organising map (an unsupervised neural network) to undertake segmentation flexibly using the conceptual structure of the code in programs with large subroutines or no subroutine structure at all.

HB-CA has been evaluated on real-world COBOL II code from a system provided by a financial services organisation. It shows high recognition accuracy and the flexible segmentation approach works well in most cases.

The approach becomes more difficult to apply as the code evolves.

The aim of this new project is to understand the relationship between software evolution, the degradation of indicators and their structures, and the effectiveness of the concept recovery technique so that the limits of the method can be established and where appropriate extended to maintain concept recovery performance on heavily maintained code.

This will be achieved through empirical study of the method's performance on multiple versions of programs and it is hypothesised that improvements can be made by increasing the richness of the conceptual map produced by the Hypothesis-Based Concept Assignment technique.

The project is funded by EPSRC, will last three years and includes a Ph.D. studentship.

Nicolas Gold is currently a Lecturer in the Department of Computation. He can be contacted at _N.E.Gold@co.umist.ac.uk_ and more details of his work can be found at [www.co.umist.ac.uk/~ngold](http://www.co.umist.ac.uk/~ngold).

# Spotlight on PPIGers

### John Pane

I will be finishing my Ph.D. this spring. In my thesis research, I built a new programming system for children using a design process that emphasized usability. I began by thoroughly cataloguing the prior research on beginner programmers, and then conducted several new user studies to examine unanswered questions. This information was the basis for designing the new system, and the result differs substantially from current popular programming languages. In a user study with fifth- grade children, I demonstrated that several features of my system have a significant positive impact on usability.

More information about John's work can be found by visiting his [web site](http://www.cs.cmu.edu/~pane/research).

<br>

**Would you like to tell other PPIGers how you are and what you are doing through the newsletter?** If so, please e-mail _chrisd@fdbk.co.uk_.

# Doddery Fodder

By **Frank Wales**

### Web sightings to confuse and amuse, loosely assembled

One of the easiest ways to convince people that your language has something going for it is to have some sexy example programs to show it off, preferably solving well- known or stereotypical problems. Or, failing that, printing 'Hello world'. Many of the latter programs exist in this ever-growing collection of hundreds of examples in over a hundred different programming languages (which might also be handy for tutorials): [www.uni-karlsruhe.de/~uu9r/lang/html/lang.en.html](http://www.uni-karlsruhe.de/~uu9r/lang/html/lang.en.html)

Those who've spent any time working with professional programmers will appreciate that it's not the choice of programming language that determine the success or failure of a project, as much as the quality and behaviour of the people. Here's a draft paper, posted for comments, that attempts to bring one practitioner's views on the topic to the fore: [members.aol.com/humansandt/papers/nonlinear/nonlinear.htm](http://members.aol.com/humansandt/papers/nonlinear/nonlinear.htm)

I do find it interesting that while this quotes Gerald Weinberg, there appears to be no recognition of the work of current members of PPIG. Perhaps you could help the author out here, if you think this is an omission.

One other thing not included is this paper is the job-security gambit practised by some developers, where they deliberately build obscure systems in order to be seen as indispensable to the project. For many great tips on how to do this, see this guide on writing unmaintainable code: [mindprod.com/unmain.html](http://mindprod.com/unmain.html)

And lest the cynic in you think that all programmers really think this way anyway, here's at least one programmer's attempt to make people write better-quality C, which the world is definitely in need of: [www.lysator.liu.se/c/ten-commandments.html](http://www.lysator.liu.se/c/ten-commandments.html)

Finally, if you're looking for something to print out for reading in the bath (what, you mean I'm the only person who does that?), here's a long, interesting essay on the changing face of large-scale software development: [www.dreamsongs.com/MobSoftware.html](http://www.dreamsongs.com/MobSoftware.html)

If the future really is software development by mob, then our group may some day be subsumed into some future Sociology of Programming Interest Group. When that happens, they'll have to come up with a better web address than spig.org, since that's gone already. Suggestions on this, and other sites that might be of interest, are welcome.

Please feel free to e-mail Frank the ten commandments of Basic at his e-mail address : _frank@limov.com_
