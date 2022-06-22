while True:
    s = input("Παρακαλώ εισάγετε μια σειρά ακέραιων αριθμών που χωρίζονται μεταξύ τους με ένα κενό διάστημα και πατήστε enter: ")

    numbers = s.split(" ")

    try:
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο ΑΚΕΡΑΙΟΥΣ ΑΡΙΘΜΟΥΣ.\n")

def check_number_series(numbers):
    return numbers[0] == numbers[len(numbers) - 1]

if check_number_series(numbers):
    print("Δεκτή")
else:
    print("Απαράδεκτη")