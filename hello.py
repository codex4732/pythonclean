import Infrastructure as I

drink = I.Services.DrinkService.getDrink()
mood = I.Services.MoodService.getMood()

if (mood == 'happy'):
    print('I want to drink {0}'.format(drink))
else:
    print('I am not thirsty because I am {0}'.format(mood))
