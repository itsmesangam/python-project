import random
small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "/", "?", "<", ">"]
random.shuffle(small_letters)
random.shuffle(capital_letters)
random.shuffle(numbers)
random.shuffle(special_characters)
all_characters = small_letters[0] + capital_letters[1] + numbers[0] + special_characters[3] + small_letters[2] + capital_letters[4] + numbers[5] + special_characters[6]

print(f"your password is {all_characters}")
