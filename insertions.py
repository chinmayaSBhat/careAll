from model import cur,conn

#adding new oldie
def insert_to_old(data):
    try:
        cur.execute("""INSERT INTO OLD(ID,NAME,AGE,ADDRESS,FUND) VALUES(NULL,?,?,?,?);""",data)
        conn.commit()
    except:
        print("can not insert please try again later")

#adding new young 
def insert_to_young(name,age,address):
    data=[name,age,address]
    try:
        cur.execute("""INSERT INTO YOUNG(ID,NAME,AGE,ADDRESS) VALUES(NULL,?,?,?);""",data)
        conn.commit()
    except:
        print("can not insert please try again later")

#get oldie id by name
def get_olie_id_by_name(name):
    query="SELECT ID FROM OLD WHERE NAME='"+name+"'"
    return(next(cur.execute(query)))
    

#get young id by name
def get_young_id_by_name(name):
    query="SELECT ID FROM YOUNG WHERE NAME='"+name+"'"
    print(query)
    return(next(cur.execute(query)))
    
        
#requests made by young
def make_request(yname,oname):
        yid=get_young_id_by_name(yname)
        oid=get_olie_id_by_name(oname)
        query="SELECT COUNT(YID) FROM CARE WHERE YID="+str(yid[0])
        data=[oid,yid]
        print(data)
        if(next(cur.execute(query))[0]<4):
            cur.execute("""INSERT INTO REQUEST_APPROVE(OID,YID,REQUEST) VALUES(?,?,0);""",data)
            conn.commit()
        else:
            print("YOU CANNOT TAKE CARE OF MORE THAN 4 PEOPLE")
   
#request approval for oldies
def approve_request(oname,yname):
    try:
        yid=get_young_id_by_name(yname)
        oid=get_olie_id_by_name(oname)
        query="UPDATE REQUEST_APPROVE SET REQUEST=1 WHERE OID="+oid+"&& YID="+yid
        cur.execute(query)
        conn.commit()
    except:
        print("can not insert please try again later")

#care taking info
def insert_care(oid,yid):
    dat=[oid,yid]
    try:
        cur.execute("""INSERT INTO CARE(OID<YID) VALUES(?,?);""",data)
        conn.commit()
    except:
        print("can not insert please try again later")

#feedback by young to oldies
def ofeedback(yname,oname,feedback,ratings):
    
    try:
        yid=get_young_id_by_name(yname)
        oid=get_olie_id_by_name(name)
        data=[oid,yid,feedback,rating]
        cur.execute(""""INSERT INTO O_FEEDBACK(OID,YID,FEEDBACK) VALUES(?,?,?,?);""",data)
    except:
        print("can not insert please try again later")

#feedback by oldies to young
def yfeedback(name,feedback,ratings):
    try:
        query="SELECT ID FROM CARE WHERE OID="+get_olie_id_by_name(name)
        yid=next(cur.execute(query))
        dat=[yid,oid,feedback,rating]
        cur.execute(""""INSERT INTO Y_FEEDBACK(YID,OID,FEEDBACK) VALUES(?,?,?,?);""",data)
    except:
        print("can not insert please try again later")

#delete request
def delete_request(name):
    try:
        oid=get_olie_id_by_name(name)
        query="DELETE FROM REQUEST_APPROVE WHERE OID="+oid
        cur.execute(query)
    except:
        print("CANNOT DELETE NOW PLEASE TRY AGAIN LATER")