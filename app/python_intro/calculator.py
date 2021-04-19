from app.base import Base

class Calculator(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):

        first_number = self.getInput("First Number: ")
        if not first_number.isdigit():
            self.getOutput("number not digit, please type again")
            self.run(self)
            return

        operation = self.getInput("Operation: ")
        if operation not in "+ - * / % // **".split():
            self.getOutput("operation not permitted, please type again")
            self.run(self)
            return

        second_number = self.getInput("Second Number: ")
        if not second_number.isdigit():
            self.getOutput("number not digit, please type again")
            self.run(self)
            return


        super().getOutput(eval(first_number + operation + second_number))


if __name__ == '__main__':

    calculator = Calculator()
    calculator.run()