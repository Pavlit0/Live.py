def welcome(name):
    print("Hello", name ,"And welcome to the World of Games (WoG). \nHere you can find many cool games to play.")

def load_game():
    while True:
                game_to_play = int(input("""    Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"""))
        # except ValueError:
        #     print("Please enter a number")
        # else:
          if game_to_play not in range(1,4):
                print("Please enter game number between 1-3")
                return;


        #         if game_to_play == 1:
        #             memory_game()
        #         elif game_to_play == 2:
        #             guess_game()
        #         elif game_to_play == 3:
        #             currency_roulette()





