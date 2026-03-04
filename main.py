
balance = 500000


while True:
    print('ATM machine logic')
    print('1) check your balance')
    print("2) Withdraw an amount")
    print("3) Deposit an Amount")
    print("4) Exit Machine")

    choice = input("Make your choice: ")

    match choice:
        # Check your Atm balance
        case "1":
            print(f"Your ATM balance is {balance}")
        # Withdraw an amount from the Atm
        case "2":
            amount = int(input("Enter an amount you wish to withdraw: "))
            if amount > balance:
                print("Insufficient balance to proceed")
            elif amount<=0:
                print("Invalid withdrawal amount")
            else:
                balance -= amount
                print(f"Successful withdrawal of {amount}")
                print(f"New balance is {balance}")
        # Deposit an amount in the Atm machine
        case "3":
            amount = int(input("Enter your deposit amount "))
            if amount > 0:
                balance+=amount
                print(f"{amount} has been successfully added to your account")
                print(f"Your New Balance is {balance}")
            else:
                print("Your Deposit amount is not valid, try again")
        # Exit the Atm Machine
        case "4":
            print("Thank you for trusting us, see you later")
            break
        # Wrong user choice logic
        case _:
            print("Not a valid choice, please try again")