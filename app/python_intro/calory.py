from app.base import Base

class Calory(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):

        print('')
        date = self.getInput('Date: ')

        calories = list(map(lambda x: int(x), self.getInput("Calories: ").split(',')))

        self.getOutput(f"{date}日期的卡路里總和是{sum(calories)}")

if __name__ == '__main__':

    calory = Calory()
    calory.run()

