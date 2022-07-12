while True:
    s = input('Παρακαλώ εισάγετε μια σειρά ακέραιων αριθμών που χωρίζονται μεταξύ τους με τον χαρακτήρα "," και πατήστε enter: ')

    numbers = s.split(",")

    try:
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο ΑΚΕΡΑΙΟΥΣ ΑΡΙΘΜΟΥΣ σε έγκυρη μορφή.\n")

while True:
    try:
        i = int(input("Παρακαλώ εισάγετε έναν θετικό ακέραιο αριθμό (> 0): "))
        if i <= 0:
            print("Παρακαλώ εισάγετε θετικό αριθμό και όχι αρνητικό ή μηδέν!")
            print()
            continue
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο θετικό ακεραίο ΑΡΙΘΜΟ και όχι χαρακτήρες!")
        print()


print(f"Η λίστα που εισάγατε είναι η: {numbers}", end="\n\n")

for j in range(1, i + 1):
    exponentiation = [num**j for num in numbers]
    print(f"Η λίστα υψωμένη στην δύναμη: {j} είναι {exponentiation}")
