file_dictionary = {"different_words": 0, "biggest_length_word" : ""}

for line in open ('alice_in_wonderland.txt', encoding="utf8"):
    s = "".join(char for char in line if char in "abcdefghijklmnopqrstuvwxyzABCDEFHGIJKLMNOPQRSTUVWXYZ—- ")
    s = s.replace("—", " ")
    s = s.replace("-", " ")
    
    for word in s.split():
        if word not in file_dictionary.keys():
            file_dictionary[word] = 1
            file_dictionary["different_words"] += 1
            if len(word) > len(file_dictionary["biggest_length_word"]):
                file_dictionary["biggest_length_word"] = word
        else:
            file_dictionary[word] += 1

print("Για το αρχείο 'Alice in Wonderland' έχουμε:\n")
print(f"Το κείμενο έχει {file_dictionary['different_words']} διαφορετικές λέξεις.")
print(f"Η λέξη Alice εμφανίζεται {file_dictionary['Alice']} φορές.")
print(f"Η λέξη με το μεγαλύτερο μήκος στο κείμενο({len(file_dictionary['biggest_length_word'])} χαρακτήρες) είναι η: {file_dictionary['biggest_length_word']}")



