# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.(Может помочь метод translate из модуля string)
from operator import itemgetter

def counts(s):  
    s = s.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('-', '').lower().split()

    soreted_result = dict(sorted({i: s.count(i) for i in s}.items(), key=itemgetter(1)))
    last_ten_result = list(soreted_result.items())

    return last_ten_result[-10:]

str = 'This document gives coding conventions for the Python code comprising the standard library in the main Python distribution.\
 Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python.\
 This document and PEP 257 (Docstring Conventions) were adapted from Guido’s original Python Style Guide essay, with some additions from Barry’s style guide [2].\
 This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.\
 Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.\
 One of Guido’s key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability \
 of code and make it consistent across the wide spectrum of Python code. As PEP 20 says, “Readability counts”.\
 A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.\
 However, know when to be inconsistent sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best.\
 And don’t hesitate to ask!\
 In particular: do not break backwards compatibility just to comply with this PEP!\
 Some other good reasons to ignore a particular guideline:\
 When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.\
 To be consistent with surrounding code that also breaks it (maybe for historic reasons) although this is also an opportunity to clean up someone else’s mess (in true XP style).\
 Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.\
 When the code needs to remain compatible with older versions of Python that don’t support the feature recommended by the style guide.'

print(*counts(str)) 