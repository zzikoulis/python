s = input("Παρακαλώ εισάγετε μια συμβολοσειρά και πατήστε enter: ")

isPalindrome = " "
for i in range(0, len(s) // 2):
    if s[i] != s[len(s) -1 - i]:
        isPalindrome = " δεν "
        break

print("Η συμβολοσειρά{}είναι παλίνδρομη.".format(isPalindrome))