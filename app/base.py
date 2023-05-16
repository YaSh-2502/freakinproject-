from flask import *
from app.db import *
from datetime import datetime


app=Flask(__name__)
d={}
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/second")
def sec():
    return render_template("second.html")

@app.route("/agentlogin")
def alogin():
    return render_template("agentlogin.html")

@app.route("/custlogin")
def clogin():
    return render_template("custlogin.html")

@app.route("/custsignup")
def csignup():
    return render_template("custsignup.html")

@app.route("/agentfirstpage")
def afpage():
    return render_template("agentfirstpage.html")

@app.route("/custfirstpage")
def cfpage():
    c=displaycar()
    return render_template("custfirstpage.html",clist=c)

@app.route("/addowner")
def addo():
    return render_template("addowner.html")

@app.route("/addcustomer")
def addc():
    return render_template("addcustomer.html")

@app.route("/addcar")
def addcar():
    return render_template("addcar.html")

@app.route("/viewowners")
def viewo():
    n=displayowner()
    return render_template("viewowners.html",olist=n)

@app.route("/viewcust")
def viewc():
    vc=displaycust()
    return render_template("viewcust.html",clist=vc)

@app.route("/viewcars")
def viewcar():
    vcar=displaycar()
    return render_template("viewcars.html",carlist=vcar)

@app.route("/viewpayment")
def viewpay():
    vpay=displayp()
    return render_template("viewpayment.html",cplist=vpay)

@app.route("/newpageowner")
def npo():
    return render_template("newpageowner.html")

@app.route("/newpagecust")
def npc():
    return render_template("newpagecust.html")

@app.route("/newpagecar")
def npcar():
    return render_template("newpagecar.html")

@app.route("/newpagepay")
def nppay():
    return render_template("newpagepay.html")


@app.route("/alogout")
def la():
    return render_template("alogout.html")

@app.route("/clogout")
def lc():
    e=request.args.get("lg")
    d.clear()
    return render_template("clogout.html")

@app.route("/contactus")
def cu():
    return render_template("contactus.html")

@app.route("/aboutus")
def au():
    return render_template("aboutus.html")

@app.route("/custcardetails")
def ccd():
    vcar1=displaycar()
    return render_template("custcardetails.html",carlist=vcar1)

@app.route("/custownerdetails")
def coo():
    vod=displayowner()
    return render_template("custownerdetails.html",colist=vod)

@app.route("/custagentdetails")
def caa():
    va=displayagent()
    return render_template("custagentdetails.html",alist=va)

@app.route("/paymentpage")
def ppp():
    email=d["info"]
    vpa=displaycp(email[0])
   
    return render_template("paymentpage.html",pplist=vpa)

@app.route("/addpayment")
def aap():
    return render_template("addpayment.html")

@app.route("/alog",methods=["post"])
def alog():
    email=request.form["email"]
    password=request.form["password"]
    t1=(email,password)
    t2=selectrec(email)
    if t1 in t2:
        return redirect("/agentfirstpage")
    else:
        return redirect("/agentlogin")

@app.route("/clog",methods=["post"])
def clog():
    email=request.form["email1"]
    password=request.form["password1"]
    t1=(email,password)
    t2=selectrec1(email)
    if t1 in t2:
        d["info"]=t1
        print(d)
        return redirect("/custfirstpage")
        
    else:
        return redirect("/custlogin")   

@app.route("/insc",methods=["post"])
def insc():
    x=0
    fname=request.form["name1"]
    for i in fname:
        x=x+int(ord(i))
    lname=request.form["name2"]
    loc=request.form["loc"]
    phno=request.form["contact"]
    email=request.form["email"]
    password=request.form["password"]
    dl=request.form["dlic"]
    led=request.form["dxd"]
    t=(x,fname,lname,loc,phno,email,password,dl,led)
    try:
        insertc(t)
    except Exception as e:
        print("Invalid")
        return redirect("/custsignup")
        
    return redirect("/custlogin")

@app.route("/insc1",methods=["post"])
def insc1():
    id=request.form["cid"]
    fname=request.form["cfname"]
    lname=request.form["cfname"]
    loc=request.form["cloc"]
    phno=request.form["cph"]
    email=request.form["cemail"]
    password=request.form["cpassw"]
    dl=request.form["cdl"]
    led=request.form["ced"]
    t=(id,fname,lname,loc,phno,email,password,dl,led)
    try:
        insertc1(t)
    except Exception as e:
        print("Invalid")
        return redirect("/addcustomer")

    return redirect("/newpagecust")

@app.route("/inso",methods=["post"])
def inso():
    oid=request.form["oid"]
    oname=request.form["oname"]
    oadd=request.form["oadd"]
    ocon=request.form["ocon"]
    oem=request.form["oemail"]
    totcar=request.form["totalc"]
    t=(oid,oname,oadd,ocon,oem,totcar)
    try:
        inserto(t)

    except Exception as e:
        print('Invalid id provided!!!')
        return redirect("/addowner")

    return redirect("/newpageowner")

