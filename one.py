balance = 10000
history = []
pin = 1234
attempts = 0


def save():
    f = open("atm.txt", "w")
    f.write(str(balance) + "\n")
    f.write(str(pin) + "\n")  
    for h in history:
        f.write(h + "\n")
    f.close()

def data():
    global balance, pin
    try:
        f = open("atm.txt", "r")
        balance = int(f.readline())
        pin = int(f.readline()) 
        for line in f:
            history.append(line.strip())
        f.close()
    except:
        save()

def Check_Balance():
    print("Current Balance:", balance)

def Deposit():
    global balance
    try:
        amount = int(input("Amount: "))
        if amount <= 0:
            print("Invalid amount.")
        else:
            balance = balance + amount
            history.append("Deposit " + str(amount))
            save()
            print("Deposit successful. New Balance:", balance)
    except:
        print("Invalid amount.")

def Withdraw():
    global balance
    try:
        amount = int(input("Amount: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - amount
            history.append("Withdraw " + str(amount) + " | balance: " + str(balance) )
            save()
            print("Withdrawal successful. New Balance:", balance)
    except:
        print("Invalid amount.Please enter numbers only.")

def Mini_Statement():
    if len(history) == 0:
        print("No transactions yet.")
    else:
        for h in history:
            print(h)

# pin verification

while attempts < 3:
    entered_pin = int(input("Enter PIN: "))
    if pin == entered_pin:
        print("Login successful.")
        break
    else:
        attempts += 1
        remaining_attempts = 3 - attempts
        print("Invalid PIN.")
        if remaining_attempts > 0:
            print("Attempts left:", remaining_attempts)
        else:
            print("Account locked. Exiting...")

if attempts == 3:
    pass
else:
    while True:
        print(" 1. Check Balance")
        print(" 2. Deposit")
        print(" 3. Withdraw")
        print(" 4. Mini Statement")
        print(" 5. Exit")

        choice = int(input("Menu option:"))

        if choice == 1:
            Check_Balance()
        elif choice == 2:
            Deposit()
        elif choice == 3:
            Withdraw()
        elif choice == 4:
            Mini_Statement()
        elif choice == 5:
            print("Thank you. Exiting...")
            break
        else:
            print("Invalid choice.")