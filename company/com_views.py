from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
import simplejson as json
from django.core.files.storage import FileSystemStorage

conn = MySQLdb.connect("localhost","root","","policy_craft")
c = conn.cursor()

# Create your views here.
def com_header_footer(request):
    return render(request,"com_header_footer.html")

def com_home(request):
    return render(request,"com_home.html")

def premium(request):
    com_id = request.session["com_id"]

    msg = ""
    qry1 = "select * from premium where com_id = '"+str(com_id)+"'"
    c.execute(qry1)
    data = c.fetchall()
    if 'add_premium' in request.POST:
        premium = request.POST.get("premium")
        qry2 = "insert into premium(`pre_type`,`com_id`) values('"+str(premium)+"','"+str(com_id)+"')" 
        c.execute(qry2)
        conn.commit()
        qry1 = "select * from premium where com_id = '"+str(com_id)+"'"
        c.execute(qry1)
        data = c.fetchall()
        msg = "Premium Added Successfully"
        return render(request,"premium.html",{"data":data,"msg":msg})
    return render(request,"premium.html",{"data":data,"msg":msg})

def insurance_amount(request):
    com_id = request.session["com_id"]

    msg = ""
    qry1 = "select * from amount where com_id = '"+str(com_id)+"'"
    c.execute(qry1)
    data = c.fetchall()
    if 'add_amount' in request.POST:
        amount = request.POST.get("amount")
        qry2 = "insert into amount(`amount`,`com_id`) values('"+str(amount)+"','"+str(com_id)+"')" 
        c.execute(qry2)
        conn.commit()
        qry1 = "select * from amount where com_id = '"+str(com_id)+"'"
        c.execute (qry1)
        data = c.fetchall() 
        msg = "Amount Added Successfully"
        return render(request,"insurance_amount.html",{"data":data,"msg":msg})
    return render(request,"insurance_amount.html",{"data":data,"msg":msg})

def add_policy(request):
    com_id = request.session["com_id"]

    msg = ""
    qry1 = "select * from category"
    c.execute(qry1)
    data = c.fetchall()

    qry2 = "select * from amount where com_id = '"+str(com_id)+"'"
    c.execute(qry2)
    data1 = c.fetchall()

    qry3 = "select * from premium where com_id = '"+str(com_id)+"'"
    c.execute(qry3)
    data2 = c.fetchall()
    if 'add_policy' in request.POST:
        category = request.POST.get("category")
        policy_name = request.POST.get("policy_name")
        s = "select count(*) from policy where p_name='"+str(policy_name)+"' and com_id = '"+str(com_id)+"'"
        c.execute(s)
        cnt = c.fetchone()
        if cnt[0] == 0 :
            amount = request.POST.get("amount")
            premium = request.POST.get("premium")
            policy_duration = request.POST.get("policy_duration")
            policy_description = request.POST.get("policy_description")
            policy_payment = request.POST.get("policy_payment")
            # policy_document = request.POST.get("policy_document")

            myfile = request.FILES["policy_document"]
            fs = FileSystemStorage()        
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            qry4 = "insert into policy(`p_name`,`cat_id`,`amount_id`,`premium_id`,`p_duration`,`p_description`,`p_document`,`com_id`,`payment`) values('"+str(policy_name)+"','"+str(category)+"','"+str(amount)+"','"+str(premium)+"','"+str(policy_duration)+"','"+str(policy_description)+"','"+str(uploaded_file_url)+"','"+str(com_id)+"','"+str(policy_payment)+"')"
            c.execute(qry4)
            conn.commit()
        
            msg = "Policy Added Successfully"
        else:
            msg = "POlicy Already Exists"
        return render(request,"add_policy.html",{"data":data,"msg":msg})
    return render(request,"add_policy.html",{"data":data,"data1":data1,"data2":data2,"msg":msg})

def view_policy(request):
    com_id = request.session["com_id"]

    # msg = ""
    qry1 = "select * from category "
    c.execute(qry1)
    data = c.fetchall()
    print(data)

    if 'submit' in request.POST:
        category = request.POST.get("category")
        s = "select * from policy p, category c, premium pr, amount a where p.cat_id='"+str(category)+"' and p.com_id = '"+str(com_id)+"' and c.cat_id = p.cat_id and a.com_id = p.com_id and a.amt_id = p.amount_id and pr.com_id = p.com_id and pr.pre_id = p.premium_id "
        c.execute(s)
        data1 = c.fetchall()
        print(s)
        print(data1)
        
        return render(request,"view_policy.html",{"data":data,"data1":data1})
    return render(request,"view_policy.html",{"data":data})

