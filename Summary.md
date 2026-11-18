# ATM Management System - Summary

A simple ATM program for the command line, written in Python 3 (PS No. 95). It copies how a real ATM works: you log in with a PIN, pick an option from a menu, and your balance and history are remembered the next time you run it.

## Key Points
- **Secure login:** 3 PIN attempts, then the account is locked
- **Banking options:** check balance, deposit, withdraw and view a mini statement
- **Safe input:** wrong entries like letters, zero or negative numbers are rejected without crashing
- **No overdraft:** you can't withdraw more than your balance
- **Saved data:** balance, PIN and history are stored in `atm.txt`
- **Repeating menu:** the menu keeps coming back until you choose Exit
- **Transaction history:** every deposit and withdrawal is recorded and shown in the mini statement
- **Missing file handling:** if `atm.txt` is not found, the program starts with default values (PIN 1234, balance 10000)
- **Clear messages:** every action shows a clear result, like "Deposit successful" or "Insufficient funds"
- **Modular code:** the work is split into functions (`data()`, `save()`, `Deposit()`, `Withdraw()`, `Check_Balance()`, `Mini_Statement()`)
- **Easy to run:** plain Python 3 with no extra libraries, started with `python one.py`
- **Tested:** normal, boundary and invalid cases were checked

## How to Run
1. Put `one.py` in a folder (for example `ATM-Management-System`).
2. Open a terminal in that folder.
3. Run the program:
   ```bash
   python one.py
   ```
4. Enter the default PIN `1234` (starting balance is 10000).

If `atm.txt` is missing, the program creates it with these default values.

## Skills Practiced
Conditions (if-else), loops, counters, error handling (try-except), functions, lists and file handling.

## Testing
I ran 4 test cases: a normal deposit, a withdrawal of the full balance, three wrong PINs, and an invalid amount followed by a valid withdrawal and statement. All 4 matched the expected output and passed.

## Outcome
A working ATM program that handles mistakes properly and keeps its data between runs.
