from app.base import Base

class UserInput(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):

        while True:

            oper = self.getInput("Continue? (Yes/No): ")

            if oper == 'Yes':
                self.getOutput("Continue")
                continue

            if oper == "No":
                self.getOutput("End")
                break

            self.getOutput("Please type again")


if __name__ == '__main__':

    userInput = UserInput()
    userInput.run()