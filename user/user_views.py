from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
import simplejson as json
from django.core.files.storage import FileSystemStorage


# Create your views here.
conn = MySQLdb.connect("localhost","root","","policy_craft")
c = conn.cursor()

def user_header_footer(request):
    return render(request,"user_header_footer.html")

def user_home(request):
    return render(request,"user_home.html")

def user_view_policy(request):
    # u_id = request.session["u_id"]

    # msg = ""
    qry1 = "select * from category "
    c.execute(qry1)
    data = c.fetchall()
    print(data)

    if 'submit' in request.POST:
        category = request.POST.get("category")
        # s = "select * from policy p, category c, premium pr, amount a, company_register cr where p.cat_id='"+str(category)+"' and p.com_id = cr.c_id and c.cat_id = p.cat_id and a.com_id = p.com_id and a.amt_id = p.amount_id and pr.com_id = p.com_id and pr.pre_id = p.premium_id "
        s = "select distinct c.* from company_register c, policy p where  p.cat_id = '"+str(category)+"' and p.com_id = c.c_id"
        c.execute(s)
        data1 = c.fetchall()
        print(s)
        print(data1)
        return render(request,"user_view_policy.html",{"data":data,"data1":data1,"category":category})
    return render(request,"user_view_policy.html",{"data":data})


def payment1(request):
    request.session["appl_id"] = request.GET.get("appl_id")
    request.session["p_id"] = request.GET.get("p_id")
    p_id = request.GET.get("p_id")
    request.session["com_id"] = request.GET.get("com_id")
    # request.session["u_id"] = request.POST.get("u_id")
    com_id = request.GET.get("com_id")
    appl_id = request.GET.get("appl_id")
    if request.POST:
        request.session["cardno"]=request.POST.get("cardno")
        return HttpResponseRedirect("/payment2/")

    
    sumamount = "SELECT SUM(amount),policy_id,amount FROM payment WHERE  appl_id='"+str(appl_id)+"'"
    c.execute(sumamount)
    data1 = c.fetchone()
    print(data1[0])
    print(sumamount)
    s1 = "select a.amount,p.payment from policy p, amount a where p.p_id= '"+str(p_id)+"' and p.com_id = '"+str(com_id)+"' and a.com_id = p.com_id and p.amount_id = a.amt_id"
    c.execute(s1)
    print(s1)
    data2 = c.fetchone()
    print(data2)
    print(data1)

    s = "select payment from policy where p_id = '"+str(p_id)+"'"
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data2[1])

    request.session["amt"] = data2[1]
    

    try:
        print("haiiiii")
        
        if  data1[0] == None : 
            print("Noooooooooooooodata")
            message = "There are Insurance Premium to pay for completing this insurance application."
        # return HttpResponseRedirect("/payment1?message="+str(message))
            return render(request,"payment1.html",{"msg":message})
        
        elif int(data1[0]) == int(data2[0]) :
            message = "0"
            print("equal")
            # return HttpResponseRedirect("/status?msg="+str(message))

            return render(request,"payment1.html",{"msgg":message})

        else:
            diff = int(data2[0]) - int(data1[0]) 
            print(diff)
            no_pre = int(diff)//int(data1[2])
            print(no_pre)
            print("Nodata")
            message = "There are "+str(no_pre)+" more Insurance Premium to pay for completing this insurance application."
        # return HttpResponseRedirect("/payment1?message="+str(message))
            return render(request,"payment1.html",{"msg":message})

    except:
        
        print("Nodata")
        message = "There are  more Insurance Premium to pay for completing this insurance application."
    # return HttpResponseRedirect("/payment1?message="+str(message))
        return render(request,"payment1.html",{"msg":message})

    
    return render(request,"payment1.html")

def payment2(request):
    amt=request.session["amt"] 
    cno= request.session["cardno"]
    if request.POST:

        request.session['t1']=request.POST.get('t1')
        request.session['t2']=request.POST.get('t2')
        request.session['t3']=request.POST.get('t3')
        request.session['t4']=request.POST.get('t4')
        return HttpResponseRedirect("/payment3/")
    return render(request,"payment2.html",{'cno':cno,"amt":amt})

def payment3(request):
  
    if request.POST:
        return HttpResponseRedirect("/payment4/")
    return render(request,"payment3.html")
def payment4(request):
    appl_id= request.session["appl_id"] 
    p_id=request.session["p_id"] 
    com_id=request.session["com_id"] 
    amt=request.session["amt"]
    tdate=now.date()
    cno= request.session["cardno"]
    u_id = request.session["u_id"]

    s= "insert into payment(`u_id`,`c_id`,`policy_id`,`cardno`,`date`,`amount`,`appl_id`) values('"+str(u_id)+"','"+str(com_id)+"','"+str(p_id)+"','"+str(cno)+"','"+str(tdate)+"','"+str(amt)+"','"+str(appl_id)+"')"
    c.execute(s)
    conn.commit()
    print(s)

    
    if request.POST:
        return HttpResponseRedirect("/payment5/")
    return render(request,"payment4.html")
def payment5(request):
  
    t1=request.session['t1']
    tdate=now.date()
    amt=request.session["amt"] 
    return render(request,"payment5.html",{'t1':t1,'tdate':tdate,'Amount':amt})

