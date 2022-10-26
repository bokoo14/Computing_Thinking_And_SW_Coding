import sys
input=sys.stdin.readline

class Duck:
    def say(self):
        print("꽥꽥")
class Chicken:
    def say(self):
        print("꼬끼오")

def say(animal):
    animal.say()


say(Duck())
say(Chicken())

