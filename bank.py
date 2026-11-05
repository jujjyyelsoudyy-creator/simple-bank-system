pin = "1234"
balance = 1000
attempts = 3

print("--- Welcome to Main Bank ATM ---")

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin:
        print("Login successful!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Remaining attempts: {attempts}")

if attempts == 0:
    print("Card blocked due to too many failed attempts.")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            print(f"Your current balance is: {balance} EGP")
            
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited {amount} EGP. New balance: {balance} EGP")
            else:
                print("Invalid amount.")
                
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print(f"Successfully withdrew {amount} EGP. Remaining balance: {balance} EGP")
                
        elif choice == "4":
            print("Thank you for using Main Bank ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
