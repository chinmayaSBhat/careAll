from model import conn,cur
import insertions as ins

#list all oldies
def list_all_oldies():
    return(cur.execute("SELECT * FROM OLD"))

#list all young
def list_all_young():
    return(cur.execute("SELECT * FROM YOUNG"))

#return all oldies who are cared by young
def retrieve_oldies_cared_by_young(name):
    try:
        query="SELECT NAME FROM OLD WHERE ID=(SELECT OID FROM CARE WHERE YID=(SELECT ID FROM YOUNG WHERE NAME="+name+"))"
        return(cur.execute(query))
    except:
        print("NO RECORDS FOUND")

#return the young wj=ho is caring the oldie
def retrieve_oldies_caretaker(name):
    try:
        query="SELECT NAME FROM YOUNG WHERE ID=(SELECT YID FROM CARE WHERE OID=(SELECT ID FROM OLD WHERE NAME="+name+"))"
        return(cur.execute(query))
    except:
        print("NO RECORDS FOUND")

#return feedback about the young
def retrieve_young_feedback(name):
    try:
        query="SELECT FEEDBACK,RATING FROM Y_FEEDBACK WHERE YID=(SELECT ID FROM YOUNG WHERE NAME="+name+")"
        return(cur.execute(query))
    except:
        print("NO RECORDS FOUND")

#return feedback about the oldie
def retrieve_oldies_feedback(name):
    try:
        query="SELECT FEEDBACK,RATING FROM O_FEEDBACK WHERE OID=(SELECT ID FROM OLD WHERE NAME="+name+")"
        return(cur.execute(query))
    except:
        print("NO RECORDS FOUND")

#list pending requests for an oldie
def list_request(name):
    try:
        query="SELECT NAME,AGE,ADDRESS FROM YOUNG Y,REQUEST_APPROVE R WHERE R.YID,OID="+ins.get_olie_id_by_name(name)
        return(cur.execute(query))
    except:
        print("NO REQUESTS YET")