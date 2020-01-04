import all_function as af 
def __main__():
   while(True):
    choice=int(input("ENTER 1 TO ADD OLDIE\n ENTER 2 TO ADD YOUNG\n ENTER 3 TO GET MAKE REQUEST \n ENTER 4 TO APPROVE AN REQUEST\n ENTER 5 TO GET OLDIES FEEDBACK\n ENTER 6 TO GET YOUNG FEEDBACK\n ENTER 7 TO LIST YOUNGS CLENTS\n ENTER 8 TO GET OLDIES CARE TAKER\n ENTER 9 TO LIST ALL OLDIES\n ENTER 10 LIST ALL YOUNG "))
    if(choice==1):
        af.add_oldie()
    elif(choice==2):
        af.add_young()
    elif(choice==3):
        af.make_request()
    elif(choice==4):
        name =input("ENTER YOUR NAME\n")
        af.list_all_requests(name)
        ch=input("ENTER YOUR CARETAKERS NAME, IF NOT INTERESTED PRESS 1\n")
        if(ch==1):
            af.delete_request(name)
        else:
            af.approve(name,ch)
    elif(choice==5):
        af.get_oldie_feedback()
    elif(choice==6):
        af.get_young_feedback()
    elif(choice==7):
        name=input("ENTER YOUNG\'s NAME TO HIS CLIENTS\n")
        af.get_youngs_clients(name)
    elif(choice==8):
        name=input("ENTER OLDIE\'s NAME TO GET HIS CARE TAKER\n")
        af.get_oldies_care_taker(name)
    elif(choice==9):
        af.get_all_oldies()
    elif(choice==10):
        af.get_all_young()
__main__()