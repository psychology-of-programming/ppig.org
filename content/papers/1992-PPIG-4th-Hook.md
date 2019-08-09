---
title: "Possible Extensions to the Byrd Box tracer aimed at Experts"
authors: [Kristina Höök, Annika Wærn, Helen Pain]
abstract: "We argue for the need of a study on how experienced users make use of the Prolog tracing facilities. We know that a lot of time is spent tracing programs during the programming development phase and that often the first attempt to find a bug fails. We divide Prolog bugs into conceptual bugs, related to the problem being solved rather than to the Prolog programming language, and mistakes, related mainly to the syntax of Prolog. We argue that most Prolog bugs arise from failed unifications, and that a lot of time is spent skipping through the trace facility. Experts also spend a lot of time writing their own debuggers in order to find their conceptual bugs, since they find the tracing facilities inadequate for this purpose.
<br>
Three changes to the Byrd Box trace are suggested in order to enhance the understanding of unification and help experts to find unification bugs quicker. The first change, is to use some techniques from abstract interpretation to make recursive calls condensed into a few lines in the trace. The second idea, is to allow for conditional skipping, where the expert can ask to see a goal before or after a certain goal has unified or failed ( can also be seen in the TPM [Eisenstadt and Brayshaw 88]). The third idea, is to allow the expert to only see calls that affects a certain datastructure that is being built or decomposed. The last change to the tracer might possibly allow the expert to find some of her conceptual bugs as well."
publishedAt: "ppig-1992"
year: 1992
url_pdf: "files/1992-PPIG-4th-Hook.pdf"
---
