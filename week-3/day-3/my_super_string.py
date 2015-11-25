# receive string, store, implement reverse,
# hello -> olleh


class MySuperString:
    def __init__(self, word):
        self.word = word

    def reverse(self):
        # n = len(self.word)
        reversed = ''
        # for i in range(len(self.word)):
        #     reversed = self.word[i] + reversed
        # return reversed
        # for i in range(len(self.word)-1, -1, -1):
        #     reversed += self.word[i]
        # return reversed
        for chr in self.word:   # No index, character
            reversed = chr + reversed
        return reversed

    def count(self, character):
        counter = 0
        for char in self.word:
            if char == character:
                counter += 1
        return counter

    def snake_case(self):
        snake_word = ''
        for character in self.word:
            if character == ' ':
                snake_word = snake_word + '_'
            else:
                snake_word += character
        return snake_word.lower()

class MySuperNum():
    def average(self, list):
        counter = 0
        z = len(list)
        if z == 0:
            return print('Hey dude, it\'s not ok, please add me some number!')
        else:
            for n in list:
                counter = counter + n
            return counter / z
