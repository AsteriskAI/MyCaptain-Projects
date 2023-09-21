
def most_frequent(string):
    letter_count = {}

    nospace = string.replace(" ","").lower()

    for char in nospace:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, frequency in sorted_letter_count:
        print(f"{letter} = {frequency}", end=" ")

string = input("Enter a string: ")
most_frequent(string)