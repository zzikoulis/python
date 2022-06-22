while True:
    try:
        a = float(input("Παρακαλώ εισάγετε έναν αριθμό: "))
        b = float(input("Παρακαλώ εισάγετε έναν ακόμα αριθμό: "))
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο ΑΡΙΘΜΟΥΣ και όχι χαρακτήρες!")
        print()

print(f"To {a} + {b} είναι: {a+b}")
print(f"To {a} - {b} είναι: {a-b}")
print(f"To {a} * {b} είναι: {a*b}")
try:
    print(f"To {a} / {b} είναι: {a/b:.2}")
except ZeroDivisionError:
    print(f"To {a} / {b} δεν μπορεί να υπολογιστεί λόγω μηδενικού διαιρέτη.")
try:
    print(f"To {a} // {b} είναι: {a//b:.2}")
except ZeroDivisionError:
    print(f"To {a} // {b} δεν μπορεί να υπολογιστεί λόγω μηδενικού διαιρέτη.")
try:
    print(f"To {a} % {b} είναι: {a%b}")
except ZeroDivisionError:
    print(f"To {a} % {b} δεν μπορεί να υπολογιστεί λόγω μηδενικού διαιρέτη.")