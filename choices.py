import constants as c

def get_choice(choices:list) -> int:
    options_menu_choices = ["Option " + str(x) for x in range(1,len(choices)+1)]
    choices_as_string = c.NEW_LINE.join([f'{x}. {y}' for x, y in zip(options_menu_choices, choices)])
    while True:
        print(choices_as_string)
        try:
            chosen_index = int(input("Please make a choice: "))
            if chosen_index > len(choices) or chosen_index <= 0:
                print("Oops!  That was not a valid choice. Try again...")
            else:
                break
        except ValueError:
            print("Oops!  That was not a valid choice. Try again...")
    return chosen_index-1