PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as letters_file:
    letters = letters_file.readlines()

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

    new_letter = ""
    for letter in letters:
        new_letter += letter

    for name in names:
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as fl:
            final_letter = new_letter.replace(PLACEHOLDER, name)
            fl.write(final_letter)

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() #strip is to get rid of the \n in between strs
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
