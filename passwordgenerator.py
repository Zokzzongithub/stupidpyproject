import os
import random
import sys
import time
import json


saved_file = "saved_passwords.json"
if not os.path.exists(saved_file):
    with open(saved_file, 'w') as f:
        json.dump([], f)

mainloop = True

while mainloop:
    user_choice = input("press y to continue, n to exit: ")
    if user_choice.lower() == 'y':
        choice = input("choose a number between 1 and 25 to generate a random password: ")
        try:
            length = int(choice)
            if 1 <= length <= 25:
                characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
                password = ''.join(random.choice(characters) for _ in range(length))
                print(f"Generated password: {password}")
                choice_save = input("press y to save the password, n to skip saving: ")
                specification = input("specify what the password is for (e.g., email, social media, etc.): ")
                if choice_save.lower() == 'y':
                    with open(saved_file, 'r') as f:
                        saved_passwords = json.load(f)
                    saved_passwords.append({"password": password, "specification": specification})
                    with open(saved_file, 'w') as f:
                        json.dump(saved_passwords, f)
                    print("Password saved successfully.")
                elif choice_save.lower() == 'n':
                    print("Password not saved.")
                    continue
                else:
                    print("Invalid choice. Password not saved.")
                    continue


                choice2 = input("press y to generate another password, n to exit: ")
                if choice2.lower() == 'y':
                    continue
                    os.system("cls" if os.name == "nt" else "clear")
                elif choice2.lower() == 'n':
                    mainloop = False
                    print("Exiting the program.")
                else:
                    print("Invalid choice. Returning to main menu.")
                

            else:
                print("Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    elif user_choice.lower() == 'n':
        mainloop = False
        print("Exiting the program.")
    else:
        print("Invalid choice. Please press 'y' to continue or 'n' to exit.")

