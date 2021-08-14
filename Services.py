import random

class MoodService:
    def getMood():
        moodlist = ['Happy','Sad','Stressed', 'Joyeous']
        return (random.choice(moodlist))

class DrinkService:
    def getDrink():
        drinkList = ['Tea','Coffee', 'Water']
        return (random.choice(drinkList))