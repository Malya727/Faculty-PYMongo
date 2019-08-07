import pymongo
from prettytable import PrettyTable 
  
try:
    url = "mongodb+srv://user:user@malya-pmnjq.mongodb.net/test?retryWrites=true&w=majority"
    conn = pymongo.MongoClient(url)
    db = conn['mite'] 
    collec = db['faculty']
    print("Connected successfully........\n") 
except Exception as e:   
    print(e)


#adding new faculty into db

def add_faculty():
    #reading Data From User

    fac = {}
    name = input("Enter Name :")
    age = input("Enter Age :")
    gender = input("Enter Gender :")
    s_name = input("Enter Subject Name :")
    s_time = int(input("Enter Teaching Hour :"))
    exp = int(input("Enter Experience :"))
    type_fac = input("Enter Type of employee :")
    qualification = input("Enter qualification :")

    #Adding to dictonary

    fac={
            "name" : name,
            "age" : age,
            "gender" : gender,
            "subjects" :[
                {
                  "s_title" : s_name,
                  "s_time" : s_time
                }],
            "experience" : exp,
            "type" : type_fac,
            "qualification" : qualification
        }

    collec.insert_one(fac)
    print("Faculty Record Inserted Successfully.......")

    print("+ "*40)



#adding one more subject for exsisting faculty

def add_ex_subject():
    try:
        sub = {}

        name = input("Enter Faculty Name To Add Subjects :")
        
        su = input("Enter Subject Name :")
        ho = int(input("Enter Teaching Hour :"))
        sub = {
            "s_title" : su,
            "s_time" : ho
        }

        collec.update_one({"name":name},{"$push" : { "subjects" : sub}})

        print(f"\nFaculty By Name {name} is updated by With 1 new Subjects")

    except:
        print(f"Unable to find employee with name {name}")

    print("+ "*40)


#deleting exisisting Subject From Faculty
def delete_one_subject():
    try:
        name = input("Enter Faculty Name To Remove Subjects :")
        sub = input("Enter The Subject Name To remove :")

        myquery = { "name": name }
        newvalues = { "$pull": { "subjects" : {"s_title" : sub} } }

        collec.update_one(myquery,newvalues)
    except:
        print("Unable To Delete Subject From {name} ")

    print("+ "*40)


#incrementing FAculty Experience by one year
def increment_exp():

    name = input("Enter The Name Of the Faculty To Incerment His/Her Experience :")

    try:
        myquery = { "name": name }
        newvalues = { "$inc": { "experience":1  } }
        collec.update_one(myquery,newvalues)
        print(f"Faculty With Name {name} increased His Experience by one year")
    except :
        print(f"Unable to find employee With Name : {name}")

    print("+ "*40)


#updating Faculty Qualification With new Qualification
def update_qualification():
    name = input("Enter The Name Of the Faculty To Update His/Her Qualification :")

    try:
        qual = input("Enter New Qualification to update Faculty :")
        myquery = { "name": name}
        newvalues = { "$set": { "qualification": qual } }

        collec.update_one(myquery, newvalues)

        print(f"Faculty With Name {name} is updated with New Qualification {qual} successfully!")

    except:
        print(f"Unable to Update Faculty With Name : {name} ")

    print("+ "*40)

#deleting Faculty From DB

def delete_faculty():
    name = input("Enter The Name Of the Faculty To Delete His Details :")

    try:
        myquery = { "name": name }
        collec.delete_one(myquery)
        print(f"Faculty With Name {name} deleted Successfully")
    except:
        print(f"Unable to Delete Faculty With name : {name} ")

    print("+ "*40)

def faculty_subject():
    que = [{"$unwind" : "$subject"},{"$project" : {"name" : 1 ,"subjects" : "$subjects.s_title"}}]

    x = PrettyTable()
    x.field_names = ["Name","Subject"]

    res = collec.aggregate(que)


    for r in res:
        x.add_row([r['name'],r['subjects']])

    print(x)
           



    
    