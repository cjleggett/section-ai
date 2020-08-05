import nltk
import sys
import operator

"""
Note: Even though this is is labeled as a solution, it is
still a work in progress. There are several bugs I still need
to work through, and if you have any suggestions please make 
a pull request!
"""

# VP "=" EXP | "print(" EXP ")"

grammar = nltk.CFG.fromstring("""
    L -> EXP
    EXP -> EXP OP EXP | N

    VP -> "u" | "v" | "w" | "x" | "y" | "z"
    OP -> "+" | "-" | "/" | "*" | "//" | "**" | "%"
    N -> "1" | "2" | "3" | "4" | "5" | "6" | "7"
    N -> "8" | "9" | "0"
""")


parser = nltk.ChartParser(grammar)

functions = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "//": operator.floordiv,
    "*": operator.mul,
    "**": operator.pow,
    "%": operator.mod,
}

def evaluate_line(tree):
    if tree.label() == "N":
        return int(tree.leaves()[0])
    elif tree.label() == "OP":
        return functions[tree.leaves()[0]]
    elif tree.label() == "L":
        return evaluate_line(list(tree.subtrees())[1])
    else:
        subs = list(tree.subtrees())[1:]
        already_done = []
        exps = []
        while len(subs) > 0:
            sub = subs.pop(0)
            if sub not in already_done:
                exps.append(evaluate_line(sub))
                already_done += [s for s in list(sub.subtrees())]
        if len(exps) == 1:
            return exps[0]
        return exps[1](exps[0], exps[2])

while True:
    sentence = input(">>> ").split()
    final_tree = None
    try:
        for tree in parser.parse(sentence):
            # tree.pretty_print()
            # tree.draw()
            final_tree = tree
            break
    except ValueError:
        print("Invalid Syntax")

    print(evaluate_line(final_tree))