import nltk
from nltk.parse.generate import generate

grammar = nltk.CFG.fromstring("""
    L -> VP "=" EXP | "print(" EXP ")"
    EXP -> EXP OP EXP | N


    VP -> "u" | "v" | "w" | "x" | "y" | "z"
    OP -> "+" | "-" | "/" | "*" | "//" | "**" | "%"
    N -> "1" | "2" | "3" | "4" | "5" | "6" | "7"
    N -> "8" | "9" | "0"
""")

parser = nltk.ChartParser(grammar)

lines = generate(grammar, n=1000, depth=4)

for line in lines:
    print(' '.join(line))

# sentence = input("Python Line: ").split()
# try:
#     for tree in parser.parse(sentence):
#         tree.pretty_print()
#         tree.draw()
#         break
# except ValueError:
#     print("No parse tree possible.")