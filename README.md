# ATM Management System

A simple command-line ATM simulator written in **Python 3** (PS No. 95). Users log in with a PIN and can check balance, deposit, withdraw and view a mini statement. Balance, PIN and history are saved in `atm.txt`, so data persists between runs.

## Features

- PIN login with 3 attempts; account locks after 3 wrong PINs
- Check balance, deposit and withdraw
- Mini statement showing transaction history
- Input validation: rejects text, zero and negative amounts
- Insufficient funds protection (balance never goes negative)
- Data saved to file after every transaction
- Menu repeats in a loop until the user chooses Exit

## Requirements

- Python 3
- No external libraries (standard library only)

## Menu

```
1. Check Balance
2. Deposit
3. Withdraw
4. Mini Statement
5. Exit
```

## Project Files

| File | Purpose |
|------|---------|
| `one.py` | Main program source code |
| `atm.txt` | Stores balance, PIN and transaction history |

## Functions

| Function | Description |
|----------|-------------|
| `data()` | Loads balance, PIN and history from file (defaults if not found) |
| `save()` | Saves balance, PIN and history to file |
| `Deposit()` | Adds amount to balance |
| `Withdraw()` | Subtracts amount from balance with validation |
| `Check_Balance()` | Displays current balance |
| `Mini_Statement()` | Displays transaction history |

## Concepts Used

| Concept | Where used |
|---------|-----------|
| If-Else | PIN check, balance check |
| While loop | Menu repeats until Exit |
| Counter | 3 PIN attempts (`attempts` variable) |
| Try-Except | Invalid input, missing file |
| Functions | `data()`, `save()`, `Deposit()`, `Withdraw()` etc. |
| List | `history[]` stores transactions |
| File handling | Read/write `atm.txt` |
| Operators | `+`, `-`, `>`, `<=`, `==` |

## Test Cases

| Test | Input | Expected Output | Actual Output | Result |
|------|-------|-----------------|---------------|--------|
| 1 Normal | PIN 1234, Menu 2, Amount 5000 | Deposit successful. New Balance: 15000 | Deposit successful. New Balance: 15000 | PASSED |
| 2 Boundary | PIN 1234, Menu 3, Amount 10000 | Withdrawal successful. New Balance: 0 | Withdrawal successful. New Balance: 0 | PASSED |
| 3 Invalid PIN | PIN 1111, 2222, 3333 | Invalid PIN. Attempts left: 2, 1. Account locked. Exiting... | Invalid PIN. Attempts left: 2, 1. Account locked. Exiting... | PASSED |
| 4 Different valid | Withdraw `abc`, then 2000, then Menu 4 | Invalid amount. Withdrawal successful. New Balance: 8000. Withdraw 2000 \| balance: 8000 | Invalid amount. Withdrawal successful. New Balance: 8000. Withdraw 2000 \| balance: 8000 | PASSED |

**Conclusion:** Expected output matched actual output in all 4 tests.

### Test Case Output (Terminal)

**Test 1 - Normal (Deposit 5000 -> New Balance 15000)**

```text
Enter PIN: 1234
Login successful.
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Mini Statement
 5. Exit
Menu option:2
Amount: 5000
Deposit successful. New Balance: 15000
```

**Test 2 - Boundary (Withdraw 10000 -> New Balance 0)**

```text
Enter PIN: 1234
Login successful.
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Mini Statement
 5. Exit
Menu option:3
Amount: 10000
Withdrawal successful. New Balance: 0
```

**Test 3 - Invalid PIN (1111, 2222, 3333 -> Account locked)**

```text
Enter PIN: 1111
Invalid PIN.
Attempts left: 2
Enter PIN: 2222
Invalid PIN.
Attempts left: 1
Enter PIN: 3333
Invalid PIN.
Account locked. Exiting...
```

**Test 4 - Different valid (Withdraw abc, then 2000 -> Mini Statement)**

```text
Login successful.
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Mini Statement
 5. Exit
Menu option:3
Amount: abc
Invalid amount.Please enter numbers only.
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Mini Statement
 5. Exit
Menu option:3
Amount: 2000
Withdrawal successful. New Balance: 8000
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Mini Statement
 5. Exit
Menu option:4
Withdraw 2000 | balance: 8000
```

## Problems Faced and Solutions

| # | Problem | Concept | Solution |
|---|---------|---------|----------|
| 1 | Wrong PIN still logging in | Counter, if-else | Attempts variable; account locks after 3 wrong PINs |
| 2 | Crash on `abc` amount | Try-except | Shows "Invalid amount" |
| 3 | Balance became negative | If condition | Added `amount > balance` check; shows "Insufficient funds" |
| 4 | Balance reset to 10000 | File handling | `save()` writes to `atm.txt` after every transaction |
| 5 | `atm.txt` not found | File handling, try-except | `data()` uses defaults 10000 and 1234 |
| 6 | Negative amount | If condition | Added `amount <= 0` check |
| 7 | Program closed after 1 menu | While loop | `while True` loop until user presses 5 |
| 8 | Mini statement empty | List | `history` list updated and saved on each transaction |
| 9 | Different balance in tests | File handling | Deleted `atm.txt` before each test |
| 10 | Test 4 statement wrong | File handling, list | Saved Withdraw 2000 first, then displayed it |
