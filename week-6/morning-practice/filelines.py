class FileLine:
    def __init__(self, file):
        myfile = open(file)
        self.mytext = myfile.read().split('\n')
        myfile.close()

    def get_last(self):
        return self.get_nth(-1)

    def get_first(self):
        return self.get_nth(1)

    def get_nth(self, row):
        return self.mytext[row-1]


lines = FileLine('alma.txt')
print(lines.get_first())
print(lines.get_last())
print(lines.get_nth(2))
