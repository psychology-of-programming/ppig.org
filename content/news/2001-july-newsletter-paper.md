---
title: "Newsletter: July 2001 - Paper"
date: "2001-07-01"
---

# A proposal for yet another dimension - the case for Tunability
Chris Roast<br>
*Sheffield Hallam University, Sheffield, UK*<br>
c.r.roast@shu.ac.uk<br>
[www.shu.ac.uk/schools/cms/teaching/crr/]

## Introduction
Cognitive dimensions provide a range of concepts that have been used to assess and compare a variety of information artifacts. The cognitive dimensions are intended to provide a "language" capable of capturing features of human system interaction that are both common to a variety of systems and highly relevant to the effective use of systems. In this short paper we propose that the notion of "tunability" should serve as another dimension not evident in the established set.

Below we: introduce the concept; provide some examples of strong and weak cases; examine the relationship with effective use in context; and consider the dimension's relation with the established dimensions.

## Tunability - Definition & Elaboration
The ease of acquiring an effective operational model of a system.

More specifically, if a system is tunable it behaves and functions in a manner that supports the user in the recognition of internal/operational artifact characteristics. This is of specific benefit to users where knowledge of the internal characteristics of a system can enable the effective use of the system. Hence, to ask "how tunable is a system?" is to ask:

How easily can a correct and useful operational model be acquired by a user?

A system (notational or otherwise) is normally designed with a particular logical model in mind. In the case of interactive systems it is widely recommended that this model corresponds to the conceptual model of the user is likely to employ in its intended context of use. Users employ such a conceptual model so that the behaviours and functions of a system can be interpreted and effectively used. In this way the potential role of a system in likely tasks can be planned and predicted. The motivation for tunability comes from the following problems:

- it is normally the case that the conceptual model to which the system is designed differs from the operational model underlying it. As a consequence, when the context of use is beyond that originally envisaged/planned, operational features impinge upon the effectiveness of use.
- the users conceptual model can be in opposition to that envisaged or planned by the designer. In these circumstances the user encounters problems, and may resort to using an operational model.

As the name suggests, high tunability is intended to support the process of the user attuning to characteristics and behavioural details that are excluded from the conceptual model.

## Examples
There follow some examples of system use in which tunability (strong and weak) is evident.

### Web Tunability
While using the world wide web, users frequently encounter non-deterministic delays that disrupt their work in a variety of ways. The speed with which a particular page is displayed depends upon numerous factors, including: whether or not elements of the page are already cached; the performance of the communication network; the load upon the server(s) being accessed; and, the size and complexity of the required page. For the user to be able to predict and work with the system delays more effectively, one would look towards making the interface more tunable, making sure that operational characteristics (such as the server load) are evident to the user. In this way it is possible for the user to acquire a more accurate model of how to use the web more effectively, associating high server load with longer delays, in general. Similarly, if the user was able to tell if a particular page was not cached locally, then they may work around the likely delay of obtaining the page again (compared with cached pages). There is good evidence that users construct their own operational rationales for system delays, which suggest they attempt to attune to delays.

Were the user to be working with an intranet, then the tunability is less likely to be an issue, as it is more likely the network, servers and clients are designed for explicit, and relatively static, upper load.

### Declarative Languages
The implementation of declarative programming languages requires that their declarative expressions be given an operational interpretation. However, in terms of language design and motivation, the intended merit of declarative languages is that the operational details are dealt with behind the scenes and need not burden the language user. Whether this claim is valid is open to question, there is considerable evidence that users seek out specific types of operational account, valid or otherwise. In addition, when a language is being used for complex problems, questions of algorithm efficiency arise and these are normally assessed in terms of operational characteristics. Thus for both professional and educational declarative programming languages, there is a good argument that they should have high tunability. High tunability would ensure easy recognition of operational characteristics that both language learners and professional programmers can benefit from.

Prolog, as an example declarative language, has the merit of trying to combine operational and declarative model. However, the backtracking characteristics of the operational model and optimisations performed by compilers detract from tunability. Prolog can be contrasted with the language, Godel, where the operational interpretation of a program is formally independent of the written program.

