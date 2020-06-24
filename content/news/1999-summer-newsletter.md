---
title: "Summer 1999 Newsletter"
date: 1999-07-01
newsletter: "july-1999"
---

Number 24, Summer `99 \
Edited by Paul Mulholland P.Mulholland@open.ac.uk

# Contents

[About PPIG]( {{< localref "#about-ppig" >}} )

[Spotlight on PPIGers]( {{< localref "#spotlight-on-ppigers" >}} ): Chris Douce, Georgios Heliades and Martin Rausch

[Testing and Debugging in Spreadsheet-Like Visual Programming Languages]( {{< localref "#" >}} )
by Margaret Burnett

[Using Z: the impact of specification upon quality]( {{< localref "#" >}} )
by Chris Roast and Jawed Siddiqi

[Educational Paradigms and Components for classroom Teamwork]( {{< localref "#" >}} )
by Martin Rausch and Eleonora Bilotta

[Workshop on End User Programming / Informal Programming]( {{< localref "#" >}} )
by Howie Goodell

[Empirical Studies of Programmers Workshop Postponed]( {{< localref "#" >}} )

[IEEE Symposium on Visual Languages, VL '99](http://www.isl.hiroshima-u.ac.jp/vl99.html)

[The Visual End User: A workshop on visual languages for end-user and domain-specific programming](http://www.cs.dal.ca/~smedley/veu/)


---

# About PPIG

The Psychology of Programming Interest Group (PPIG) was established in 1987 in order to bring together people from diverse communities to explore common interests in the psychological aspects of programming and/or in computational aspects of psychology. 'Programming', here, is interpreted in the broadest sense to include any aspect of software development. The group, which at present numbers approximately 300 world-wide, includes cognitive scientists, psychologists, computer scientists, software engineers, software developers, HCI people et al., in both Universities and industry.

PPIG aims to provide a forum for the rapid dissemination of results, ideas, and language or paradigm tool development, circumventing the long time-lag of conferences and journals. It does this by maintaining two electronic mailing lists - one for announcements and one for discussion - by publishing two newsletters a year, maintaining pages on the World Wide Web, and organising a workshop annually, together with other workshops as and when required.

The annual workshops, which always attract a high percentage of attendees from outside the United Kingdom, consist of keynote addresses by eminent practitioners in the relevant fields, discussion panels, software demonstrations and seminar-like presentations. Invited speakers have included Professors Jack Carroll, Bill Curtis, Laura Leventhal, Clayton Lewis, Gary Olson, Peter Polson, Elliot Soloway and Willemien Visser. Venues have included the Universities of Warwick (1989), Wolverhampton (1990), Huddersfield (1991), Loughborough (Jan 1992), INRIA (Paris) (Dec. 1992), the Open University (Jan. 1994), University of Edinburgh (1995), University of KaHo Sint Lieven, Ghent (1996), Sheffield Hallam University (1997), the Open University (1998) and University of Leeds (1999).

In 1996, for the first time, a workshop was held specifically to allow post-graduate students in the relevant disciplines to come together, give presentations and exchange ideas. It is hoped that this will be the first of a series.

There is no subscription. Financial help in the past has come from Xerox EuroPARC, the DTI and EPSRC. Further information is available from the organiser, Judith Segal.

The PPIG website can be found at http://www.ppig.org/

---

# Spotlight on PPIGers

## Chris Douce

Recently, I have taken the plunge and moved from academia to industry, much to the bemusement of some of my friends. 'Real life!', they exclaimed. They joked that I would soon be debating the merits of one company car make over another, and coveting a named car parking space next to the marketing manager. I told them that this would never happen, and that I will be very happy driving my humble studentmobile for many years to come. Being intelligent sorts, they were quick to agree that there is more than one type of 'real-life' and both equally as difficult. I also informed them that I intend to stay close to my academic interests - after all, my job of chasing bugs and being confused with programs and programming languages is not a million miles away from what I was confused with and reading about when I was a student. It is only now that there is a little more money involved, and the programs are a little more complicated. I'm not sure whether its because of my change, but I seem to find Dilbert calendars all the more amusing. I also seem to have changed my psychology of programming interests. I am now interested in programmers episodic/autobiographical memory in programmers, its strength, and how it develops. This is no more evident when I glance over a few sparsely commented object classes and ask my boss, 'hey, what the hell does this do?' His furrowed brow soon gives way to a brightening of his eyes and movements of the mouse, culminating in an explanation, 'its here! its here! look!....', with simultaneous scribbles on pieces of note paper (sometimes spatially arranged on the desk). Only now do I realise how little I know, and how much more there is to do in understanding what happens when we look at code, and wonder how it works. And how confusing my object hierarchies can get, especially first thing on a Monday morning.

## Georgios Heliades

Georgios Heliades has just completed (subject to examination) his Ph.D. – thesis entitled «An argumentative approach to supporting early software design activities» – at the Department of Computer Science, Loughborough University.

The thesis investigated the potential of design rationale to facilitate transfer of expertise among software designers working on error-prone tasks. That piece of research contributed towards a process model of the software design process based on argumentative reasoning as well as to the expansion of the role of notation in decision making activities of that kind. The strong experimental element in that work as well as the realisation of the benefits of looking at the design process from alternative perspectives brought up his interest in the PPIG community. He presented a paper at the 1st student PPIG workshop in 1996 and he became a member of PPIG just after PPIG 11. Other research interests include HCI and software methodologies.

During his time at Loughborough he worked as a teaching assistant on the Systems Analysis and Design first year course module (further information can be found at http://www-staff.lboro.ac.uk/~copv/coa281.htm) and as a research assistant on the SEDRES project (see http://www.lboro.ac.uk/departments/co/research_groups/sedres.html), an ESPRIT project defining data exchange standards for the systems engineering process in the aerospace industry. He currently plans his new study of “virtual discussion” between design diagrams and reader as an aid to the communication of the context of the original production and last update of the diagrams.

## Martin Rausch

Fraunhofer Institute for Computer Graphics (IGD) in Darmstadt, Germany.

I have gone to graduate school at the University of Colorado in Boulder where I worked on the team of Professor Repenning on issues related to the simulation authoring tool AgentSheets. As Master’s thesis topic I investigated issues of synchronous and asynchronous collaboration among student groups working in similar setups cooperating via the Web. I am now working at IGD and help establish AgentSheets and its simple yet powerful ideas in Europe. I am especially interested in end-user programming aspects and how EUP can benefit education.


# Testing and Debugging in Spreadsheet-Like Visual Programming Languages

**Margaret Burnett burnett@CS.ORST.EDU**

A group of us has been working on the problem of how users of visual programming languages might go about testing and debugging their visual programs. At this time, we are concentrating our work on the spreadsheet family of languages. Our goal is to bring some of the benefits of organized testing and debugging to these kinds of users and programmers. Our approach is a highly visual approach that is tightly integrated into a visual environment. We are prototyping our approach using [Forms/3](http://www.cs.orst.edu/~burnett/Forms3/forms3.html).

The researchers involved in this project are Margaret Burnett, Gregg Rothermel, Curtis Cook, Thomas Green, and several student researchers. For more information, see: [http://www.CS.ORST.EDU/~grother/vptestdebug.html](http://www.CS.ORST.EDU/~grother/vptestdebug.html)

---

# Using Z: the impact of specification upon quality

**Chris Roast and Jawed Siddiqi**

Sheffield Hallam University, \
Sheffield, S1 1WB, UK. \
Tel.+44 (0)114 225 2907 \
Fax.+44 (0)114 225 3161 \
c.r.roast@shu.ac.uk

The study reported is concerned with the human factors that can influence the effectiveness with which a design representation notation is exploited. We report an empirical study focusing upon the task of completing a formal specification expressed in the Z notation. The study illustrates how the requirement to employ a formal specification notation can have a deterimental influence upon the validity of the solution produced.

Keywords: Formal Specification, Z, Human Factors

[View PDF version of the paper](/pdf/1999-summer-newsletter-roast.pdf)

---

# Educational Paradigms and Components for classroom Teamwork

__Martin Rausch, [rausch@igd.fhg.de](mailto:rausch@igd.fhg.de)__ * \
__Eleonora Bilotta [eleb@abramo.it](mailto:eleb@abramo.it)__ **

\* Dept. Communication & Cooperation (A9) \
Fraunhofer Institute for Computer Graphics (IGD) \
Darmstadt

** Interdepartmental Centre of Communication (CIC) \
Department of Educational Sciences \
University of Calabria, Rende- Cosenza, Italy

## Introduction

The creative opportunities that computers are capable to provide are completely neglected in schools. In an effort to enrich teaching we planned to present a project, EPACOT (Educational Paradigms and Components for classroom Teamwork) with the aim to introduce new content as well as new content creation techniques. In particular, the objective of the project is to widespread the programming activity in European school (through simulation) in order:

* to study and analyse learning process students exhibit in designing a simulation;
* to gain a better knowledge about novice and guidance to teachers willing to take part in the experiment. Measures include seminars that instruct on the use and application of the simulation environment, on connecting simulations to other components, and on integrating such activities in a more explorative curriculum.

### Develop alternative curricula

A combined action among researchers and teachers of involved schools is foreseen. A number of workshops are organised to establish which alternative activities are necessary to define the curricular activity models and to establish the learning/teaching modalities to be used.

In particular, the workshops’ objective is to develop a model of constructivist curricula (a format) and a way to motivate students to explore knowledge in a personalised manner, through learning by designing, or learning by doing.

### Employ creativity tools

The courseware and seminars will support different use case scenarios that target teachers and students with different degrees of exposure to the simulation tools. The most basic use case is to reuse an already completed simulation component as it is in a classroom activity. Many such simulation components exist and can be used to illustrate processes from subject areas from social science (California Grape Boycott) to biochemistry (effects of medication on synaptic gap) (1). Once teachers and students feel comfortable using the simulations the next step is to motivate them to extend existing simulations and add new aspects to the simulation by designing and end-user programming new simulation elements (2). Ultimately, users will be able to design a whole new simulation of a process they are interested in.

### Encourage social computing and component reuse

The main result and objective of most efforts is the creation of a telematic network and its presentation via a worldwide web interface as the EPACOT repository. The new information technologies can transform a predominantly informative medium such as the web into a formative tool. This transformation is achieved by using appropriate educational environments that support knowledge transfer and teaching/learning processes. The users of the repository will not be mere consumers – as are 90% of the web surfers – but active co-designers in a collaborative environment (3).

### Test the EPACOT approach and grow repository

When an initial seed of objects has been inserted into the repository and classroom activities have been designed and arranged in collaboration with teachers experimental classes are started where the different aspects can be assessed.

## Experimental setting and expected results

In the EPACOT project teachers and students are the primary sources for user feedback. The learning activities carried out by the students and the teachers and their role in class are observed and described. The experimentation will also give assessments of the usability of AgentSheets and the internationalised versions provided by the EPACOT project partners. Interesting for further studies and projects are interaction activities among students while learning the visual end-user programming language Visual AgenTalk and at the same time simulation design and problem solving in this environment. As for the teachers it will be important to note which level of proficiency is necessary or inadequate in order to apply such end-user programming language. This will have a direct impact on the set-up of follow-up projects.

At the beginning of the experimental phase all experimental subjects (students) will be instructed the first basic step of programming with the Visual AgenTalk, the visual end-user programming interface to AgentSheets. At the end, the students will be able to master Agentsheets and to use it to build their own simulations. This step is inter-linked with the contents learning activities. The program and programming instructions should make up a minimal portion of the class time. The centre of attention will move immediately to the content and the problem domain that is covered in the class.

The experimental classes will take place in Italy and England where EPACOT is applied in two very different situations. The project partners will take the function of mentors to the teachers and guarantee a direct link between methodology, technology, and their implementation.

### Data collecting

The classroom activities are monitored and analysed by teachers and EPACOT researchers under different perspectives. Videotapes as well as transcripts of class sessions will make dissemination of observations, conclusions, and results transparent and usable for the research community.

### Elaboration of results

All the partners in the project will utilise elaboration methodologies (which will be identified collaboratively) that will be applied to analyse the data collected. Reports on results from each country will be composed and combined to a final report for all the samples taken by the partners. This final report will also analyse cultural or organisational differences and their implications for the viability of the approach under different circumstances. These deliverables will also be made public on the project web server.

To summarise, the results of EPACOT project, interesting for the PPIG sector could be:

* Improving teachers’ and students’ use of programming languages enabling them to augment their creative potential.

Teachers will share scientific collaboration among researcher, students and programmers and will improve their qualitative and quantitative performances, oriented towards international models and new styles of teaching.

Students will be able to build new and creative objects, through the narrative simulation modality, to design and to synthesise new objects, moving through the phases of ideation, conceptual and structural organisation. This process is a re-organisation of knowledge gestalten in order to produce new representations and simulations of the phenomena they are studying.

* Check out the ability students and teachers should have to become expert programmers.
* Create a repository on line where it is possible to operate in the Participatory Design modalities.

<br>

(1) A. Repenning, A. Ioannidou, and J. Ambach, "Learn to Communicate and Communicate to Learn," in Journal of Interactive Media, pp. 1998. \
(see: http://www.cs.colorado.edu/~ralex/papers)

(2) M. Rausch; "The Agent Repository – Supporting Collaborative Contextualized Learning with a Medium for Indirect Communication"; Master’s Thesis; University of Colorado, 1996 \
(see: http://www.cs.colorado.edu/~ralex/papers)

(3) A. Repenning, M. Rausch, J. Phillips, A. Ioannidou; "Using Agents as a Currency of Exchange between End-Users". Proceedings of AACE WebNet ’98 \
(see: http://www.cs.colorado.edu/~ralex/papers)

---

# Workshop on End User Programming / Informal Programming

**Howie Goodell hgoodell@cs.uml.edu**

The workshop on End User Programming / Informal Programming at CHI 99 (Workshop #11; original title "End User Programming and Blended User Programming) produced some excellent position papers (including one by Thomas Green he was unfortunately unable to present) and interesting discussions. Read all about it, including the official report and full text of the position papers, at

http://www.cs.uml.edu/~hgoodell/EndUser/blend/index.html

---

# Empirical Studies of Programmers Workshop Postponed

Since 1986, the Empirical Studies of Programmers (ESP) Workshops have been the premier forum for research on the Psychology of Programmers. The Eighth Workshop (ESP8) was to be held October 1999 in Alexandria, Virginia, USA. Unfortunately, due to an insufficient number of submissions, the conference organizers made the difficult decision to postpone ESP8.

Instead, the conference organizers have arranged for a special issue of the International Journal of Human-Computer Studies. The special issue will contain a selection of the manuscripts submitted to ESP8 along with an introduction by the guest editors. This special issue is currently being produced and should appear sometime in 2001.

We apologize to everyone who was planning to attend ESP 8 in October, and we will distribute an announcement when arrangements for the postponed conference are in place.

Irvin Katz, Laura Leventhal, Marian Petre

ESP 8 conference committee
