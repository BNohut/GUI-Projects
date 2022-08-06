import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_of_all = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_of_all)


is_on = True
while is_on:
    user_input = input("Whats the word?: \n").upper()
    try:
        new_list = [dict_of_all[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_on = False
        print(new_list)
