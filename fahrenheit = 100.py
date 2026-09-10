person = {
    "first_name": input("Enter your first name: "),
    "last_name": input("Enter your last name: "),
    "age": int(input("Enter age: "))
}

print(f"{person['first_name']} {person['last_name']} is {person['age']} years old.")

print("-------Account Created-------")

#Account verification

if input("Re-enter your name: ") == f"{person['first_name']} {person['last_name']}":
    print("Account verified")

else:
    print("Account verification failed. Please try again.")

    for i in range(3):
        if input("Re-enter your name: ") == f"{person['first_name']} {person['last_name']}":
            print("Account verified")
            break
        else:
            print("Account verification failed. Please try again.")