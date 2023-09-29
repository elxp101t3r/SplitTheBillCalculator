def main():
   print('Welcome to Split the payment calculator.\n')
   bill = float(input('What was the total of the bill? $'))
   tip = int(input('How much tip would you like to give?10, 12 or 15? '))
   people = int(input('How many people to split the bill? '))
   
   prc  = tip / 100
   tip_total = bill * prc
   bill_total = tip_total + bill
   bill_split = bill_total / people
   payment = round(bill_split, 2)
   
   print(f'Each person should pay: ${payment}')
if __name__ == '__main__':
    main()