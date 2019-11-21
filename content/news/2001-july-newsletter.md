---
title: "Newsletter: July 2001"
date: "2001-07-01"
---

Editor: **Chris Douce**

# Contents

[Editorial]( {{< localref "#editorial" >}} )

[Book Reviews]( {{< localref "#book-reviews" >}} ), **Chris Douce**
*Rebel Code: Linux and the Open Source Revolution*

[Musings from the Trenches]( {{< localref "#musings-from-the-trenches" >}} ), **Fabrice Retkowsky**

[Paper]( {{< localref "#paper" >}} ):
*A proposal for yet another dimension - the case for Tunability*, **Chris Roast**

[Conference Reports]( {{< localref "#conference-reports" >}} ): IWPC 2001, **Michael O'Brien**

[New Projects]( {{< localref "#new-projects" >}} ): A new crusade for comprehension, **Pablo Romero**

[Announcements]( {{< localref "#announcements" >}} ):
[INSERC 2001]( {{< localref "#inserc" >}} ),
[eLearn Magazine]( {{< localref "#elearn-magazine" >}} )
and spotlight on PPIGers:
[David Gilmore]( {{< localref "#david-gilmore" >}} ),
[Alan Blackwell]( {{< localref "#alan-blackwell" >}} ) and
[Terry Eden]( {{< localref "#terry-eden" >}} )

---

# Editorial
by **Chris Douce**

Welcome to the Summer 2001 PPIG newsletter. This new issue presents a new column entitled [Musings from the Trenches]( {{< localref "#musings-from-the-trenches" >}} ), meanderings through the never-ending torturous avenues of software development, this month given by PPIGer Fabrice Retkowsky following his entry to the cut and thrust, ever-changing world of e-business. If you know of any pitfalls or pearls (or perls?) of wisdom that we should all heed, please tell all.

Also included within this issue is a new interdisciplinary [book review]( {{< localref "#book-reviews" >}} ) section. This section is not limited to newly published texts, but also extended to our old favorites. Being such an eclectic bunch, contributions from the whole academic spectrum is encouraged.

The PPIG newsletter is what you make it, so please feel free to submit articles and ideas for inclusion at any time. Other possibilities for future issues include compressed bibliographies or subject area summaries aimed towards busy researchers and industrialists. We are also particularly interested in conference reports and announcements, abstracts of recently published PPIG papers and developments within industry that may be of interest to the PPIG community, whether it being a new language, human-computer interaction evaluation approach or that new fantastic silver-bullet wielding software tool! Do tell us all!

**Chris Douce** \
*Chrisd@fdbk.co.uk*

---

# Book Reviews
by **Chris Douce**

## Rebel Code: Linux and the Open Source Revolution

Glyn Moody's book presents an enthusiastic history of the Linux operating system and how it gradually arose to attempt to challenge the dominance of Microsoft. Moody describes the Open Source 'movement', where software development takes place by many for the common good of providing software that is useful, reliable and free, alongside many of the fascinating key players.

Having been an infrequent user of Emacs for a number of years, the name Stallman was anonymous amongst my gradually incrementing collection of photocopied instruction manuals. While trying to find a way to copy and paste text, I stumbled upon the GNU public license nestling between the cover and the table of contents. At the time, I considered the license to be a curiosity miles away from the other more familiar licenses that state 'this software may not do anything that it supposed to do', and 'you must not reverse engineer under any circumstances'. Moody paints a describes how the GNU licensing model has been central to open-source development.

Rebel Code provoked me to consider whether I should propose the opening-up of source code to my employer. Paradoxically, there was much discussion as to how open source software could assist an organisations competitive advantage. I concluded that in cases where the organisations are large and the competition is fierce, the opening-up of source code could potentially give an advantage, providing that communities of fluent and able developers are available. I have yet to be convinced of the case where the domain is very specialised, where there are only a limited number of users and software is developed for a very small number of providers. I will have to read the book again to appreciate all the arguments fully!

One of the fascinating issues that Moody touches upon is how the choice of early hardware technologies, often motivated out of pure curiosity, and sometimes due to a lack of available finances, can substantially influence and possibly direct our future careers. While it must be true that we are defined by our culture, it may be also true that we may also be defined by our early choice of computing devices or microprocessor.

Rebel Code is considered to be an important addition to the genre of writing that will undoubtedly become termed 'pop-computing' which will encompass books like Fire in the Valley and a Brief History of the Future.

