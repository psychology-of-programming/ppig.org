---
title: "How A Data Structure’s Linearity Affects Programming and Code Comprehension: The Case of Recursion vs. Iteration"
authors: [Aviad Baron, Dror G. Feitelson]
abstract: "Iteration and recursion are two ways to traverse data structures. But when is one of them preferable over
the other? Some researchers argue that it is natural to use recursion to process recursively defined data
structures, such as linked lists and trees. In order to test this, we conducted two experiments of writing
and understanding code segments related to the processing of different data structures, with about 100
participants in each. The results showed that the way the structure is defined is not a significant factor
affecting the nature of the processing. On the other hand, the main factor that influenced the selected
approach was having a “linear mindset”, either due to the linearity of the structure (where data items
are arranged in a linear fashion, as in a list), or the linearity of the processing path (where data items
are visited in a linear manner, without branching). When we process a linear structure like a linked
list, the nature of its processing tends to be more iterative; a similar but weaker effect is obtained when
we process a linear path in a tree, for example when looking for an item in a binary search tree. But
when we need to understand code, recursion is problematic in the event that the processing is divided
both before and after the recursive call, and especially when the processing after the call (the so-called
“passive flow”) is non-trivial. These results provide insights into the cognitive factors which affect how
programmers interact with code. They can be explained by the observation that linear processing and
simple recursion (with a trivial or non-existent passive flow) are more suitable for the serial thinking of
humans."
publishedAt: ppig-2023
year: 2023
url_pdf: /files/2023-PPIG-34th-baron.pdf
paper_number: 6
---
