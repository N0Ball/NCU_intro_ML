from app.base import Base

class Duty(Base):

    def __init__(self):
        super().__init__(self)
        pass

    def run(self):

        from os import urandom
        import sys

        members = []

        while True:

            user_input = self.getInput('Name: ')

            if ' ' == user_input:
                continue 

            if 'q' == user_input:
                break 

            members.append(user_input)
        

        rand = int.from_bytes(urandom(10), sys.byteorder)%len(members)
        self.getOutput(f"今天是{members[rand]}倒垃圾")


if __name__ == '__main__':

    duty = Duty()
    duty.run()