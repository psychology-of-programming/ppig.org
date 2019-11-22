---
title: "PPIG 2015: Work in Progress meeting report"
date: 2015-02-28
newsletter: "wip-report-2015"
---

By __Chris Douce__

## Day 1

On 8 January 2015 I went to a mini-workshop: the Psychology of Programming Interest Group (PPIG) Work in Progress meeting. I've had an affiliation with PPIG for what must be at least fifteen years and I try to visit their meetings whenever I can. In some sense, returning to the PPIG meetings is like returning to a comfortable academic home: you regain enthusiasm for the research interests that you once held (and have an opportunity to say hello some familiar faces too).

This 2015 WIP event (as it is colloquially known) was held at the University of Middlesex in Hendon Town Hall and skilfully organised by Richard Bornat, who is a PPIG community regular. This short series of two blog post aims to summarise what were my own highlights.

### Keynote talk: Thomas Green

The opening keynote was by Thomas Green, who is one of the founders of the group. Thomas told us what the group was about and emphasised the point that the group doesn't just discuss research into programming, but also the activities that surround programming (and psychology too). Subjects for investigation have involved pair programming and explorations into the sociological and anthropological. Other research subjects have included computer science education and pedagogy, and studies into the relationship between personality and programming.

Thomas is known for creating (or discovering) the [cognitive dimensions of notations framework](http://en.wikipedia.org/wiki/Cognitive_dimensions_of_notations) (Wikipedia). His framework can be used to help us think about programming language design and user interfaces. Thomas described it as 'ambitious in scope, [and a framework that] addresses any kind of information artefact'. Simply put, Cognitive Dimensions is a set of principles that helps us to think about stuff.

To explain, Thomas gave us a couple of examples. One of the dimensions is viscosity (which is my personal favourite!) Viscosity is, of course, an attribute of liquids: the higher the viscosity, the harder it is to push you hand through a liquid (for example) – I think I've got that the right way round! When it comes to the dimensions, this can be understood in terms of 'changes' to something (or, to move a system from one state to another). To make one change (to an information artefact), you might have to do a whole bunch of smaller changes before you get to your desired outcome.

Another dimension is: hidden dependencies. An example of this is the links or connections that might exist between the different cells of spreadsheets. You can't immediately see what the connections between different cells might be, but you need to understand them if you're going to understand and work with a spreadsheet.

This is all very well and good, but how does this relate to programming that we find in the real world? Thomas gave us a number of examples of computer code used with a content management system (CMS). Why study content management systems? Thomas had some good answers: they were widely used, often are pretty difficulty to get your head around (which is certainly true!), and they haven't been studied very much.

If you're interested in content management systems, this Wikipedia page presents an amazing [list of different content management systems](http://en.wikipedia.org/wiki/List_of_content_management_systems) (Wikipedia). On the same subject of geek lists, this is another favourite of mine: [comparison of web application frameworks](http://en.wikipedia.org/wiki/Comparison_of_web_application_frameworks) (Wikipedia). You can spend hours looking though these different pages. These two summary links clearly show how big the 'CMS space' is. (As an aside, if you have too much time on your hands, there's also a [List of Cakes](http://en.wikipedia.org/wiki/List_of_cakes) and a [List of Lists](http://en.wikipedia.org/wiki/Portal:Contents/Lists))

An interesting point that Thomas made (which is one that resonates with my own experience), is that they all claim they are 'easy to use'. Two examples that were spoken about were [Wordpress](http://en.wikipedia.org/wiki/WordPress) (Wikipedia) and [Drupal](http://en.wikipedia.org/wiki/Drupal) (Wikipedia). For the purposes of Thomas's presentation, we looked at the [Perch](http://grabaperch.com/) (CMS website), a CMS that I had never heard of before. The point was clear: Thomas's framework can be used applied to study CMS's and web frameworks.

After being mildly baffled with screens filled with code that used lots of angle brackets, there was a brief question and answer session. I think I made a comment that I chose a CMS based on the quality of the on-line tuition videos. My decisions were not based on language efficiency, but how easily I could see how to create something that similar to what I wanted to do. (I've often wondered about whether we could look to the murky world of media studies to learn about why some tools become more popular than others: there's a whole other dimension of CMS systems that could be explored). There was also brief discussion about design patterns, since many of them make use of the model-view controller pattern.

It was pretty thought provoking stuff. When it comes to content management systems, I can't help but think there's an opportunity to use them as a vehicle to conduct research into the creation, development and sustainability of software communities.

### Active error: examining error detection and recovery in software development

Tamara Lopez gave the first talk of the day, and within minutes of starting her talk, I had started to remember some research I looked at over fifteen years ago. Tamara's research was all about human error and programming. As Tamara was speaking, I thought to myself, 'I wonder whether she has heard of a researcher called James Reason. The answer came within minutes: of course she had.

Reason wrote a book called Human Error and carried out research into active errors (mistakes that happen in 'real time') and latent errors (which remain undetected within a system or product for considerable time). Have you ever bought a chocolate bar, unwrapped it from its wrapper and then thrown the chocolate bar away? Have you ever walked into a room and immediately thought, 'why am I here?' I recently put my keys in my fridge for no apparent reason. These, I guess, are examples of active errors.

The aim of Tamara's research was to perform a naturalistic observation of error in programming, and gather reports of error occurrence. Understanding the characteristics of error can, of course, allow us to understand more about it and why error arises.

Tamara used a great method. She was studying pair programming data videos that had been published on the internet through a website called [Pairwith.us](http://pairwith.us/) (website). The developers were working on a project to adapt some kind of testing tool. Tamara analysed the errors in terms of incidents and themes. Some keywords that I picked up from Tamara's talk were temporal, material and social. A good talk and interesting research.

### Visual Analytics as End-User Programming

The second research talk was by Advait Sarkar who had travelled from the University of Cambridge. Advait gave a demonstration of some software that he had put together. The focus of his prototype appeared to relate to the area of data analytics, specifically, how the area of machine learning might be connected to a spreadsheet environment.

Following this session (and Advait's demonstration) there was there quite a bit of discussion about different machine learning approaches such as decision trees and neural networks; subjects that I hadn't really touched on or explored in any great depth since I was an undergraduate. Advait's presentation wasn't really in my area of expertise but it's good to be exposed to different areas.

### SQ and EQ and programming, revisited

The next talk was by Melanie Coles from Bournemouth University. I remember Melanie from other PPIG events, so it was great to see her again. It was interesting to hear that her talk related to some earlier research that she presented at PPIG back in 2007 (if I've understood this correctly).

The title of her talk was: 'SQ and EQ and programming' So, what exactly does SQ and EQ mean? I understand them as rough and broad measures of personality. EQ is an abbreviation for Empathy Quotient. Simply put, EQ is a measure of someone's drive to identify with other peoples' feelings and emotions. SQ, on the other hand, means Systemising Quotient. It is the extent to which people have a drive to understand rules governing things.

I've made a very rough note that Melanie related both measures to work carried out by Simon Baron-Cohen, who works in the area of autism research. I've made another note in my notepad that there are tensions between these traits, along with the sentence, 'scientists score higher in AQ than non-scientists'.

Some studies seem to suggest a correlation between the role of programming and these traits. Other studies, on the other hand, don't show anything. The message coming through is that you don't have to be high on the AQ scale to become a programmer.

I don't know that this means, but I've made another note that reads 'polite grumpiness about sterotypes' which might have been scribbled down during the question and answer session. I have no idea who was expressing polite grumpiness, or which stereotypes were being discussed. I do, however, feel that this expression should still stand and has some validity. A sensible rule is that if you're going to take issue with stereotypes, you'll go a lot further if you politely disagree rather than go around shouting about them. I should also add, that I have no idea how this paragraph relates to Melanie's very good (and very clear) presentation. All this said, some really interesting ideas and (some exceedingly polite) discussions.

A great end to the first day!

## Day 2

### Teaching programming at a distance

The first presentation of the second day was by yours truly. I gave a short talk about a university funded project that aims to understand more about the teaching experience of Open University associate lecturers who are tutoring on the [TT284 Web Technologies](http://www.open.ac.uk/courses/modules/tt284) module.

One of the purposes of the project was to understand issues particular to the learning (and teaching) of programming. An area of particular interest is the transition between the first level modules (which use some visual programming language) to the second level modules which require students to pay more attention to other issues, such as language syntax.

I wasn't able to present any firm findings at this stage (since I keep getting sucked into the idiosyncrasies of my day job), except that three themes that were emerging were that some students can struggle with understanding what PHP is and how it works, confusion about Javascript, and the perpetual battle to understand regular expressions (which is, I believe, an issue that pretty all developers, expert or novice, seem to have)

The question and answer session was interesting. There was some chat about a coding DoJos (group coding sessions), the use of MOOCs (FutureLearn and the Kahn Academy), and how get students talking to each other.

### Holistic programming teaching at Middlesex

Franco Raimondi's talk was rather different to all the others: he showed us some robots (real hardware!) that he used in his teaching. They had an interesting design, using both Raspberry Pi devices that were connected to Arduino microcontrollers.

One question was: why use both? The Arduinos are used to control analogue input, but the heart of the control is managed (as far as can understand it) by the Raspberry Pi devices. Students then have the challenge of how to design and implement a communication protocol between the Pi and the sub-component. I personally think this is a great approach: students are exposed to different devices and learn more about their purpose. When I had a job in industry, one thing that I had to do is figure out how to get one embedded controller talking to another: Franco's robots would have helped me a lot to figure out how to do this. More information about the robots can be found by taking a look at the [MIddlesex Robotic plaTfOrm: MIRTO website](http://www.rmnd.net/middlesex-robotic-platformo-mirto/).

Okay, so there is an interesting robot, but how are they used in practice? Franco described a series of lectures, design workshops, programming workshops and physical computing workshops. In the workshops (if my notes are correct!) students are asked to solve different problems, such as to write a line following algorithm where the robot has to cater for 90 degree turns, and to complete different line circuits as fast as possible. Students could also implement control algorithms, such as [PID controllers](http://en.wikipedia.org/wiki/PID_controller) (Wikipedia) (which again takes me back to the days when I worked in industry for a while), remote control and managing the taking of cameras by controlling the Raspberry Pi.

What I found really interesting was that the platform (and the workshops) made use of a programming language called [Racket](http://en.wikipedia.org/wiki/Racket_(programming_language)) (Wikipedia). Racket is a language that I had not heard of before, but apparently it has roots in the Lisp language. In some respects, I commend the choice (because it's great to expose students to different programming paradigms), but on the other hand, there is something to be said for getting to grips with tools that are used in industry. I guess this just goes to show that whenever you come along to workshop like these, you always learn new stuff.

Towards the end of Franco's session, he spoke about a system to record Student Observable Behaviours, which then led onto a discussion about learning objectives. Apparently, the use of 'observable student behaviours' is something that Middlesex use, perhaps as a part of their assessment strategy. We were shown a web-based tool that lecturers can use to gather evidence of student engagement and activity.

I don't know what this relates to, but I also made a note of a place called [The Crystal](http://www.thecrystal.org/) (Crystal website), which was also described as the Siemens technology centre. As soon as I looked into it, I realise that I had once seen it before: on a cable car ride across the Thames. I now know how to get to The Crystal if ever I need to visit it!

I enjoyed Franco's session: he covered a lot of 'tech stuff' in a very short time. Students at Middlesex are clearly challenged and are clearly kept busy!

One thought is that different computing courses and degrees cover different topics and perspectives. When I was heading home from the workshop I remembered that The Open University covered a bit about robots too on a first year undergraduate module that has the code: [TM129 Technologies in Practice](http://www.open.ac.uk/courses/modules/tm129) (OU website). Students are also presented with the challenge of creating a line following robot. Rather than using real robots, a simulated one is used (but, students can get to see real ones if you come along to an engineering day school).

### Measuring programming achievement after a first course

The next presentation was by Ed Currie who presented what were described as 'thoughts and preliminary research'. One of the key thoughts (and one that I found most interesting) was why some students find programming so difficult. One note that I have made is that we can't teach it, students can only learn programming. It's not up to us; it's up to them, and our job (as lecturers and teachers) it to facilitate the learning.

Ed mentioned the idea of [Threshold concepts](http://en.wikipedia.org/wiki/Threshold_knowledge) (Wikipedia) by Meyer and Land. I've made a note of the point that 'sequence is a threshold concept' (when it comes to programming). I remembered hearing the phrase before from a colleague who was doing what I think was some research to see what happened when students grappled with key 'threshold concepts'.

Two great phrases that I've noted down are 'neo-piagetian stages' and ['flip classroom'](http://en.wikipedia.org/wiki/Flipped_classroom) (Wikipedia). In some respects the OU has always been doing 'flipped classrooms', i.e. students study some material and the go to a face to face tutorial to apply what has learnt, either in terms of solving a problem, or through facilitated discussions.

I don't know what the context was or where this came from, but I also made the note 'sharing of learning stories'. This might have just been an idle idea during Ed's talk, or something that Ed had said. When it comes to learning how to do computer programming, I've got my own story (which might well be insufferably dull!), and I'm sure that other people have their stories. Perhaps something could be gained (in terms of learning strategies and approaches) if we find the space to discuss and share how we know what we know.

### Reflections on teaching design patterns

The final presentation of the day and final presentation of the workshop was by Carl Evans, who is a lecturer at Middlesex. Carl talked about his work on an MSc module and his experience of creating and presenting a module about software design patterns.

In computer science and software engineering, Design Patterns is one of my favourite topics. A couple of points that Carl made really resonated with me. One was that 'industry needs architects, not just programmers'. Another great point (and one that I totally subscribe to) is that there is an increasing expectation (from industry) that graduates can work with frameworks as well as know how to use programming languages. In some ways, this point connected up with Thomas's keynote.

Carl mentioned Sun/Oracle certifications, the use of layered architectures, and frameworks called [Spring](http://en.wikipedia.org/wiki/Spring_Framework) (Wikipedia) and [Hibernate](http://en.wikipedia.org/wiki/Hibernate_(Java)) (Wikipedia) that I have heard of, but have never used in anger. A quick look into these frameworks quickly shows that design patterns feature pretty prominently.

A really questions are: how do we best teach patterns, and where do we start? Is there a pattern about how to teach patterns? I noted down that a refresher about the object-oriented approach is useful, before taking students through different categories of patterns, such as object creation patterns, enterprise patterns, data access patterns, and compound patterns (I was writing everything down pretty quickly at this point, so I might not have managed to the nuances of everything that was said).

Carl also told us about a site called [Design Patterns Library](http://hillside.net/patterns) which I don't think I've seen before. One book that was referenced was [Head First Design Patterns](http://www.headfirstlabs.com/books/hfdp/) by O'Reilly. There seems to be a claim going around that says that these 'head first' books are based on 'neuroscience' (but I've yet to find out exactly what exactly this means: claims like that immediately make me sceptical!) Either way, anything that helps to make important technical concepts understandable is a good thing.

### Final thoughts

I don't know how many Psychology of Programming Work In Progress events I've been to, but it's been quite a few. This might have been my fourth or fifth. I have enjoyed every single one, and I enjoyed this one at Middlesex University too. It was well organised, friendly and thought provoking. The talks were really interesting, covering distance learning, errors, notation, robots, challenge of teaching object-oriented programming and a whole load of other subjects too. The great thing about these events is that you never know what you're going to get, which means that you never really know what you're going to learn (and this can be, invariably, a very good thing too).

From my perspective, the event helped to strengthen an opinion I have, which is that we need to figure out how to help students (and practicing programmers) how to best understand and work with software frameworks. This issue is not only a computing education issue, but also, significantly, a psychology of programming issue. The first subject that I studied when I discovered this subfield of computing (or of psychology, depending on your 'home' discipline) was the topic of program (or software) comprehension. It's clear from this short workshop that this continues to be (for me) an important topic.
