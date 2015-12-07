import re

def filereader():
    with open("proba.txt", "r") as inp:
        text = inp.read()
        v = re.sub(r'a', 'b', text)
        print(v)

filereader()