By contrast the functional languages, such as Hope, normally have an explicit abstract operational model that defines pattern matching, reduction and strictness, and avoids backtracking. Although this probably ensures a level of tunability, programmers often rely upon particular programming styles to help with operational comprehension.

### Development
More generally, consider the task of developing a rapid prototype, the choice of language may be one to easily obtain illustrative functionality with limited robustness or efficiency (e.g. lisp). Once developed, the team is so pleased with the prototype it is not thrown away (as was planned) but it is to be refined and developed as a product quality program (i.e. robust & efficient). This development from prototype to product requires high tunability - which in this case corresponds to the language (and its toolset) supporting the analysis of program quality.

### Pascal Variable Names
A specific version of Pascal provides variable names of arbitrary length, though only the first eight characters are significant. In many cases this difference does not matter, however the difference does not encourage tunability to the real identity of a variable. This poor tunability is not a major problem in most programs, but it need not be a problem in any program.

### Mousing Over
While using a mouse pointing device, novice users find they run out of mouse mat, or even desk, and do not appreciate that the mouse can be lifted to disengage its movement from the system. In this case they are highly engaged with the illusion that moving the mouse means moving the pointer. A small investigation of what's under the mouse reveals the physical characteristics of the mouse and they are able to avoid running out of mouse space. This is a minor case of poor tunability - one can envisage a mouse design that is well suited to tuning of this sort.

For instance: The mouse puck is transparent, the mouse ball is textured and can be felt from the top of the mouse - users can easily see that they are in fact rolling a ball on a surface in order to direct the screen pointer.

### Email Client Design
While using a specific email client with a modem connection, opening a folder involves a progress indicator showing data transfer and when the folder data will be full available. This behaviour may be considered as supporting tunability, since it supports the development of an accurate operational model that allows the end user to work effectively. However, once a folder is open the client interface gives no indication of data transfers - as a consequence it is easy to believe that there are no transfers until the closing of the folder. Suprisingly, there is no apparent transfer when folder is closed.

When queried about this behaviour the designers revealed that the data flow maintained consistency between the client and server at all times, once a folder was open. The designers accepted that the imbalance in operational feedback was not necessarily of benefit to the end user and proposed visually flagging, whenever synchronization took place. The design improvement represents improved tunability.

### Theory

The notion of tunability depends upon two alternative models of an interactive system's behaviour that can be employed by users to their benefit. The first is the conceptual model embodied by the system, for a good system design users' tasks and requirements can be articulated in terms of this model. The other model is an operational model, this represents accurate details of a system that are not part of the conceptual model, and is based on concepts and terminology that are not primary elements of the intended domain of system use. Conventionally, the conceptual model is an abstraction of the operational model. The condition that brings tunability to the fore as a relevant concept is when the conceptual model becomes invalid - that is under some parameters/conditions the system behaviour appears to no longer fulfil its intended role in terms of the intend domain of use. Under this condition the conceptual model is of limited value to the user, irritating, confusing or misguiding them. For a system to be tunable, operational details are available and enable the user to adopt an alternative model that is valid under the conditions that invalidated the conceptual model.

In software engineering terms, it appears that tunability becomes relevant when a systems environment (and usage) dynamically influences the satisfaction of non-functional requirements.

### Tunability and Design
In many cases tunability makes demands upon overall system design as it conflicts with established design principles of hiding operational details (and transparency in the case of distributed systems).

### Operational Lockin
If a system is tunable, and a user recognises and adopts an operational model, there is a tendency to remain committed to the more accurate model and thus loose touch with the carefully designed conceptual model. For instance, once an operational model of, say, Prolog is established, it is hard to think back at the level of pure Horn clause logic. Similarly, WWW users who are aware of network latency may think of web links as communications as opposed to hyper-links.

## Pros. and Cons.
As a potential cognitive dimension it is important to point out that tunability is an attribute of interactive systems and the context of system use determines whether it is beneficial or not. The determinants of whether tunability is relevant are: how reliable a specific operational model may be over time? and whether the conceptual model will become significantly invalid?

### The Benefit of High Tunability
High tunability can support effective artifact use in a broad range of contexts by allowing the users to acquire and develop operational knowledge that they can use to their benefit.

