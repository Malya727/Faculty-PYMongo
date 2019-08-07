import database as db 


print("~ "*10,"Welcome to Faculty Management System","~ "*10,"\n")
while True:
    print("~ "*15,"\n1.Add Faculty\n2.Add Subject To Faculty\n3.Remove Subject From Faculty\n4.Increase Experience by one year\n5.Update Faculty Qualification\n6.Delete Faculty\n7.Faculty With Subject\n8.Exit\n","~ "*15)
    choice = int(input("\nEnter Your Choice : "))

    if choice == 1:
        db.add_faculty()
    elif choice == 2:
        db.add_ex_subject()
    elif choice == 3:
        db.delete_one_subject()
    elif choice == 4:
        db.increment_exp()
    elif choice == 5:
        db.update_qualification()
    elif choice == 6:
        db.delete_faculty()
    elif choice == 7:
        db.faculty_subject()
    else:
        print("Invalid Choice Please Try Again.....")