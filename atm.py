import sys

#Sample bank ATM program
account = {
  "name":"CHLOE",
  "balance":50000, 
  "pin":"1234",
  "type":"PERSONAL ACCOUNT"
}
print("===MINI ATM===")
pin = input("Enter your pin :")

if pin == account["pin"]:
  while True:
    print("\n****ATM MENU****")
    print("1. Check Balance :")
    print("2. Deposit Money :")
    print("3. Withdraw money :")
    print("4. Account details :")
    print("5. EXIT")

    choice = input("Enter your choice :")
    if choice == "1":
      print(f"YOUR BALANCE IS {account['balance']:,}") 
    elif choice == "2":
      try:
        amount_str = input("Enter your amount :")
        amount = int(amount_str)
        if amount > 0:
          account["balance"] += amount
          print("Money deposited successfully")
          print(f"NEW BALANCE {account['balance']:,}") 
        else:
          print("Invalid amount. Amount must be positive.")
      except ValueError:
        print("Invalid input. Please enter a number.")
    elif choice == "3":
      try:
        amount_str = input("Enter your amount :")
        amount = int(amount_str)
        if amount <= 0:
          print("Invalid amount. Amount must be positive.")
        elif amount > account["balance"]:
          print("Insufficient amount")
        else:
          account["balance"] -= amount
          print("COLLECT YOUR CASH :")
          print(f"NEW BALANCE {account['balance']:,}") 
      except ValueError:
        print("Invalid input. Please enter a number.")
    elif choice == "4":
     print(f"\nACCOUNT NAME: {account['name']}")
     print(f"ACCOUNT BALANCE: {account['balance']:,}") 
     print(f"ACCOUNT TYPE: {account['type']}")
    elif choice == "5":
     print("THANK YOU ")
     break
    else:
      print("Invalid choice")

else:
  print("Invalid pin")
  print("Access denied")
