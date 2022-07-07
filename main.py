from wordlist import movie
def try_again(retry):
    if retry == "Y" or retry == "y" or retry == "Yes" or retry =="yes" or retry == "YES":
        playgame()
    elif retry == "N" or retry == "n" or retry == "No" or retry == "no" or retry == "NO":
        exit()

def change_current_word_state(selected_movie,guessed_char,current_word_state):
    modified_word_state = ''
    for i in range(len(selected_movie)):
            if current_word_state[i] == '_' and selected_movie[i] == guessed_char: 
                modified_word_state += guessed_char
            else:
                modified_word_state+=current_word_state[i]
    return modified_word_state

def chk_for_input_char_in_word(guessed_char,current_word_state,chances_remaining,selected_movie):
    if guessed_char in selected_movie:
        current_word_state = change_current_word_state(selected_movie,guessed_char,current_word_state)
    else:
        chances_remaining -= 1
    return current_word_state, chances_remaining
    
def print_current_state_of_game(current_word_state,chances_remaining):
    #it will print current status of the game
    print("Current Word Status: ",end= ' ')
    for i in current_word_state:
        print(i,end = ' ')
        #prints game's current status
    print('\tChances_Remaining:',chances_remaining)
    #prints attempts remaining
def playgame(attempts = 5):
    # it will start the game and contains main logic of the game and default attempts are given as 3
    selected_movie = movie.upper()
    # it will store imported movie name in a variable
    if len(selected_movie) > 10 and  len(selected_movie) <= 15:
        attempts = attempts + 1
    elif len(selected_movie) > 15:
        attempts = attempts + 2
    elif len(selected_movie) <= 9 and len(selected_movie) >=6:
        attempts = attempts - 2
    elif len(selected_movie) < 6:
        attempts = attempts - 3
    else:
        pass
    current_word_state = ''
    for characters in movie:
        if characters  == ' ' or characters == 'a' or characters == 'i' or characters == 'e' or characters == 'o' or characters == 'u':
            current_word_state+= characters.upper()
        else:
            current_word_state+= '_'
    chances_remaining = attempts
    print_current_state_of_game(current_word_state,chances_remaining)
    while True:
        guessed_char = input('Guess The Character: ').upper()
        current_word_state,chances_remaining = chk_for_input_char_in_word(guessed_char,current_word_state,chances_remaining,selected_movie)
        print_current_state_of_game(current_word_state,chances_remaining)
        if chances_remaining == 0:
            print("\nGame Over! You Lost. The Movie Was {}. ".format(selected_movie))
            retry = input("Would You Like to Start Again? Press Y/N : ")
            try_again(retry)
        elif "_" not in current_word_state:
            print("\nCongratulations! You Guessed The Movie. ")
            retry = input("Would You Like to Start Again? Press Y/N : ")
            try_again(retry)

if __name__ == '__main__':
    playgame()
