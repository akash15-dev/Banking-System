from colorama import init, Fore, Style
from datetime import datetime
init(autoreset=True)

class Banking_System:
    
    holders_name = "Guest"     #class variables to store account details
    account_number = 0000
    
    @staticmethod
    def home_page():  #home page method
        loop = True
        print(Fore.CYAN + Style.BRIGHT + "\nWelcome to the Banking System!✨\n")
        print(Fore.YELLOW + "1. Create Account-📝\n2. Login-🔐\n3. Exit-🚪\n")
        while loop:
            try:
                number = int(input(Fore.GREEN + Style.BRIGHT + "👉Enter your choice: "))
                
                if number == 1:     #checking user input if 1 it calls new_account method 
                    print(Fore.MAGENTA + "\n-------------------------------------------")
                    print(Fore.MAGENTA + "<< Redirecting to Account Creation Page >>")
                    print(Fore.MAGENTA + "-------------------------------------------")
                    Banking_System.new_account()
                    loop = False
                elif number == 2:   #checking user input if 2 it login_page method 
                    print(Fore.MAGENTA + "\n--------------------------------")
                    print(Fore.MAGENTA + "<< Redirecting to Login Page >>")
                    print(Fore.MAGENTA + "--------------------------------")
                    Banking_System.login_page()
                    loop = False
                elif number == 3:    #checking user input if 3 it Exit
                    print(Fore.RED + "Exiting...👋")
                    print(Fore.BLUE + Style.BRIGHT + "\n-----------------------------------")
                    print(Fore.BLUE + Style.BRIGHT + "<< Thanks for Banking with us😊 >>")
                    print(Fore.BLUE + Style.BRIGHT + "----------------------------------- \n")
                    loop = False
                else:
                    print(Fore.RED + " ### Please Enter Number Between 1-3 ❌ ### \n")
            except ValueError:  #eror handling for wrong values
                print(Fore.RED + "### Please Enter Valid Number ❌ ### \n")

    @staticmethod
    def new_account():  #creating new bank account in thsis method
        
        loop = True
        
        while loop:  #here while loop is for repeating the logic if user enter wrong values
            try:
                print(Fore.CYAN + Style.BRIGHT + "\nPlease Enter your Details to Create New Account \n")
                name = input(Fore.GREEN + Style.BRIGHT + "👉Enter your name: ")
                deposit = float(input(Fore.GREEN + Style.BRIGHT + "👉Enter your initial deposit: "))
                acc_number = int(input(Fore.GREEN + Style.BRIGHT + "👉Your account number: "))
                password = input(Fore.GREEN + Style.BRIGHT + "👉Enter a password: ")
                
                with open("accounts.txt", "a+") as file:  # creating new account in account.txt with user input details
                    file.seek(0)  
                    data = file.read()
                    if data and not data.endswith('\n'):
                        file.write('\n')
                    file.write(f"{acc_number},{name},{password},{deposit},{datetime.now()}\n")
                    
                print(Fore.GREEN + "\nAccount created successfully!✅")
                print(Fore.MAGENTA + "\n--------------------------------")
                print(Fore.MAGENTA +"<< Redirecting to Login Page >>")
                print(Fore.MAGENTA +"-------------------------------- \n")
                loop = False
                Banking_System.login_page()  #redirecting to login method
                break
            
            except ValueError:   #eror handling for wrong values
                print(Fore.RED + " ### Please Enter Correct Details ❌ ### \n")
            except FileNotFoundError:   #eror handling for file not found
                print(Fore.RED + " ### Sorry..Error in Saving Records ❌ ### \n")
            

    @staticmethod
    def login_page():  #validating login details in this method
        loop = True
        count = 3
        account_found = True
        while loop:      #here while loop is for repeating the logic if user enter wrong values
            try:
                print(Fore.CYAN + Style.BRIGHT + "\nPlease Enter your Details to Login \n")
                acc_number = int(input(Fore.GREEN + Style.BRIGHT + "👉Enter your account number: "))
                password = input(Fore.GREEN + Style.BRIGHT + "👉Enter your password: ")
                
                with open("accounts.txt", "r") as file:   #reading account details to verify user details
                    data = file.readlines()
                    for account in data:
                        acc_num, name, passw, balance,created_date = account.strip().split(",")
                        if acc_num == str(acc_number):
                            account_found = False
                            if passw == password:
                                Banking_System.holders_name = name    #checking login details
                                Banking_System.account_number = acc_num
                                print(Fore.GREEN + "\nLogin successful!✅")
                                print(Fore.MAGENTA + "\n--------------------------------")
                                print(Fore.MAGENTA +"<< Redirecting to Main Menu >>")
                                print(Fore.MAGENTA +"-------------------------------- \n")
                                loop = False
                                Banking_System.main_menu()
                                break
                            else:
                                print(Fore.RED + "\n<< Entered Password is Wrong ❌ >>")
                                count -= 1
                    
                    if account_found:   # if condition to conform that if that account is find or not
                        print(Fore.RED + "\n<< Entered Account Number is Wrong ❌ >>")
                        count -= 1
                    
                    if count == 0:
                        print(Fore.RED + "\nAttempt Limit Exceeded..Please Try again Later ❌")
                        break
            except ValueError:    #eror handling for wrong values
                print(Fore.RED + "Please Enter Valid Details ❌")
            except FileNotFoundError:   #eror handling for file not found
                print(Fore.RED + "Account Not Found ❌")

    @staticmethod
    def main_menu():
        updated_account = []
        main_loop = True
        loop = True
        account_found = False
        updated_balance = 0
        status_dept = "Deposit"
        status_withd = "Withdraw"
       
        
        print(Fore.CYAN + Style.BRIGHT + f"Welecome back {Banking_System.holders_name}✨, \n")
        print(Fore.YELLOW + "1. View Profile🧑‍           6. Check Balance💰\n2. Deposit Money💳          7. Withdraw Money💸\n3. Transfer Funds🔁         8. Transaction History📜\n4. Interest Calculator🧮    9. Change Password🔒\n5. General FAQ❓            10. Logout🚪 \n")            
    
        while main_loop:
           try:
               number = int(input(Fore.GREEN + Style.BRIGHT + "👉Enter your choice: "))
               
               if number == 1:  #checking user input
                   
                   print(Fore.CYAN + Style.BRIGHT + "\nYour Profile Details🧑‍ \n")
                   
                   with open ("accounts.txt","r") as file:   #reading account details to showing account details
                       for line in file:
                           acc_num, name, password, balance, created_date = line.strip().split(",")
                           if acc_num == str(Banking_System.account_number):  #if account matches it will  show  account details
                               print(Fore.WHITE + f"# Account Number       : {acc_num}")
                               print(Fore.WHITE + f"# Holder's Name        : {name}")
                               print(Fore.WHITE + f"# Account Balance      : {balance}")       # printing values
                               print(Fore.WHITE +  "# Account Password     : xxxxxx")
                               print(Fore.WHITE + f"# Account Created Date : {created_date}")
                               
                               print(Fore.MAGENTA + "\n--------------------------------")
                               print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                               print(Fore.MAGENTA +"-------------------------------- \n")
                               main_loop = False
                               Banking_System.main_menu()  # redirecting to main menu
                           
                    
               
               if number == 2:
                   amount = float(input(Fore.GREEN + Style.BRIGHT + "\n👉Enter Amount to Deposit: "))
                   with open("accounts.txt", "r") as file:  #reading account details to deposit money
                       for line in file:
                           acc_num, name, password, balance, created_date = line.strip().split(",")
                           if acc_num == str(Banking_System.account_number):  # checking for account number to deposit money
                               updated_account.append(f"{acc_num},{name},{password},{float(balance) + amount},{created_date}\n") # addinng money
                               updated_balance = float(balance) + amount
                               account_found = True
                           else:
                               updated_account.append(line.strip() + "\n")
                   if account_found:
                       with open("transactions.txt", "a") as file:  # adding transaction details to transaction.txt
                           file.write(f"{Banking_System.account_number},{status_dept},{amount},{datetime.now()}\n")
                       with open("accounts.txt", "w") as file:   # writing account final values
                           file.writelines(updated_account)
                       print(Fore.GREEN + "\nDeposit successful!✅")
                       print(Fore.YELLOW + f"🔴Your Current Balance : {updated_balance}")
                       print(Fore.MAGENTA + "\n--------------------------------")
                       print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                       print(Fore.MAGENTA +"-------------------------------- \n")
                       main_loop = False
                       Banking_System.main_menu()  #redirecting to main menu
                   else:
                       print(Fore.RED + "Account not Found ❌")





               elif number == 3:
                   
                   print(Fore.CYAN + Style.BRIGHT + "\nTransfer Funds🔁 \n")
                   loop = True
                   while loop:
                       try:
                           transfer_amount = float(input(Fore.GREEN + Style.BRIGHT + "Enter Amount to Transfer: "))
                           transfer_account = input(Fore.GREEN + Style.BRIGHT + "Enter Receiver's Account Number: ")

                       
                           sender_found = False
                           receiver_found = False


                           with open("accounts.txt", "r") as file: #reading account details to check sender account is there for transfer monney
                               accounts = file.readlines()
                               for line in accounts:
                                   acc_num, name, password, balance, created_date = line.strip().split(",")
                                   if acc_num == str(transfer_account):  # checking for the receiver account number 
                                       new_balance = float(balance) + transfer_amount
                                       updated_account.append(f"{acc_num},{name},{password},{new_balance},{created_date}\n")
                                       receiver_found = True
         
                                   elif acc_num == str(Banking_System.account_number): # checking for the sender account number 
                                       if float(balance) >= transfer_amount:
                                           new_balance = float(balance) - transfer_amount
                                           updated_account.append(f"{acc_num},{name},{password},{new_balance},{created_date}\n") # updating amount
                                           sender_found = True
                                       else:
                                           print(Fore.RED + "\n❌ Insufficient balance!")
                                           loop = False
                                           break
                                   else:
                                       updated_account.append(line if line.endswith("\n") else line + "\n")

                           if sender_found and receiver_found:
                               with open("accounts.txt", "w") as file:  # writing final values
                                   file.writelines(updated_account)

                               with open("transactions.txt", "a") as tfile:    # adding sending and reciving transaction details to transaction.txt
                                   tfile.write(f"{Banking_System.account_number},Sent,{transfer_amount},{datetime.now()}\n")
                                   tfile.write(f"{transfer_account},Recived,{transfer_amount},{datetime.now()}\n")
                                   print(Fore.GREEN + "\n✅ Transfer Successful!")
                                   loop = False
                                   main_loop = False
                                   print(Fore.MAGENTA + "\n--------------------------------")
                                   print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                                   print(Fore.MAGENTA +"-------------------------------- \n")                                   
                                   Banking_System.main_menu()   #redirecting to main menu
                           elif not receiver_found:
                               print(Fore.RED + "\n❌ Receiver account not found!")

                       except ValueError:   #eror handling for wrong values
                           print(Fore.RED + "\n❌ Please enter valid numeric values!")
                       except FileNotFoundError:   #eror handling for file not found
                           print(Fore.RED + "\n❌ Account file not found!")
                   
                   
                   
                   
               elif number == 4:
                   
                   print(Fore.CYAN + Style.BRIGHT + "\nInterest Calculator🧮 \n")
                   while loop:
                       try:
                           principal = float(input(Fore.GREEN + Style.BRIGHT + "👉 Enter Principal Amount (₹): "))
                           rate = float(input(Fore.GREEN + Style.BRIGHT + "👉 Enter Annual Interest Rate (%): "))
                           time = float(input(Fore.GREEN + Style.BRIGHT + "👉 Enter Time (in years): "))
                           
                           interest = (principal * rate * time) / 100     # interest calculation formula
                           total_amount = principal + interest
                           
                           print(Fore.WHITE + f"\n🔴 Simple Interest: ₹{interest:.2f}")
                           print(Fore.WHITE + Style.BRIGHT + f"🔴 Total Amount after {time} years: ₹{total_amount:.2f}")   # printing intrest details
                           print(Fore.MAGENTA + "\n--------------------------------")
                           print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                           print(Fore.MAGENTA +"-------------------------------- \n")
                           loop = False
                           main_loop = False
                           Banking_System.main_menu()  # redirecting to main menu
                           
                           
                       except ValueError:   #eror handling for wrong values
                           print(Fore.RED + "\n❌ Please enter valid numeric values!\n")
            
               
               elif number == 5:
                   
                   print("\nGeneral FAQ❓")   # general FAQ printing
                   print(Fore.CYAN + Style.BRIGHT + "\nQ1: How can I create a new account?")
                   print("👉 Ans: From the main menu, choose the option to create a new account and follow the prompts.")

                   print(Fore.CYAN + Style.BRIGHT + "\nQ2: What should I do if I forget my password?")
                   print("👉 Ans: Currently, you must remember your password. Password recovery may be added in future versions.")

                   print(Fore.CYAN + Style.BRIGHT + "\nQ3: Is there a minimum balance required?")
                   print("👉 Ans: No, your account can have ₹0 balance, but you must maintain at least ₹1 to make withdrawals.")

                   print(Fore.CYAN + Style.BRIGHT + "\nQ4: Is my data saved?")
                   print("👉 Ans: Yes, your account details are securely saved in the accounts.txt file.")

                   print(Fore.CYAN + Style.BRIGHT + "\nQ5: How is interest calculated?")
                   print("👉 Ans: We use Simple Interest formula: (Principal × Rate × Time) / 100")
                   
                   print(Fore.MAGENTA + "\n--------------------------------")
                   print(Fore.MAGENTA +"<< 🔙 Returning to main menu >>")
                   print(Fore.MAGENTA +"-------------------------------- \n")
                   main_loop = False
                   Banking_System.main_menu()   # redirecting to main menu
            
               
               elif number == 7:
                   with open("accounts.txt", "r") as file:  #reading account details to withdraw
                       for line in file:
                           acc_num, name, password, balance, created_date = line.strip().split(",")
                           if acc_num == str(Banking_System.account_number):    # checking for correct account number
                               while loop:
                                   print(Fore.YELLOW + Style.BRIGHT + f"\n🔴Your Current Balance : {float(balance)}")
                                   amount = float(input(Fore.GREEN + Style.BRIGHT + "👉Enter Amount to Withdraw: "))
                                   if amount >= 1 and float(balance) >= amount:  # checking balance amount and user entered amount
                                       updated_account.append(f"{acc_num},{name},{password},{float(balance) - float(amount)},{created_date}\n")
                                       updated_balance = float(balance) - float(amount)
                                       loop = False
                                       account_found = True
                                   else:
                                       print(Fore.RED + "\nPlease Check your Balance and Enter the Valid Amount ❌")
                           else:
                               updated_account.append(line.strip() + "\n")
                   if account_found:   #checking for account present in txt file
                       with open("transactions.txt", "a") as file:  
                           file.write(f"{Banking_System.account_number},{status_withd},{amount},{datetime.now()}\n")  # adding transaction details
                       with open("accounts.txt", "w") as file:
                           file.writelines(updated_account)
                       print(Fore.GREEN + "\nWithdraw successful!✅")
                       print(Fore.YELLOW + f"🔴Your Current Balance : {updated_balance}")
                       print(Fore.MAGENTA + "\n--------------------------------")
                       print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                       print(Fore.MAGENTA +"-------------------------------- \n")
                       main_loop = False
                       Banking_System.main_menu  # redirecting to main menu
                   else:
                       print(Fore.RED + "Account not Found ❌")            

               elif number == 6:
                   try:
                       with open("accounts.txt", "r") as file:  # reading account details
                           for line in file:
                               acc_num, name, password, balance, created_date = line.strip().split(",")
                               if str(Banking_System.account_number) == acc_num:  # checking for the account
                                   print(Fore.YELLOW + f"🔴Your Account({acc_num}) Balance is {float(balance)}")  #printing balance details
                                   print(Fore.MAGENTA + "\n--------------------------------")
                                   print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                                   print(Fore.MAGENTA +"-------------------------------- \n")
                                   main_loop = False
                                   Banking_System.main_menu()  # redirecting to main menu
                   except FileNotFoundError:    #eror handling for file not found
                       print(Fore.RED + "Account not Found ❌")

               elif number == 9:   
                   try:
                       new_password = input(Fore.GREEN + Style.BRIGHT + "\n👉Enter Your New Password: ")
                       with open("accounts.txt", "r") as file:   # reading account details
                           for line in file:   # iterating account details
                               acc_num, name, password, balance, created_date = line.strip().split(",")
                               if acc_num == str(Banking_System.account_number):    #checking for account number 
                                   updated_account.append(f"{acc_num},{name},{new_password},{balance},{created_date}\n")
                                   account_found = True
                               else:
                                   updated_account.append(line.strip() + '\n')
                       if account_found:
                           with open("accounts.txt", "w") as file:  #writing final account details
                               file.writelines(updated_account)
                           print(Fore.YELLOW + "New Password Changed successful!✅")
                           print(Fore.MAGENTA + "\n--------------------------------")
                           print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                           print(Fore.MAGENTA +"-------------------------------- \n")
                           main_loop = False
                           Banking_System.main_menu()  #redirecting to main menu
                   except ValueError:    #eror handling for wrong values
                       print(Fore.RED + "\nPlease Enter Valid Details ❌")
                   except FileNotFoundError:   #eror handling for file not found
                       print(Fore.RED + "\nAccount not Found ❌")

               elif number == 8:
                   
                   try:
                       with open ("transactions.txt", "r") as file:   #reading account details
                           print(Fore.CYAN + Style.BRIGHT + "\nTransaction Details of your Account📜")
                           
                           for line in file:   #iterating account details
                               acc_num, status, amount, date = line.strip().split(",")
                               if acc_num == str(Banking_System.account_number):  #checking for account number
                                   print(Fore.WHITE + f"{acc_num} - {status} - {amount} - {date}")    
                          
                          
                           print(Fore.MAGENTA + "\n--------------------------------")
                           print(Fore.MAGENTA +"<< 🔙 Returning to Main Menu >>")
                           print(Fore.MAGENTA +"-------------------------------- \n")
                           main_loop = False
                           Banking_System.main_menu()   #redirecting to main menu
                       
                       
                   except FileNotFoundError:   #eror handling for file not found
                       print(Fore.RED + "\nAccount not Found ❌")
                   
                   
               elif number == 10:  
                   print(Fore.RED + "Exiting...👋")  #exiting 
                   print(Fore.BLUE + Style.BRIGHT + "\n-----------------------------------")
                   print(Fore.BLUE + Style.BRIGHT + "<< Thanks for Banking with us😊 >>")
                   print(Fore.BLUE + Style.BRIGHT + "----------------------------------- \n")
                   main_loop = False
                   
               elif number > 10:   # if user enter wrong number this block will execute
                   print(Fore.RED + " ### Please Enter Number Between 1-10 ❌ ### \n")
                   
           except ValueError:    #eror handling for wrong values
               print(Fore.RED + " ### Please Enter Integer Value ❌ ### \n")
         
        

Banking_System.home_page()  #calling home page to execute the process.

# ------------------- Thank You --------------------------------#