Chris Douce works in a small company that uses a mixture of open source and proprietary software to design educational systems for colleges.

<br>

***Rebel Code: Linux and the Open Source Revolution*** \
by **Glyn Moody**   January 2001   ISBN: 0738203335

---

**Have you read a book that may be of interest to the PPIG community?**
**Or maybe you have stumbled across a new journal that may interest us all?** If so, send all your reviews to *chrisd@fdbk.co.uk*.

---

# Musings from the Trenches
by **Fabrice Retkowsky**

Tales of the gap between research and industry abound. Having jumped this gap by completing a PhD within the PPIG area and then joining a web service company, I take this new column as a chance to put together some thoughts on the issue.

While researching on the "Psychology of Java Software Reuse" at [Sussex University](http://www.cogs.susx.ac.uk/), it became quite common to hear or read researchers (both inside and outside of PPIG) complain of the lack of communication with the industry. Now that I work for [Runtime Collective](http://www.runtime-collective.com/), where we create web sites such as [www.infoconomy.com](http://www.infoconomy.com), I realise how this communication could happen if only both sides were interested in the same issues.

What challenges a company such as Runtime is diversity: diversity of skills, people and technologies brings innovation, synergy and motivation, but also raises problems:

## 1. Diversity of programmers

Programmers have various skills: some will be good at understanding code, others at quickly fixing bugs, they may have more experience with such or such language. But more than that, they may have programming styles: coders fancy getting their hands dirty and can browse and hack through huge programs easily, while developers will design and plan things carefully but program slowly, and enhancers will modify, correct, fix, improve the usability of a system, etc. Why is that so, can people change their style, how can different profiles work together?

For example, how can a "prototyper" (who likes the instant gratification of methodologies which let him get a basic system working quickly) work with a "planner" (who prefers careful preparing, designing, building and testing)?

And why are there such differences between programmers? Is it only a matter of experience, but then, what is really experience? Estimates of experience in the literature are plenty: number of years of programming, number of years of professional work, number of languages learnt, ... have all been used by experimenters to infer the elusive "experience" quantity. But what use is this quantity, when all that matters for a company like ours, is efficiency: how much time a programmer will need to implement such or such functionality, when will the new system be delivered, etc.

## 2. Diversity of "kinds" of programming

Most of the literature identifies and studies usual programming tasks such as understanding, designing, coding, and debugging. Yet all of these will be strongly influenced by the "kind" of programming used. Here at Runtime, within one same day a programmer can template some ADP web pages, then do some core implementation in Java, then configure a new system by editing some Tcl scripts, and finally draw out some OO relationship designs. These kinds of programming (templating, scripting, system design, coding) are very distinct in nature.

Obviously, programmers gain efficiency in each of these with practice, but some of them also seem to be naturally more skilled for one than for the others. This suggests that these programming kinds don't require the same skills, hence the same "thinking" (mental processes), and therefore that they cannot be represented by a unique model of programming.

Shouldn't there be a set of fundamentally different theories and models for each kind of programming, rather than one unique model of programming? Understandably most research has focused on proper analyse-design-code-test development, but at Runtime (and similar companies) most of the "programming" time is spent doing things like creating and modifying templates, installing new systems and reconfiguring them, maintaining and querying a web site's database, all of which hardly fall into the analyse-design-code-test category.

## 3. Diversity of working styles

Programmers have varying skills and behaviors. Furthermore, they don't work on their own. Programming takes place in project teams (small teams in Runtime's case, between 2 to 6 members). Team members don't just interact socially: they actually work together, and influences each other's programming. They share their knowledge, their understanding, their tasks, their expectations, and more than once clash on their opinions. Moreover, with programming techniques such as XP (extreme programming, see www.extremeprogramming.org), they code, debug, understand in pairs. This is a far cry from most empirical research where single programmers are asked to write a small piece of code on their own. How do all the interactions which occur during "programming" impact on it? How does it impact on separate tasks: design of OO models, querying of a database, templating of a new web page? How do programmers with different interaction styles (e.g. social versus independent) can cooperate?