def list_policy(request):
    com_id = request.GET.get("com_id")
    cat_id = request.GET.get("cat_id")

    # s = "select * from policy where cat_id = '"+str(cat_id)+"' and com_id = '"+str(com_id)+"'"
    # s= "SELECT * FROM policy p ,premium pr, amount a WHERE p.cat_id = '"+str(cat_id)+"' AND p.com_id = '"+str(com_id)+"' AND p.`com_id`= pr.`com_id` AND a.`com_id` = p.`com_id` AND p.premium_id = pr.`pre_id`"
    s = " SELECT * FROM policy p ,premium pr, amount a WHERE p.cat_id = '"+str(cat_id)+"' AND p.com_id = '"+str(com_id)+"' AND p.`com_id`= pr.`com_id` AND a.`com_id` = p.`com_id` AND p.premium_id = pr.`pre_id` AND p.`amount_id` = a.`amt_id`"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)

    return render(request,"list_policy.html",{"data":data})

def apply_policy(request):
    msg = ""
    com_id = request.GET.get("com_id")
    cat_id = request.GET.get("cat_id")
    p_id = request.GET.get("p_id")
    u_id = request.session["u_id"]
    tdate=now.date()
    print(tdate)
    

    if 'apply_policy' in request.POST:
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        s = "select count(*) from applications where name = '"+str(name)+"' and dob = '"+str(dob)+"' and p_id = '"+str(p_id)+"'"
        c.execute(s)
        data = c.fetchone()
        if data[0] == 0 :
            s1 = "insert into applications(`name`,`gender`,`age`,`dob`,`address`,`phone`,`email`,`p_id`,`com_id`,`cat_id`,`u_id`,`status`) values('"+str(name)+"','"+str(gender)+"','"+str(age)+"','"+str(dob)+"','"+str(address)+"','"+str(phone)+"','"+str(email)+"','"+str(p_id)+"','"+str(com_id)+"','"+str(cat_id)+"','"+str(u_id)+"','Applied')"
            c.execute(s1)
            conn.commit()
            msg = "Application Send Successfully"

            s2 = "select p_document from policy where p_id ='"+str(p_id)+"'"
            c.execute(s2)
            data1 = c.fetchone()
            return render(request,"policy_form.html",{"msg":msg,"data1":data1})
        else:
            msg = "Already Applied"
            return render(request,"apply_policy.html",{"msg":msg,"data1":data1})
    return render(request,"apply_policy.html",{"tdate":tdate})

def policy_form(request):
    return render(request,"policy_form.html")


def status(request):
    u_id = request.session["u_id"]

    # msg = request.GET.get("msg")
    s = "SELECT a.apl_id,a.name,a.gender,a.age,a.dob,a.address,a.phone,a.email,a.p_id,a.com_id,a.cat_id,a.u_id,a.status,p.p_id,p.p_name,c.c_id,c.c_name FROM applications a, policy p, company_register c WHERE a.u_id = '"+str(u_id)+"' AND a.`p_id` = p.`p_id` AND a.`com_id` = c.`c_id`"
    c.execute(s)
    print(s)
    data = c.fetchall()
   
    return render(request,"status.html",{"data":data})

def remove_appl(request):
    
    appl_id = request.GET.get("appl_id")
    s ="delete from applications where apl_id = '"+str(appl_id)+"' "
    c.execute(s)
    conn.commit()

    return HttpResponseRedirect("/status")

def view_pay_history(request):
    msg = ""
    u_id = request.session["u_id"]
    appl_id = request.GET.get("appl_id")
    s = "select pay_id,date,amount from payment where appl_id='"+str(appl_id)+"' and u_id='"+str(u_id)+"'"
    print(s)
    c.execute(s)
    data = c.fetchall()
    if not bool(data):
        msg = "No Transaction done yet"
        return render(request,"View_pay_history.html",{"data":data,"msgg":msg})
    return render(request,"View_pay_history.html",{"data":data})
    
def rate_now(request):
    tdate=now.date()
    u_id = request.session["u_id"]
    p_id = request.GET.get("p_id")
    com_id = request.GET.get("com_id")

    s1 = "select u.u_name, r.rating,r.posted_date, r.feedback from rating r, user_register u where r.user_id = u.u_id and  r.p_id = '"+str(p_id)+"'"
    c.execute(s1)
    conn.commit()
    data = c.fetchall()
    print(data)

    if request.POST:
        rating = request.POST.get("rating")
        feed = request.POST.get("feed")
        print(rating)
        ss = "select count(*) from rating where user_id = '"+str(u_id)+"' and p_id = '"+str(p_id)+"'"
        c.execute(ss)
        rate_count = c.fetchone()
        print(rate_count)
        if rate_count[0] == 0:
            s = "insert into rating(`user_id`,`com_id`,`p_id`,`rating`,`posted_date`,`feedback`) values('"+str(u_id)+"', '"+str(com_id)+"','"+str(p_id)+"','"+str(rating)+"','"+str(tdate)+"','"+str(feed)+"')"
            c.execute(s)
            conn.commit()
            msg = "Rating added successfully"
            return render(request,"rate_now.html",{"msgg":msg,})
        else:
            msg = "You have already rated this policy"

            return render(request,"rate_now.html",{"msgg":msg,"data":data})

    return render(request,"rate_now.html",{"data":data})