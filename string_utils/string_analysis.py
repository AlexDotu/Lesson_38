
def count_vowels(s):
    vowels = []
    for letter in s:
        if letter == 'e' or letter == 'E':
            vowels.append(letter)
        elif letter == 'y' or letter == 'Y':
            vowels.append(letter)
        elif letter == 'u' or letter == 'U':
            vowels.append(letter)
        elif letter == 'i' or letter == 'I':
            vowels.append(letter)
        elif letter == 'o' or letter == 'O':
            vowels.append(letter)
        elif letter == 'a' or letter == 'A':
            vowels.append(letter)
    vowels_for_return = len(vowels)
    print(f"The number of the vowels letters is: {vowels_for_return}")
    return vowels_for_return


def count_char(s):

    total_char_count = len(s)
    print(f"The number of the signs in string is: {total_char_count}")

