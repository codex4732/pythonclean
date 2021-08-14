import Infrastructure as I

drink = I.Services.DrinkService.getDrink()
mood = I.Services.MoodService.getMood()


print('I want to drink {0}'.format(drink)) if (mood == 'Happy') else print('I am not thirsty because I am {0}'.format(mood))
