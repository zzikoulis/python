from operator import le


s = input("Παρακαλώ εισάγετε μια συμβολοσειρά και πατήστε Enter: ")
chardict = {}

def string_to_dictionary(s):
    chardict = {}

    for letter in s:
        if letter in chardict.keys():
            chardict[letter] += 1
        else:
            chardict[letter] = 1

    return chardict

print(f"\nΤο λεξικό συχνότητας εμφάνισης αριθμών είναι το: {string_to_dictionary(s)}")

