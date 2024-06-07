import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values) :
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols += [symbol] * symbol_count

    return [[random.choice(all_symbols) for _ in range(cols)] for _ in range(rows)]


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()


def deposits():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and " + str(MAX_LINES))
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"Total bet ({total_bet}) is greater than balance ({balance}). Please try again.")
    print(f"you are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"you won on", *winning_lines)
    return winnings - total_bet
def main():
    balance = deposits()
    while True:
        if balance == 0:
            print("You have no more money to bet.")
            break
        if balance > 0:
            print(f"Your current balance is ${balance}")
            answer = input("Press enter to play or q to quit")
            if answer == "q":
                break
        balance += spin(balance)
        print(f"you left with ${balance}")

main()
