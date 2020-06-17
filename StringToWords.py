"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


# SOLUTION
def original_words(words, s):
    result = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if s[i:j] in words:
                result = add_span(result, (i, j))

    if len(result) == 0:
        return
    if len(result) == 1:
        return [s] if len(s) == result[0][1] else None
    result = [s[span[0]:span[1]] for span in result]
    result_string = ""
    for word in result:
        result_string += word
    if result_string == s:
        return result
    return


def add_span(result, span):
    if len(result) == 0:
        return [span]
    if result[-1][0] == span[0]:
        result[-1] = span
    elif result[-1][1] == span[0]:
        result.append(span)
    return result


words = {"quick", "the", "brown", "fox"}
s = "thequickbrownfox"
print(original_words(words, s))

words = {"bedbathandbeyond", "and", "bath"}
s = "bedbathandbeyond"
print(original_words(words, s))


