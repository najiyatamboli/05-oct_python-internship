age = int(input("Enter your age:"))

if age < 0 or age > 120 :
    print("Invalid age")
elif age >= 18:
    print("valid age")
    print("Eligible forvoting")

else:
    print("valid age")
    print("Not eligible for voting ")