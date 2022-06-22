s = input("Παρακαλώ εισάγετε μια συμβολοσειρά και πατήστε enter: ")

print(f"Η συμβολοσειρά '{s}' που εισάγατε έχει {len(s)} συνολικά χαρακτήρες.")

s_even_positions = s[1::2]
print("Οι χαρακτήρες στις ζυγές θέσεις είναι οι:") 
for letter in s_even_positions:
    print(letter,end="   ")
