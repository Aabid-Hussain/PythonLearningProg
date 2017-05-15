class alphabet12:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index +=1
        return self.letters[self.index]

alpha = alphabet12()

for letter in alpha:
    print(letter)

