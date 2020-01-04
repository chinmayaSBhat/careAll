import model 
import insertions as insert
import retrievals as ret

def add_oldie():
    name=input("ENTER YOUR NAME  ")
    age=int(input("ENTER YOUR AGE  "))
    address=input("ENTER YOUR ADDRESS  ")
    fund=int(input("ENTER THE PAYMENT YOU CAN MAKE  "))
    data=[name,age,address,fund]
    insert.insert_to_old(data)


def add_young():
    name=input("ENTER YOUR NAME  ")
    age=int(input("ENTER YOUR AGE  "))
    address=input("ENTER YOUR ADDRESS  ")
    insert.insert_to_young(name,age,address)


def add_young_feedback():
    name=input("ENTER YOUR NAME  ")
    feedback=input("ENTER YOUR FEEDBACK  ")
    rating=int(input("ENTER YOUR RATING TO YOUR CARE TAKER"))
    insert.yfeedback(name,feedback,rating)

def add_oldie_feedback():
    yname=input("ENTER YOUR NAME  ")
    oname=input("ENTER NAME OF PERSON YOU ARE TAKING CARE  ")
    feedbak=input("ENTER YOUR FEEDBACK  ")
    rating=int(input("ENTER RATING TO THE PERSON"))
    insert.ofeedback(yname,oname,feedback,rating)

def get_oldie_feedback():
    name=input("ENTER THE NAME  ")
    feedback=ret.retrieve_oldies_feedback(name)
    try:
        for row in feedback:
            print(feedback)
    except:
        print("NO RECORD FOUND")

def get_young_feedback():
    name=input("ENTER THE NAME  ")
    feedback=ret.retrieve_young_feedback(name)
    try:
        for row in feedback:
            print(feedback)
    except:
        print("NO RECORD FOUND")

def make_request():
    yname=input("ENTER YOUR NAME  ")
    oname=input("ENTER OLDIE'S NAME  ")
    insert.make_request(yname,oname)

def list_all_requests(name):
    req=ret.list_request(name)
    try:
        for r in req:
            print(r)
    except:
        print("NO RECORD FOUND")

def delete_request(name):
    insert.delete_request(name)

def approve(oname,yname):
    insert.approve_request(oname,yname)

def get_youngs_clients(name):
    res=ret.retrieve_oldies_cared_by_young(name)
    try:
        for r in res:
            print(r)
    except:
        print("NO RECORD FOUND")

def get_oldies_care_taker(name):
    res=ret.retrieve_oldies_caretaker(name)
    try:
        for r in res:
            print(r)
    except:
        print("NO RECORD FOUND") 

def get_all_oldies():
    res=ret.list_all_oldies()
    try:
        for r in res:
            print(r)
    except:
        print("NO RECORD FOUND")

def get_all_young():
    res=ret.list_all_young()
    try:
        for r in res:
            print(r)
    except:
        print("NO RECORD FOUND")
