import Interfaces as I

drink = I.Services.DrinkService.getDrink()
mood = I.Services.MoodService.getMood()


print('I want to drink {0} because I am {1}'.format(drink, mood)) if (mood == 'Happy') else print('I am not thirsty because I am {0}'.format(mood))