More generally, and this is possibly getting outside of the boundaries of PPIG, Runtime staff diverge on the amount of structure they apply to their work: some display disciplined, ordered, formal work habits while others prefer less structured styles. The solution is obviously not to force everybody into the same mould: efficient staff is of utmost value - who cares about their idiosyncratic behavior as long as they are 5 or 10 times more efficient than others. But what can be done to reconcile each individual's preferred way of working in order to maximise the overall team efficiency? How can the sharing of information be maintained or optimised, and can various profiles work together, can rules be applied to non-structured styles, is it really worthwhile?

As I found out when writing my thesis on reuse, asking questions is easy - if only you can ask the right question. Reuse is, as much as I had expected, an important issue for the IT industry: if you can develop and deliver more quickly better software, then you can increase your margins, reduce your prices, etc. It also helps you, with time, build better systems which have the pooled functionality of individual projects. And the sine qua non to achieve this (far from purely cognitive issues such as program understanding, programmer's memory overloading, and so on) is to maintain compatibility between systems: if two systems are built on the same toolkit, but cannot co-exist on the same server, how can they be merged or at least work together? How can two distinct systems communicate together if they don't use similar interfaces? How will they communicate and work with external systems? A solution is to adopt a stable, open, standard development platform, and to adhere to standards such as XML, SOAP. Writing to a standard is an increasingly important part of the web industry - but I cannot remember any literature covering this.

Finally, I mentioned some of the languages we have to deal with: ADP, ASP, JSP for web page templating, Java and Tcl for core programming, Tcl again and Perl for scripting, SQL for data-model creation and database queries. We definitely don't use languages such as Prolog, Pop-11 or Fortran. It would be interesting to see research focus on the languages which we are actually using.

I hope these many questions will grab your attention and maybe kick-start some discussions on the PPIG mailing-list, in any case do not hesitate to email me directly!

**Fabrice Retkowsky** \
*fabrice@runtime-collective.com* \
[www.runtime-collective.com](http://www.runtime-collective.com)

---

# Paper
## A proposal for yet another dimension - the case for Tunability
**Chris Roast** \
Sheffield Hallam University Sheffield \
*c.r.roast@shu.ac.uk* \
http://www.shu.ac.uk/schools/cms/teaching/crr/

### Introduction
Cognitive dimensions provide a range of concepts that have been used to assess and compare a variety of information artifacts. The cognitive dimensions are intended to provide a "language" capable of capturing features of human system interaction that are both common to a variety of systems and highly relevant to the effective use of systems. In this short paper we propose that the notion of "tunability" should serve as another dimension not evident in the established set.

[read the full paper...](archives/news/2001-july-newsletter-paper/)

---

# New Projects

## CRUSADE

[Ben du Boulay](http://www.cogs.susx.ac.uk/users/bend/cv/frameshomepage.html), [Richard Cox](http://www.cogs.susx.ac.uk/users/richc/), [Rudi Lutz](http://www.cogs.susx.ac.uk/users/rudil/) and [Pablo Romero](http://www.cogs.susx.ac.uk/users/juanr/) recently started working in an EPSRC-funded project entitled CRUSADE (**C**oordination of multiple external **R**epresentations in program **U**nder**S**t**A**nding and **DE**bugging).

This project will study novice programmers of Java when using software visualisation representations for program comprehension tasks. We are interested in how the co-ordination of these external representations influences 1) the form of their mental representations and 2) their comprehension strategies.

The aims of this project are:

▻ to investigate the role that perspective, modality and individual differences such as cognitive style play in the co-ordination of multiple external representations in novice program comprehension.

▻ to develop a set of design principles for program comprehension aids, and particularly for software visualisation packages for Java.

▻ to develop a computerised experimental tool that will include a prototype visualisation environment for Java suitable for learners.

More information [about this project](http://www.cogs.susx.ac.uk/projects/crusade/) is available.

---

# Conference Reports

## International Workshop on Program Comprehension - IWPC 2001, Toronto
IWPC 2001 was held at the Westin Harbour Castle Hotel, Toronto, Ontario, Canada, on May 12-13. It was co-located with ICSE 2001, the 23rd International Conference on Software Engineering. The hotel, situated directly on the lakefront overlooking Lake Ontario, provided ample meeting and guestroom space for the entire conference.

The structure of this year's program emphasized the wide range of on-going research activities in the area of program comprehension. It included research papers in the areas of design recovery, program transformation, data flow analysis, and software architecture recovery, as well as papers on tools, techniques, and experimental studies. Keynotes were presented by Prof. Keith Bennett from the University of Durham and Prof. Dewayne Perry from the University of Texas.

This year, a total of 44 submissions were received by the program committee, and after a rigorous and painstaking review process, 28 were selected, and subsequently presented, in 9 sessions, running on parallel tracks.

I presented a paper entitled "Inference-based & Expectation-based processing in program comprehension". This research formally distinguishes between two variants of top-down comprehension (as originally described by Brooks and Soloway). The first is 'inference-based' comprehension, where the programmer derives meaning from clichéd implementations in the code. The second is 'expectation-based' comprehension, where the programmer has pre-generated expectations of the code's meaning. The paper described the distinguishing features of the two variants, and used these characteristics as the basis for an empirical study. This study established their existence, and identified their relationship with programmers' domain and coding standards familiarity.

On a final note, it was mentioned and agreed upon by all attendees of IWPC that due to the increasing awareness and significance of program comprehension as an integral part of the software lifecycle, this workshop should, in the near future, become a conference.

Next year, the International Workshop on Program Comprehension (IWPC 2002), will take place in Buenos Aires, Argentina, as a co-located event with ICSE 2002. Details of IWPC 2002 can be found by following the links on the [ICSE 2002 web site](http://www.icse-conferences.org/2002/).

**Michael O'Brien** \
Department of Information Technology \
Limerick Institute of Technology \
Moylish Park, Limerick \
IRELAND *michael.obrien@lit.ie*

---

# Announcements

### INSERC 2001
Details available at [www.lit.ie/research/conf/inserc2001.html].

### eLearn Magazine
I'd like to announce the availability of [eLearn magazine](http://www.elearnmag.org/). *eLearn magazine* puts education and technology in perspective. This online magazine is produced by the ACM and incorporates the knowledge and views of experts in the field of online learning. Advisory Board Members include: Don Norman of UNext and Nielsen Norman Group; and Randy J. Hinrichs of Microsoft Research.

*eLearn magazine* is free, and we encourage contributions. Contribution information is available on the site.

**Lisa Neal**
Editor-in-Chief, eLearn magazine
Consultant Architect, EDS Web Universities & Training

### David Gilmore
As an old and original PPIGer I thought I'd update people on my activities.

I am now the senior HF specialist at IDEO Palo Alto, worrying a lot about the user-centered design of numerous internet related products. I worked on 3COM's now-departed Audrey and a number of other internet-enabled keyboards, picture frames and entertainment devices - all involving detailed visits to people's homes and offices to understand their needs, goals and motivations.

As I write this I am in Helsinki about to spend 3 days visiting homes and offices here to understand a different cultural perspective on the internet and wireless technologies - for a client determined to provide a user-centered internet experience, rather than just a product catalogue.

Besides the high-tech angle I have also been working recently on the design of kitchen tools, office chairs and innovation in products for your pet (well mainly dogs in fact!).

Although the work of a user-centered design consultancy doesn't really include programming, I've been struck many times by the striking difference between hardware and software product development.

In hardware development there is a very clear boundary between the activities of the industrial designer and those of the engineers (whether mechanical, electrical or manufacturing) - even though they impinge on each other they all seem to be in pretty good agreement about their territories. Most importantly there is fairly standard agreement between them and clients about who has which responsibilities and what the appropriate form of deliverables should be.

However, for software no-one seems to know (or at least agree) where the boundary lies between interaction design and software engineering - a problem which can make life very difficult. Here there is little agreement about the right kind of design deliverable to enable software engineering to proceed.

And as one moves into the arena of web-enabled experiences .... - it seems that there is even more potential here for boundary confusion. Isn't this an area where PPIG should be contributing intelligent debate?

### Alan Blackwell
It's not really PPIG news, but since Helen and I have both attended PPIG in the past, people may be interested to know that we have just had our first child.

Congratulations to Alan! You can e-mail him at *Alan.Blackwell@cl.cam.ac.uk*

### Terry Eden
I'm a third year student in the University of East Anglia's applied computing program. My third year project will be concentrating on HCI issues in ubiquitous computing. I'll be looking at how humans expect to be able to control ambient intelligence (think of "The Computer" in Star Trek). It ties with Europe's Disappearing Computer initiative that is described in more detail at [www.cordis.lu/ist/fetdc-ob.htm](http://www.cordis.lu/ist/fetdc-ob.htm).
