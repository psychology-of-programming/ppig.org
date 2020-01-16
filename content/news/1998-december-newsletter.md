---
title: "December 1998 Newsletter"
date: 1998-12-01
newsletter: "december-1998"
---

Number 23, December `98 \
Edited by Paul Mulholland P.Mulholland@open.ac.uk

# Contents

[About PPIG]( {{< localref "#about-ppig" >}} )

[A constructive model of OO design]( {{< localref "#a-constructive-model-of-oo-design" >}} ) by Rob Rist

[Spotlight on PPIGers]( {{< localref "#spotlight-on-ppigers" >}} ): Susan Wiedenbeck, Alan Blackwell and Howard Goodell

[Web sites of interest to PPIGers]( {{< localref "#web-sites-of-interest-to-ppigers" >}} ) by Ray Panko

[VL '99 Special Track on Usability of Visual Languages]( {{< localref "#usability-of-vls" >}} ) Margaret Burnett

[CHI '99 Workshop on End-User Programming and Blended-User Programming]( {{< localref "#chi-99-workshop-on-end-user-programming-and-blended-user-programming" >}} )

[Empirical Studies of Programmers, ESP 8]( {{< localref "#empirical-studies-of-programmers-esp-8" >}} )

[PPIG '99 Workshop]( {{< localref "#ppig-99-workshop" >}} )

---

# About PPIG

The Psychology of Programming Interest Group (PPIG) was established in 1987 in order to bring together people from diverse communities to explore common interests in the psychological aspects of programming and/or in computational aspects of psychology. 'Programming', here, is interpreted in the broadest sense to include any aspect of software development. The group, which at present numbers approximately 300 world-wide, includes cognitive scientists, psychologists, computer scientists, software engineers, software developers, HCI people et al., in both Universities and industry.

PPIG aims to provide a forum for the rapid dissemination of results, ideas, and language or paradigm tool development, circumventing the long time-lag of conferences and journals. It does this by maintaining two electronic mailing lists - one for announcements and one for discussion - by publishing two newsletters a year, maintaining pages on the World Wide Web, and organising a workshop annually, together with other workshops as and when required.

The annual workshops, which always attract a high percentage of attendees from outside the United Kingdom, consist of keynote addresses by eminent practitioners in the relevant fields, discussion panels, software demonstrations and seminar-like presentations. Invited speakers have included Professors Jack Carroll, Bill Curtis, Laura Leventhal, Clayton Lewis, Gary Olson, Peter Polson, Elliot Soloway and Willemien Visser. Venues have included the Universities of Warwick (1989), Wolverhampton (1990), Huddersfield (1991), Loughborough (Jan 1992), INRIA (Paris) (Dec. 1992), the Open University (Jan. 1994), University of Edinburgh (1995), University of KaHo Sint Lieven, Ghent (1996) and Sheffield Hallam University (1997).

In 1996, for the first time, a workshop was held specifically to allow post-graduate students in the relevant disciplines to come together, give presentations and exchange ideas. It is hoped that this will be the first of a series.

There is no subscription. Financial help in the past has come from Xerox EuroPARC, the DTI and EPSRC. Further information is available from the organiser, Judith Segal.

The PPIG website can be found at http://www.ppig.org/


# A constructive model of OO design
**Rob Rist, rist@socs.uts.EDU.AU**

Computing Sciences, University of Technology, Sydney \
PO Box 123 Broadway, Sydney, NSW 2007 Australia

This year, I have used the framework I developed for empirical analysis of software design to teach (simple) OO design. I teach the OO language Eiffel as a first language. I've found that I can do this best by separating the syntax and mechanism of Eiffel from the process of design, allowing me to treat design as an explicit topic.

My basic approach is (what else?) focal or bottom-up design, where goals and objects are orthogonal. I divide the subject into three parts: design based on data flow, control flow, and inheritance. The steps in the model I teach are

1. Identify and list the goals in the specification.

For each goal

2. Write down the focus

The focus is the "meaning" of the goal. If the goal is to produce a value (function), it is the line that produces the value. If the goal is to change a value (procedure), the focus is the line that changes the value. If the goal is a restriction on a value (see 4 below) such as "maximum" or "valid", then the focus is the line that tests for that restriction on the value.

3. Add the data (control) flow that supports the focus.

This is the constructive equivalent of backward slicing, that identifies all and only the data (control) that is needed. As Francoise has shown, novices tend to infer features from object names with little concern for their relevance.

4. For each node in the data (control) flow, expand its name to the form

```
<goal, object>, <role, object>,
<role, goal, object>, or
<role, goal, object, class>, or permutations on these.
```
A role is a restriction on a value, such as "highest" or "first"; it can also be seen as a filter on a set.

5. From the expanded names, use the goal and object to locate each node on a system structure chart.

6. Code each node as a routine; the "source" data values are usually attributes, that may be set with inputs, arguments, constants, or literals.

When my students adopt this approach, they get about 90% of the structure of the OO system "for free". The hardest part is (1) to convince them that it is better to follow a method than to wing it, and (2) to get them to listen to what the method tells you (use the expanded names as a design heuristic).

A longer, but still very rough, description with examples may be found by clicking on "Design Studies" in http://www-staff.socs.uts.edu.au/~rist

# Spotlight on PPIGers

## Susan Wiedenbeck

Susan Wiedenbeck's new address is:

Susan Wiedenbeck \
Faculty of Computer Science \
DalTech \
Dalhousie University \
P.O. Box 1000 \
Halifax, Nova Scotia \
Canada B3J 2X4

phone (902) 494-1425 \
susan@cs.dal.ca

## Alan Blackwell

Alan Blackwell has recently completed (subject to examination) his PhD at the ex-Applied Psychology Unit in Cambridge. The title of his thesis was "Metaphor in Diagrams", and completes an experimental investigation of the theoretical paper he presented at PPIG 8 in Ghent. The results of this work will be presented at PPIG in the near future, but in general they do not support the proposals made at PPIG 8.

Alan has now moved to the Computer Laboratory in Camridge University, where with EPSRC funding he is working on a PPIG-related project. This project, christened "Vital Signs: New Paradigms for Visual Interaction", is based on the work that he presented with Mark Simos at PPIG 10, and on Thomas Green's Cognitive Dimensions of Notations. It should have particular relevance to the current discussion on "end-user" programming.

Further information on the Vital Signs project is available at: http://www.cl.cam.ac.uk/users/afb21/vital/index.html

## Howard Goodell

My name is Howard Goodell. I have been doing controls programming, mostly in the semiconductor capital equipment business, since I dropped out of a chemistry PhD program in the late 70's. 4 years ago I took over an end-user-programmed control system for equipment automation. My users and fellow-programmers and I agree this system transformed a frequently painful and tedious development process into the most productive software interaction of our careers. A paper on this system is in preparation.

End-user programming is also my doctoral research topic in the HCI Group of the Computer Science Department at the University of Massachusetts at Lowell, USA. I have maintained an End-User Programming Web page http://www.cs.uml.edu/~hgoodell/EndUser there since 1997. With Carol Traynor (now Professor of Computer Science at St. Anselm College in Manchester, New Hampshire USA), I organized a SIG on End-User Programming at CHI 97. We are currently soliciting position papers for a workshop at CHI 99 on "End-User Programming and Blended-User Programming" http://www.cs.uml.edu/~hgoodell/EndUser/blend/index.html.

The latter is my term (better suggestion, anyone?) for the rapidly growing class of concrete-minded, experimentally trained, full-time programming professionals: "Access programmer"; "NT networking expert"; "SAP applications specialist". They fall in the continuum of programming professionalism between end user and university-trained professional programmer. The purpose of the workshop is to formulate a research agenda for studying this phenomenon. I would like to acknowledge that the genesis of this idea was partly from the PPIG mailing list discussion of the "Eisenstadt-Bonar bet" last Spring. Also Prof. Russell Winder and others helped me clarify the idea after I suggested it there a couple months ago.


# Web sites of interest to PPIGers
**Ray Panko panko@hawaii.edu**

College of Business Administration, University of Hawaii \
2404 Maile Way, Honolulu, HI 96822, USA \

I maintain two research websites that may be of interest to PPIG members.

The Spreadsheet Research (SSR) website focuses on errors in spreadsheet development and inspection.

My Human Error (HumanErr) website collects data on error rates in a broad spectrum of human cognitive activities. There is a page on error rates found in programming. These error rates, not surprisingly, are similar to those in programming and other complex human cognitive activities.

Spreadsheet Research (SSR) website: http://www.cba.hawaii.edu/panko/ssr/

Human Error Website: http://www.cba.hawaii.edu/panko/HumanErr/

# Usability of VLs
**Margaret Burnett burnett@CS.ORST.EDU**

The Call for Papers for the IEEE Symposium on Visual Languages can be found at http://www.isl.hiroshima-u.ac.jp/vl99.html

Of special interest to PPIG'ers: [Usability of VLs - Special Track of VL'99](https://web.archive.org/web/20051113091727/http://www.cs.orst.edu/~burnett/track-Usability.html)

The primary reason for VL research is to increase human effectiveness in communicating with computers. For this reason, we view research on techniques and tools for designing, developing and evaluating usability aspects of VLs to be a central, core subdiscipline of VL research. PPIG'ers take note: we want your papers! Due date extended to **March 10, 1999**.

# CHI '99 Workshop on End-User Programming and Blended-User Programming

[The workshop website is at: http://www.cs.uml.edu/~hgoodell/EndUser/blend/index.html. The Call For Papers appears below]

[CORRECTION: Carol Traynor's email address is ctraynor@cs.uml.edu and not ctraynor@uml.edu, as stated when the newsletter first appeared]

## 1999 Conference on Human Factors in Computing Systems

CHI 99 \
15-20 May 1999 \
Pittsburgh, PA, USA \
http://www.acm.org/sigchi/chi99

CHI 99 Workshops provide an extended forum for small groups to exchange ideas on a topic of common interest. Workshop participation is by invitation only based on position papers submitted by 26 February 1999. The 14 Workshops for CHI 99 will be held 16-17 May 1999.

One workshop that may be of particular interest to PPIG readers is:

## End-User Programming and Blended-User Programming

End-User Programming has not met expectations: today's computer world is dominated by "fatware" programs with hundreds of features, not simple applications built by the users themselves. Yet, a strange convergence is occurring between roles of programmers and end-users. Professional programmers become end users of complex IDEs (Integrated Development Environments) indistinguishable from tools for non-programmers. A new group we call "blended-user programmers" has appeared -- professional application experts without software degrees: Web designers and GUI or business applications programmers. Major end-user applications support a continuum of programming tools; advanced users may move into these new software careers.

This workshop will use and re-evaluate insights of classical end-user programming to understand the converging programming world. Questions it may address:

* What are useful boundaries of "programming" in an environment of check-box customization and code modification?
* What are appropriate programming abilities for schoolchildren and adults to learn? What requirements are minimized with modern tools?
* What are commonalties and differences between new areas of blended/end-user programming and forms studied earlier?
* What technical and social interactions develop when "real" programmers with CS degrees work with blended-user programmers from much less formal backgrounds?
* Do certificate courses primarily expand blended-user programmers repertoire of tinkering, or make them more analytical?

Fifteen experts in end-user programming, psychology and sociology of programming backgrounds will be selected based on position papers. If appropriate, these may be published as a book to inform research and practice in this emergent area.

Workshop participation is by invitation only based on position papers submitted by 26 February 1999

**Contact:** \
Carol Traynor \
St. Anselms College \
100 St. Anselm Drive \
Manchester NH 03102 USA \
Tel: +1 603 656 6021 \
Email: [ctraynor@cs.uml.edu]

The workshop website is at: http://www.cs.uml.edu/~hgoodell/EndUser/blend/index.html.

For further information about CHI 99 Workshops, contact the CHI 99 Workshop Co-Chairs at: [chi99-workshops@acm.org]

The annual CHI conference is sponsored by ACM's Special Interest Group on Computer-Human Interaction (ACM SIGCHI).


# Empirical Studies of Programmers, ESP 8

[The ESP-8 web site address is http://hfac.gmu.edu/ESP. The Call For Papers recently sent to the PPIG mailing list appears below]

The Empirical Studies of Programmers (ESP) workshops are the premier forum in North America for the presentation of both field and laboratory studies of programmers and software engineers.

## Key Dates
Papers and Panels are due: March 31, 1999 \
Authors informed : May 17, 1999 \
Final submissions due: June 10, 1999 \
Poster submissions due: August 2, 1999 \
Poster authors notified: August 27, 1999 \
Workshop: Oct. 22-24, 1999 \

## Topics

The primary focus of ESP 8 (as with all ESP workshops) is the empricial observation and theoretical analysis of programming and software engineering behavior. Topics include, but are not limited to:

* design, comprehension, debugging and modification of programs
* teaching, learning and knowledge transfer of various programming languages and paradigms
* programming environments
* end-user programming, programming by example and related issues
* novice/expert differences in programming

## Submission categories

### Papers
Submissions of any length are accepted. (15-30 pages is a reasonable length.)

### Panels
Panel proposals should contain the names and affiliations of the organizer and all panel members. The proposal should consist of an overall statement about the panel's purpose and statements from each of the panel members stating their position on the panel. This should be limited to 3 pages. A brief description of the way the panel will be conducted should accompany the submission.

### Posters
Posters represent work-in-progress. Poster submissions should include a brief sketch of the proposed poster and a two-page description of the work presented on the poster.

## Submission Information
Six copies of paper and panel submissions should be sent to arrive no later than March 31, 1999. Send to either:

## Empirical Studies of Programmers (non-North American submissions)
c/o Dr. Marian Petre \
Computing Department \
Open University \
Milton Keynes MK7 6AA \
U.K.

### Empirical Studies of Programmers (North American submissions)
c/o Dr. Laura Leventhal \
Computer Science Department \
Bowling Green State University \
Bowling Green, OH 43403 \
U.S.A.

### Poster Submission Information
Four copies of the poster description and the poster sketch should be sent to arrive no later than August 2, 1999. Submit posters to one of the addresses above. Posters will be reviewed more lightly than submissions in the papers category.

### Publications
Accepted papers will be published by ACM Press. In addition, we tentatively plan to invite authors of accepted papers to submit revised and expanded versions of their papers to a special journal issue. Further details will be provided when arrangements have been finalized with a journal. Poster descriptions will be distributed to ESP attendees in a photocopied booklet.

## For more information
See the ESP Web page at http://hfac.gmu.edu/ESP

Contact any of the co-chairs:

Dr. Irvin Katz, +1-703-993-4663
Dr. Marian Petre, +44 1908-65-33-73
Dr. Laura Leventhal, +1-419-372-2765

## Accommodation
ESP 8 will be held at the Ramada Hotel ($99/night, single or double) situated in Alexandria, Virginia, about 15 minutes by Metro from the Capital and Museum district of Washington, DC. The hotel provides free shuttle buses to and from Washington National Airport as well as to and from the nearest Metro stop. The hotel can provide accommodation at the above rate for ESP attendees arriving earlier or departing later than the conference dates.

### Student Participation
Student submissions are encouraged. We will provide complimentary registration and housing for students who are first authors of accepted papers.

Additionally, we are expecting that a student-only conference will be held prior to ESP. Students will be invited to the opening ESP cocktail party regardless of whether they are attending ESP. In addition, early arrivals at ESP will be invited to a late afternoon session of the student conference on Oct. 22, 1999. We are also planning to have a special student poster section for any students attending the student conference. More details will be posted on the ESP Web page and on the PPIG mailing list at a later date. John Pane will be the organizer and Dr. Susan Weidenbeck will be the mentor for this program. Contact John Pane at pane+esp@cs.cmu.edu for information.

## Workshop Schedule
ESP 8 will follow the typical format for ESP workshops. The general outline of this format is:

### Friday, Oct. 22

Registration opens in the late afternoon \
Late afternoon open session with student conference \
Early evening cocktail party \
Dinner on your own - chance to meet new and previous attendees.

### Saturday, Oct. 23
Registration opens prior to breakfast \
Continental Breakfast \
Presentations \
Lunch * \
Presentations \
Banquet* \
*These will include a speaker.

### Sunday, Oct. 24
Continental Breakfast \
Presentations \
Finish around lunch time

## ESP 8 Program Committee
Alan Blackwell - University of Cambridge, U.K \
Deborah Boehm-Davis, George Mason University, U.S.A. \
Michael Clancey, University of California-Berkeley, U.S.A. \
Francoise Detienne, INRIA, France \
Ben du Boulay, University of Sussex, U.K. \
Mark Guzdial, The Georgia Institute of Technology, U.S.A \
Shelly Heller, George Washington University, U.S.A. \
Paul Mulholland, The Open University, U.K. \
John Pane, Carnegie-Mellon University, U.S.A \
Robert Rist, University of Technology Sydney, Australia \
Mary Beth Rosson, Virginia Institute of Technology \
Jorma Sajaniemi, University of Joensuu, Finland \
Jean Scholtz, NIST, U.S.A \
Judith Segal, University of Surrey, U.K. \
James Spohrer, Apple Computer, U.S.A. \
John Stasko, The Georgia Institute of Technology, U.S.A \
Barbee Teasley, Southwestern Bell, U.S.A \
Susan Weidenbeck, University of Dalhousie, Canada \
Willemien Visser, INRIA, France

## ESP 8 Organizing Committee
Irvin Katz, Co-chair and Local Arrangements \
Marian Petre, Co-chair \
Laura Leventhal, Co-chair

## ESP Board of Directors
Deborah A. Boehm-Davis, Chair \
Wayne D. Gray, Secretary/Treasurer \
Susan Wiedenbeck, Board Member \
Jean Scholtz, Board Member \
Stan Rifkin, Board Member


# PPIG '99 Workshop

Conference website here: [workshops/1999-annual-workshop](workshops/1999-annual-workshop)
