s = input("Παρακαλώ εισάγετε μια συμβολοσειρά και πατήστε enter: ")

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

def check_string_number(s, k):
    if k >= len(s):
        return s
    return s[k:]

print(check_string_number(s,k))
