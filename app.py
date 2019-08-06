import database as db 


print("~ "*10,"Welcome to Faculty Management System"," ~"*10)
while True:
    print("\n1.Add Faculty\n2.Add Subject To Faculty\n3.Remove Subject")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        db.add_faculty()
    elif choice == 2:
        db.add_ex_subject()
    elif choice == 3:
        db.delete_one_subject()
    else:
        print("Invalid Choice Please Try Again.....")