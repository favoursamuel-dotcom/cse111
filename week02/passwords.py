def word_in_file(word, filename, case_sensitive):
    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(password, min_length=10, strong_length=16):
    pass

def main():
    while True:
        password = input("Enter password: ")
        if password != "q" and password != "Q":
            strength = password_strength(password)
            print(f"You entered: {password}")
            print(f"Password strength: {strength}")
        else:
            break
main()