E.g. once I've an accurate model of the local caching strategy of my browser, I can browse/work more effectively.

E.g. once I understand the strictness of a primitive function, I can improve the efficiency of my functional programs.

High tunability ideally ensures a form of graceful degradation of interaction. As opposed to a system not being usable beyond its intended context of use, tunability offers a level of support for interaction in such cases. Thus, in circumstances where the tasks supported by a system are more generic than the context in which it is intended to be used, it is appropriate to consider high tunability.

### The Benefit of Low Tunability
High tunability may encourage the adoption of operational knowledge by the user when it is not needed or of no benefit. For instance, if a user is using the system in a normative context, then detailed operational knowledge may represent an unnecessary mental burden.

E.g. - on a fast intranet, knowledge of a browser's caching policy is of little value.

In addition, an acquired detailed operational model may represent a specialisation of user skills that cannot be transferred or re-used effectively.

E.g. alternative browsers (and configurations) may be frequently encountered that make a specific operational model redundant (or incorrect).

E.g. when looking at the merits of a new Prolog compiler I have to examine whether or not my existing source code is exploiting compiler features that are also available in the new compiler.

## Relations with other dimensions
### Closeness of Mapping (negative)
Tunability appears to be akin to an exceptional form of closeness of mapping for circumstances where the user is focused upon details of the device, as opposed to the conceptual model of their task domain. Hence the concept is in opposition to the conventional notion of closeness of mapping.

### Abstraction Gradient (positive and negative)
Tunability is also similar to abstraction gradient, however its focus is upon the inverse relation. As with abstraction we can consider whether the transition from conceptual model to operational model encouraged by tunability has a "gradient" - the operational details required in order to effectively to cope with an invalid conceptual model.

A high tunability gradient would be one where one had to, say, attend a Prolog compiler construction course before being able to benefit from Prolog's operational reading. By contrast, a low tunability gradient may be where simple guidelines can be easily and incrementally adopted - such as, use tail-recursion, use first argument indexing, and so forth.

### Secondary Notation (negative)
Secondary notation of various sorts may interfere with tuning, since a user may attune to the information conveyed by a secondary notation. This is problematic for tuning, since the integrity of information conveyed by secondary notation is not guaranteed.

The status bar on a GUI web browser is a form of secondary notation. It is quite possible for the user to interpret the status bar messages indications of operational details, however page authors are to free control the status bar in any way they want.

### Visibility (negative)
If tuning is to be encouraged one of main mechanisms is likely to be the displaying of appropriate information. In terms of a system's conceptual display design, accommodating operational details may be seen as an unnecessary burden upon the display real estate. In addition, providing the appropriate cues for tuning without necessarily distracting from the primary conceptual design is likely to be problematic. The common solution to this is to have "validity aware" mechanisms that can employ visual aids for tuning when they are likely to be needed.

The Windows copy file behaviour provides an example. When copying a small file there is no special behaviour, however, when copying a large file an animation of a file's pages flying between folders is used to convey the underlying work involved (justifying the delay).

## Next
The notion of "tunability" has been discussed with various researchers interested in Cognitive Dimensions. One possible direction for the work is to re-cast it in a form that is not biased towards any particular abstraction orientation. The current description is reliant upon an abstraction/logical level being contrasted with an operational level. This specific ordering of different abstractions may not be necessary - however it is hard to identify specific compelling examples when the ordering is ignored.

## Key References

T. Green & A. Blackwell, **Design for usability using Cognitive Dimensions**, 1998, *HCI98, Tutorial notes (AM7)*

I. Ritchie & C. Roast, **Performance, Usability and the Web** *Proceedings of HICSS-43 the Hawaiian International Conference on System Science*, 2001, IEEE Computer Society

C. R. Roast, **Designing for Delay in Interactive Information Retrieval**, *Interacting with Computers*, 1998, pp. 87-104

C. Roast & I. Ritchie 2000, **Transparency in Time**, presented at *Which Architecture for What -- Towards Property-Based Selection of Software Architectures for Cooperative Systems*, Workshop on Software Architectures for Cooperative Systems, IFIP Working Group 2.7/13.4 in association with ACM CSCW, (December 2000)
