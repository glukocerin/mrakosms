class MySuperString:
    def __init__(self, word):
        self.word = word

    def count(self, char):
        counter = 0
        for chr in self.word:
            if char == chr:
                counter += 1
        return counter
