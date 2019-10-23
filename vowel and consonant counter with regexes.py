import re

def main():
    userInput = input("Please input a string: ")

    vowels = r'[aeiou]'
    consonants = r'[^aeiou]'
    vowelCounter = 0
    consonantCounter = 0

    for letter in userInput:
        if re.search(vowels, letter):
            vowelCounter += 1
        elif re.search(consonants, letter):
            consonantCounter += 1

    print("There are {} vowels in this string.".format(vowelCounter))
    print("There are {} consonants in this string.".format(consonantCounter))

if __name__ == '__main__':
    main()