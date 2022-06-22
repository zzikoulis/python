while True:
    s = input('Παρακαλώ εισάγετε μια σειρά ακέραιων αριθμών που χωρίζονται μεταξύ τους με με το χαρακτήρα "," και πατήστε enter: ')

    numbers = s.split(",")

    try:
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο ΑΚΕΡΑΙΟΥΣ ΑΡΙΘΜΟΥΣ σε έγκυρη μορφή.\n")

while True:
    try:
        k = int(input("Παρακαλώ εισάγετε έναν θετικό ακέραιο αριθμό: "))
        if k <= 0:
            print("Παρακαλώ εισάγετε θετικό αριθμό και όχι αρνητικό ή μηδέν!")
            print()
            continue
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο θετικό ακεραίο ΑΡΙΘΜΟ και όχι χαρακτήρες!")
        print()

print(f"Οι αριθμοί της σειράς που διαιρούνται ακριβώς με τον αριθμό {k} είναι οι:")

for number in numbers:
    if not number % k:
        print(number, end="   ")