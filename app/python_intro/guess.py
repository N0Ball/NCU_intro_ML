from app.base import Base

class Guess(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):
        from os import urandom
        rand = int(urandom(1).hex(), 16) % 4 + 1
        count = 1
        
        while True if int(self.getInput("Guess number: ")) != rand else False:
            count += 1

        self.getOutput(f'Time guessed: {count}\nRight answer: {rand}')


if __name__ == '__main__':

    guess = Guess()
    guess.run()