def view_request(request):
    # msg = ""
    msg = request.GET.get("message")
    com_id = request.session["com_id"]
    s = "SELECT * FROM applications a, policy p, user_register u  WHERE a.com_id = '"+str(com_id)+"' AND p.com_id = a.com_id AND a.p_id = p.p_id AND a.`u_id` = u.`u_id`"
    c.execute(s)
    data1 = c.fetchall()
    print(s)
    print(data1)
    if not bool(data1):
        msg = "No Requests to Show"
    return render(request,"view_request.html",{"data1":data1,"msg":msg})


def view_user(request):
    # msg = ""
    msg = request.GET.get("message")
    com_id = request.session["com_id"]
    s = "SELECT * FROM applications a, policy p, user_register u  WHERE a.com_id = '"+str(com_id)+"' AND p.com_id = a.com_id AND a.p_id = p.p_id AND a.`u_id` = u.`u_id`"
    c.execute(s)
    data1 = c.fetchall()
    print(s)
    print(data1)
    if not bool(data1):
        msg = "No Requests to Show"
    return render(request,"view_user.html",{"data1":data1,"msg":msg})


def remove_policy(request):
    policy_id = request.GET.get("policy_id")

    s  = "delete from policy where p_id = '"+str(policy_id)+"'"
    c.execute(s)
    conn.commit()
    msg = "Deleted Successfully"
    return HttpResponseRedirect("/view_policy",{"msg":msg})

def update_status(request):
    appl_id = request.GET.get("appl_id")
    st = request.GET.get("st")
    com_id = request.session["com_id"]


    if st == 'Approved' :
        s  = "update applications set status = '"+str(st)+"' where apl_id = '"+str(appl_id)+"'"
        c.execute(s)
        conn.commit()
    elif st == 'Completed' :
        sumamount = "SELECT SUM(amount),policy_id,amount FROM payment WHERE  appl_id='"+str(appl_id)+"'"
        c.execute(sumamount)
        data1 = c.fetchone()
        # print(data1[2])
        print(sumamount)
        s1 = "select a.amount from policy p, amount a where p.p_id= '"+str(data1[1])+"' and p.com_id = '"+str(com_id)+"' and a.com_id = p.com_id and p.amount_id = a.amt_id"
        c.execute(s1)
        print(s1)
        data2 = c.fetchone()
        # print(data2)
        # print(data1)
    
        try:
            print("haiiiii")
            if int(data1[0]) == int(data2[0]) :
                s  = "update applications set status = '"+str(st)+"' where apl_id = '"+str(appl_id)+"'"
                c.execute(s)
                conn.commit()
                return HttpResponseRedirect("/view_request")
            else:
                diff = int(data2[0]) - int(data1[0]) 
                print(diff)
                no_pre = int(diff)//int(data1[2])
                print(no_pre)
                print("Nodata")
                message = "There are "+str(no_pre)+" more Insurance Premium payment dues. Please make sure that all payments are done before closing the Insurance case."
            return HttpResponseRedirect("/view_request?message="+str(message))
        except:
            print("Nodata")
            message = "There Insurance Premium payment dues. Please make sure that all payments are done before closing the Insurance case."
            return HttpResponseRedirect("/view_request?message="+str(message))

    elif st == 'Processing' :
        s  = "update applications set status = '"+str(st)+"' where apl_id = '"+str(appl_id)+"'"
        c.execute(s)
        conn.commit()
    else:
        s  = "update applications set status = '"+str(st)+"' where apl_id = '"+str(appl_id)+"'"
        c.execute(s)
        conn.commit()
    return HttpResponseRedirect("/view_request")
def complaint(request):
    id=request.GET.get("id")
    uid=request.session["usersid"]
    t="user"
    s = "select count(*) from  login where reg_id = '"+str(id)+"' and type= '"+str(t)+"'"
    c.execute(s)
    da=c.fetchone()
    cou=da[0]
    
    cou=cou+1
    st="counted"
    s = "update login set count = '"+str(cou)+"',bstatus = '"+str(st)+"' where reg_id = '"+str(uid)+"'"
    c.execute(s)
    print(s)
    conn.commit()
    return HttpResponseRedirect("/view_request/")
def pay_history(request):
    msg = ""
    com_id = request.session["com_id"]
    appl_id = request.GET.get("appl_id")
    u_id = request.GET.get("u_id")
    request.session["usersid"]=u_id
    s = "select pay_id,date,amount from payment where appl_id='"+str(appl_id)+"' and c_id='"+str(com_id)+"'"
    print(s)
    c.execute(s)
    data = c.fetchall()
    if not bool(data):
        data=""
        msg = "No Transaction done yet"
        return render(request,"pay_history.html",{"data":data,"msgg":msg,"uid":u_id})
    return render(request,"pay_history.html",{"data":data})