import random
import requests
import time
import starwars as sw

your_score = 0
rival_score = 0

print('Welcome to Top Trumps!')
time.sleep(1)
# Store the player's name for the high score file
name = input('What is your name? ')
round_type = input("Which Card Deck would you like to use? (pokemon or starwars) ")


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'health': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defence': pokemon['stats'][2]['base_stat']
    }


def random_starwars():
    player_card_id = random.randint(1, 83)  # Random Card ID given to player
    while (player_card_id == 17):  # 17 does not have any content
        player_card_id = random.randint(1, 83)  # Random Card ID given to player
    print("Getting your card ready...")  # The Star Wars APi is slower than the others
    player_card = sw.get_character_stats(player_card_id)
    return player_card


def pokemon_round():
    print('New Round! \n')
    won_round = False
    my_pokemon = random_pokemon()
    print('{} you have been given {}'.format(name, my_pokemon['name']))
    print(
        "Player Top Trumpz Card Stats are: \nName: {}, ID: {}, Height {}m, Weight {}Kg, Health {}, attack {}, defence {}\n".format(
            my_pokemon["name"], my_pokemon["id"], (my_pokemon["height"] / 10), (my_pokemon["weight"] / 10),
            (my_pokemon["health"]),
            my_pokemon["attack"], my_pokemon["defence"]))
    stat_choice = input('Which stat would you like to use? (id, height, weight, health, attack, defence) ')
    print(stat_choice)

    opponent_pokemon = random_pokemon()
    if my_pokemon == opponent_pokemon:
        opponent_pokemon = random_pokemon()
    time.sleep(2)
    print('Your rival has been given {}'.format((opponent_pokemon['name']).capitalize()))
    time.sleep(2)
    my_stat = my_pokemon[stat_choice]
    print('Your {} stat is {}'.format(my_pokemon['name'], my_stat))
    opponent_stat = opponent_pokemon[stat_choice]
    time.sleep(2)
    print("Your rival's {} stat is {} \n".format(opponent_pokemon['name'], opponent_stat))
    time.sleep(2)

    if my_stat > opponent_stat:
        print('You win!')
        # your_score = your_score + 1
        won_round = True
        # rival_score = rival_score + 0
    elif my_stat < opponent_stat:
        print('You lose!')
        # your_score = your_score + 0
        # rival_score = rival_score + 1
    else:
        print('Its a draw!')

    return won_round


def starwars_round():
    print('New Round! \n')
    won_round = False
    my_character = random_starwars()
    print('{} you have been given {}'.format(name, my_character['name']))
    print("Player Top Trumpz Card Stats are: \nName: {}, ID: {}, Height {}m, Weight {}Kg, No. of films {}\n".format(
        my_character["name"], my_character["id"], my_character["height"], my_character["weight"],
        my_character["films"]))
    stat_choice = input('Which stat would you like to use? (id, height, weight, films) ')
    print(stat_choice)

    opponent_character = random_starwars()
    if my_character == opponent_character:
        opponent_pokemon = random_pokemon()
    time.sleep(2)
    print('Your rival has been given {}'.format(opponent_character['name']))
    time.sleep(2)
    my_stat = my_character[stat_choice]
    print('Your {} stat is {}'.format(my_character['name'], my_stat))
    opponent_stat = opponent_character[stat_choice]
    time.sleep(2)
    print("Your rival's {} stat is {} \n".format(opponent_character['name'], opponent_stat))
    time.sleep(2)

    if my_stat > opponent_stat:
        print('You win!')
        # your_score = your_score + 1
        won_round = True
        # rival_score = rival_score + 0
    elif my_stat < opponent_stat:
        print('You lose!')
        # your_score = your_score + 0
        # rival_score = rival_score + 1
    else:
        print('Its a draw!')

    return won_round


rounds_to_win = 2  # 3
while (your_score < rounds_to_win) and (rival_score < rounds_to_win):
    if round_type == 'pokemon':
        if (pokemon_round() == True):  # If the player won
            your_score += 1  # Increase their score
        else:
            rival_score = +1
    else:
        if (starwars_round() == True):  # If the player won
            your_score += 1  # Increase their score
        else:
            rival_score += 1

        if my_stat > opponent_stat:
            print('You win!')
            # your_score = your_score + 1
            your_score += 1
            # rival_score = rival_score + 0
        elif my_stat < opponent_stat:
            print('You lose!')
            # your_score = your_score + 0
            # rival_score = rival_score + 1
            rival_score += 1
        else:
            print('Its a draw!')

        print('{} your score is {}'.format(name, your_score))
        print("Your rival's score is {} \n".format(rival_score))
        # print('Next Round! \n')

highscore_data = ('{}s total score is {}'.format(name, your_score))
print(highscore_data)

# Is there a way we can have something like "you've won the game!" here?
if your_score >= rounds_to_win:
    print("you've won the game!")

with open('highscore.txt', 'a') as highscore_file:
    highscore_data = ('{}s total score is {}\n'.format(name, your_score))
    highscore_file.write(highscore_data)