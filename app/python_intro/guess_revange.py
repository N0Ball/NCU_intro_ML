from app.base import Base

class Guess_revange(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):
        from os import urandom
        rand = int(urandom(1).hex(), 16) % 4 + 1
        count = 1
        
        while True:
            user_input = self.getInput("Guess number: ")
            
            if not user_input.isdigit():
                self.getOutput("Wrong input, please type again")
                continue

            user_input = int(user_input)

            if user_input == rand:
                break

            self.getOutput('Too big') if user_input > rand else self.getOutput('Too small')

            count += 1

        self.getOutput(f'Time guessed: {count}\nRight answer: {rand}')


if __name__ == '__main__':

    guess_revange = Guess_revange()
    guess_revange.run()