@app.route("/inscar",methods=["post"])
def insca():
    caid=request.form["carid"]
    cab=request.form["cbrand"]
    cam=request.form["cmodel"]
    col=request.form["ccol"]
    cac=request.form["ccap"]
    cat=request.form["ctype"]
    cnp=request.form["cnplate"]
    co=request.form["co"]
    con=request.form["coname"]
    cpa=request.form["pa"]
    t=(caid,cab,cam,col,cac,cat,cnp,co,con,cpa)
    try:
        insertcar(t)
    
    except Exception as e:
        print("Invalid")
        return redirect("/addcar") 

    return redirect("/newpagecar")

@app.route("/insp",methods=["post"])
def inspa():
    cun=request.form["p1"]
    cab=request.form["p2"]
    cat=request.form["pp"]
    ccn=request.form["p3"]
    rd1=request.form["p4"]
    rd2=request.form["p5"]
    d1 = datetime.strptime(rd1,"%Y-%m-%d")
    d2 = datetime.strptime(rd2,"%Y-%m-%d")
    delta = d2 - d1
    cpa=findamt(cab,cat)[0][0]
    cpa2=int(delta.days)*int(cpa)
    cpm=request.form["payment"]
    email=request.form["ak"]
    t=(cun,cab,cat,ccn,rd1,rd2,cpm,cpa,cpa2,email)
    insertp(t)
    return redirect("/paymentpage")

    

@app.route("/deleteo")
def do():
    did=request.args.get("OWNER_ID")
    deleteo(did)
    return redirect("/viewowners")

@app.route("/deletec")
def dc():
    Cdid=request.args.get("CUST_ID")
    deletec(Cdid)
    return redirect("/viewcust")

@app.route("/deletecar")
def dcar():
    carid=request.args.get("CAR_ID")
    deletecar(carid)
    return redirect("/viewcars")

@app.route("/deletep")
def dpay():
    cuname=request.args.get("CUST_NAME")
    deletep(cuname)
    return redirect("/viewpayment")

@app.route("/editowner")
def edito():
    sid=request.args.get("OWNER_ID")
    e=selo(sid)
    return render_template("/editowner.html",olist=e)

@app.route("/editcust")
def editc():
    sid=request.args.get("CUST_ID")
    ec=selc(sid)
    return render_template("/editcust.html",clist=ec)

@app.route("/editcar")
def editcar():
    csid=request.args.get("CAR_ID")
    cl=selcar(csid)
    return render_template("/editcar.html",carlist=cl)

@app.route("/editpay")
def editpay():
    ep=request.args.get("CUST_NAME")
    pe=selp(ep)
    return render_template("/editpay.html",plist=pe)

@app.route("/update",methods=["post"])
def upo():
    oid=request.form["oid"]
    oname=request.form["oname"]
    oadd=request.form["oadd"]
    ocon=request.form["ocon"]
    oem=request.form["oemail"]
    totcar=request.form["totalc"]
    t1=(oid,oname,oadd,ocon,oem,totcar,oid)
    updateo(t1)
    return redirect("/viewowners")

@app.route("/updatec",methods=["post"])
def upc():
    id=request.form["cid"]
    fname=request.form["cfname"]
    lname=request.form["cfname"]
    loc=request.form["cloc"]
    phno=request.form["cph"]
    email=request.form["cemail"]
    password=request.form["cpassw"]
    dl=request.form["cd"]
    led=request.form["ced"]
    t1=(id,fname,lname,loc,phno,email,password,dl,led,id)
    updatec(t1)
    return redirect("/viewcust")

@app.route("/updatecar",methods=["post"])
def upcar():
    caid=request.form["carid"]
    cab=request.form["cbrand"]
    cam=request.form["cmodel"]
    col=request.form["ccol"]
    cac=request.form["ccap"]
    cat=request.form["ctype"]
    cnp=request.form["cnplate"]
    co=request.form["co"]
    con=request.form["coname"]
    cpa=request.form["pa"]
    t1=(caid,cab,cam,col,cac,cat,cnp,co,con,cpa,caid)
    updatecar(t1)
    return redirect("/viewcars")

@app.route("/updatepay",methods=["post"])
def uppay():
    eun=request.form["p1"]
    eab=request.form["p2"]
    eat=request.form["pp"]
    ecn=request.form["p3"]
    ed1=request.form["p4"]
    ed2=request.form["p5"]
    epm=request.form["payment"]
    epa=request.form["p7"]
    t1=(eun,eab,eat,ecn,ed1,ed2,epm,epa,eun)
    updatep(t1)
    return redirect("/viewpayment")


if __name__=="__main__":
    app.run(debug=True)




