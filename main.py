MAX_LINES = 3


def deposits():
    
    while True:
        amount = input("Enter the amount you want to deposit: ")
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


def main():
    balance = deposits()
    pass
   
main()    