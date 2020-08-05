import nltk

grammar = nltk.CFG.fromstring("""
    L -> 
""")

parser = nltk.ChartParser(grammar)

sentence = input("Python Line: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()
        break
except ValueError:
    print("No parse tree possible.")