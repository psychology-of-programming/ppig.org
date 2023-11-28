---
title: "How Developers Extract Functions: An Experiment"
authors: [Alexey Braver, Dror G. Feitelson]
abstract: "Creating functions is at the center of writing computer programs. But there has been little empirical research
on how this is done and what are the considerations that developers use. We design an experiment
in which we can compare the decisions made by multiple developers under exactly the same conditions.
The experiment is based on taking existing production code, “flattening” it into a single monolithic function,
and then charging developers with the task of refactoring it to achieve a better design by extracting
functions. The results indicate that developers tend to extract functions based on structural cues, such as
if or try blocks. The extracted functions tend to be short, but not necessarily due to an explicit desire to
create short functions, but rather because of other considerations (like keeping logic cohesive or making
functions easily testable). Finally, while there are significant correlations between the refactorings
performed by different developers, there are also significant differences in the magnitude of refactoring
done. For example, the number of functions that were extracted was between 3 and 10, and the amount
of code extracted into functions ranged from 37% to 95%."
publishedAt: ppig-2023
year: 2023
url_pdf: /files/2023-PPIG-34th-braver.pdf
paper_number: 14
---
