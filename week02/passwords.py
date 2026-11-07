
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if case_sensitive == False:
                if word.lower == file_word.lower():
                    return True
            else:
                if word == file_word:
                    return True
    return False
def word_has_character(word, character_list):
    for w in word:
        if w in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity +=1
    if word_has_character(word, UPPER):
        complexity+=1
    if word_has_character(word, DIGITS):
        complexity +=1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity

    return strength
# OPTIONAL FEATURE: Password improvement tips
# This function gives users suggestions for creating
# stronger passwords based on their password's strength.

def password_tips(strength):
    if strength == 0:
        print("Tip: Avoid dictionary words and commonly used passwords.")

    elif strength == 1:
        print("Tip: Use at least 10 characters in your password.")

    elif strength == 2 or strength == 3:
        print("Tip: Try adding uppercase letters, numbers, and special symbols.")

    elif strength == 4:
        print("Tip: Good password! Consider making it longer.")

    else:
        print("Excellent! Your password received the highest strength score.")
def main():
    while True:
        password = input("Enter password: ")
        if password != "q" and password != "Q":
            strength = password_strength(password)
            print(f"You entered: {password}")
            print(f"Password strength: {strength}")
            # OPTIONAL FEATURE: Show password improvement tips
            password_tips(strength)
        else:
            break
if __name__ == "__main__":
    main()