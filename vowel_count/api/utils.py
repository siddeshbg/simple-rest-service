
VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def vowel_count(word):
    vowels = list()
    for letter in list(word):
        if letter in VOWELS:
            vowels.append(letter)

    return len(vowels)


if __name__ == '__main__':
    v = vowel_count("SIddesh")
    print(v)