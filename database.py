import pymongo 
  
try: 
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn['mite'] 
    collec = db['faculty']
    print("Connected successfully........\n") 
except:   
    print("Could not connect to MongoDB........\n")

def add_faculty():
    #reading Data From User

    fac = {}
    sub = {}
    name = input("Enter Name :")
    age = input("Enter Age :")
    gender = input("Enter Gender :")
    su = input("Enter Subject Name :")
    ho = int(input("Enter Teaching Hour :"))
    exp = input("Enter Experience :")
    type_fac = input("Enter Type of employee :")
    qualification = input("Enter qualification :")

    #Adding to dictonary

    fac['Name'] = name
    fac['age'] = age
    fac['gender'] = gender
    fac['subjects'] = [su,ho]
    fac['experience'] = exp
    fac['type'] = type_fac
    fac['qualification'] = qualification

    collec.insert_one(fac)
    print("Faculty Record Inserted Successfully.......")

def add_ex_subject():
    sub = {}

    name = input("Enter Faculty Name To Add Subjects :")
    
    su = input("Enter Subject Name :")
    ho = int(input("Enter Teaching Hour :"))
    sub['Item'] = su
    sub['hour'] = ho

    collec.update_one({"name":name},{"$push" : { "subjects" : sub}})

    print(f"\nFaculty By Name {name} is updated by With 1 new Subjects")

def delete_one_subject():
    pass



    
    