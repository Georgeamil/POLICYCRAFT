from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
import simplejson as json
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
import smtplib 
import urllib.request


conn = MySQLdb.connect("localhost","root","","policy_craft")
c = conn.cursor()

# Create your views here.

def index(request):
    msg = ""
    if 'u_register' in request.POST:
        u_name = request.POST.get("u_name")
        u_last_name = request.POST.get("u_last_name")
        u_email = request.POST.get("u_email")
        u_address = request.POST.get("u_address")
        u_phone = request.POST.get("u_phone")
        u_gender = request.POST.get("u_gender")
        u_dob = request.POST.get("u_dob")
        password = request.POST.get("password")

        u_full_name = u_name.strip()+" "+u_last_name.strip()
        print(u_full_name)
       

        c_count = "select count(*) from user_register where u_email = '"+str(u_email)+"' and  u_phone = '"+str(u_phone)+"'"
        c.execute(c_count)
        conn.commit()
        data = c.fetchone()
        if data[0] == 0:
            s = "insert into user_register(`u_name`,`u_email`,`u_address`,`u_phone`,`u_gender`,`u_dob`) values('"+str(u_full_name).strip()+"','"+str(u_email)+"','"+str(u_address)+"','"+str(u_phone)+"','"+str(u_gender)+"','"+str(u_dob)+"')"
            c.execute(s)
            conn.commit()

            s1 = "insert into login(`reg_id`,`email`,`password`,`type`) values((select max(u_id) from user_register),'"+str(u_email)+"','"+str(password)+"','user')"
            c.execute(s1)
            conn.commit()
            msg = "User Registered Successfully"
            return render(request,"index.html",{"msg":msg})
        else: 
            msg = "Account Already Exists"
            return render(request,"index.html",{"msg":msg})

    if 'c_register' in request.POST:
        c_name = request.POST.get("c_name")
        c_reg_no = request.POST.get("c_reg_no")
        c_email = request.POST.get("c_email")
        c_address = request.POST.get("c_address")
        c_phone = request.POST.get("c_phone")
        # c_doc = request.POST.get("c_doc")
        password = request.POST.get("password")
        myfile = request.FILES["c_doc"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        c_count = "select count(*) from company_register where c_email = '"+str(c_email)+"' and c_reg_no = '"+str(c_reg_no)+"'"
        c.execute(c_count)
        conn.commit()
        data = c.fetchone()
        if data[0] == 0:
            s = "insert into company_register(`c_name`,`c_reg_no`,`c_email`,`c_address`,`c_phone`,`c_doc`) values('"+str(c_name)+"','"+str(c_reg_no)+"','"+str(c_email)+"','"+str(c_address)+"','"+str(c_phone)+"','"+str(uploaded_file_url)+"')"
            c.execute(s)
            conn.commit()

            s1 = "insert into login(`reg_id`,`email`,`password`,`type`) values((select max(c_id) from company_register),'"+str(c_email)+"','"+str(password)+"','company')"
            c.execute(s1)
            conn.commit()
            msg = "Company Registered Successfully"
            return render(request,"index.html",{"msg":msg})
        else: 
            msg = "Account Already Exists"
            return render(request,"index.html",{"msg":msg})


    if 'login' in request.POST:
        try:
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            s = "select * from login where email='"+str(user_name)+"' and password='"+str(password)+"' and status='1' and count<3 "
            print(s)
            c.execute(s)
            conn.commit()
            log_count = c.fetchone()
            print(log_count)
            if log_count[5] == "admin":
                return HttpResponseRedirect("/admin_home")
            elif log_count[5] == "user":
                request.session["u_id"]=log_count[1]
                # request.session["username"]=log_count[2]
                # request.session["type"]=log_count[4]
                return HttpResponseRedirect("/user_home")
            elif log_count[5] == "company":
                request.session["com_id"]=log_count[1]
                print(log_count[1])
                # request.session["username"]=log_count[2]
                # request.session["type"]=log_count[4]
                return HttpResponseRedirect("/com_home")
            else:
                msg = "Invalid User"
                return render(request,"index.html",{"msg":msg}) 
        
        except:
            msg = "Invalid User"
            return render(request,"index.html",{"msg":msg})

    return render(request,"index.html",{"msg":msg})

#-----------------Admin page---------------#

def admin_header_footer(request):
    return render(request,"admin_header_footer.html")

def admin_home(request):
    return render(request,"admin_home.html")

def approve_company(request):
    msgg = ""
    s = "select * from company_register c , login l where c.c_id = l.reg_id and l.status = 0"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(s)
    if not bool(data):
        msgg = "No new Company registrations..."
    return render(request,"approve_company.html",{"data":data,"msgg":msgg})

def approve_com(request):
    reg_id = request.GET.get("reg_id")
    s = "update login set status = '1' where reg_id = '"+str(reg_id)+"'"
    c.execute(s)
    conn.commit()
    return HttpResponseRedirect("/approve_company")

def view_company(request):
    msgg = ""
    s = "select * from company_register c , login l where c.c_id = l.reg_id and l.status = 1"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(s)
    if not bool(data):
        msgg = " No Company list to show..."
    return render(request,"view_company.html",{"data":data,"msgg":msgg})

def remove_com(request):
    reg_id = request.GET.get("reg_id")
    s = "delete from company_register where c_id = '"+str(reg_id)+"'"
    # s = "delete login set status = '1' where reg_id = '"+str(reg_id)+"'"
    c.execute(s)
    conn.commit()
    s1 = "delete from login where reg_id = '"+str(reg_id)+"'"
    c.execute(s1)
    conn.commit()
    return HttpResponseRedirect("/view_company")

def approve_user(request):
    msgg=""
    s = "select * from user_register u , login l where u.u_id = l.reg_id and l.status = 0"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(s)
    if not bool(data):
        msgg = "No new User registrations..."
    return render(request,"approve_user.html",{"data":data,"msgg":msgg})

def approve_us(request):
    reg_id = request.GET.get("reg_id")
    s = "update login set status = '1' where reg_id = '"+str(reg_id)+"'"
    c.execute(s)
    conn.commit()
    return HttpResponseRedirect("/approve_user")

def view_user(request):
    msgg = ""
    s = "select * from user_register u , login l where u.u_id = l.reg_id and l.status = 1"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(s)
    if not bool(data):
        msgg = " No User List to show..."
    return render(request,"view_user.html",{"data":data,"msgg":msgg})
def block(request):
    reg_id = request.GET.get("reg_id")
    st="blocked"
    s = "update  login set bstatus='"+str(st)+"' where reg_id = '"+str(reg_id)+"'"
    # s = "delete login set status = '1' where reg_id = '"+str(reg_id)+"'"
    c.execute(s)
    conn.commit()
    
    return HttpResponseRedirect("/view_user")
def remove_us(request):
    reg_id = request.GET.get("reg_id")
    s = "delete from user_register where u_id = '"+str(reg_id)+"'"
    # s = "delete login set status = '1' where reg_id = '"+str(reg_id)+"'"
    c.execute(s)
    conn.commit()
    s1 = "delete from login where reg_id = '"+str(reg_id)+"'"
    c.execute(s1)
    conn.commit()
    return HttpResponseRedirect("/view_company")


def add_category(request):
    msg = ""

    qry1 = "select * from category"
    c.execute(qry1)
    cat_data = c.fetchall()
    if 'add_category' in request.POST:
        category = request.POST.get("category")
        ss = "select count(*) from category where cat_name= '"+str(category)+"'"
        c.execute(ss)
        data = c.fetchone()
        if data[0] == 0 :
            print(category)
            s = "insert into category(`cat_name`) values('"+str(category)+"')"
            c.execute(s)
            conn.commit()   
            msg = "Category Added Successfully"
            return render(request,"add_category.html",{"msg":msg,"cat_data":cat_data})

        else: 
            msg = "Category already Exists"
            return render(request,"add_category.html",{"msg":msg,"cat_data":cat_data})
    return render(request,"add_category.html",{"msg":msg,"cat_data":cat_data})

def admin_view_policy(request):
    msgg = ""
    print("admin")
    qry1 = "select * from category"
    c.execute(qry1)
    cat_data = c.fetchall()

    qry2 = "select * from company_register"
    c.execute(qry2)
    com_data = c.fetchall()

    if 'submit' in request.POST:
        category = request.POST.get("category")
        company = request.POST.get("company")

        s= "SELECT * FROM policy p ,premium pr, amount a WHERE p.cat_id = '"+str(category)+"' AND p.com_id = '"+str(company)+"' AND p.`com_id`= pr.`com_id` AND a.`com_id` = p.`com_id` AND p.premium_id = pr.`pre_id` AND a.`amt_id` = p.`amount_id`"
        print(s)
        c.execute(s)
        conn.commit()
        data = c.fetchall()
        print(data)
        if not bool(data):
            msgg = " No Policy List to show..."
        return render(request,"admin_view_policy.html",{"cat_data":cat_data,"com_data":com_data,"data":data,"msgg":msgg})

        
    return render(request,"admin_view_policy.html",{"cat_data":cat_data,"com_data":com_data})


def logout(request):
    return render(request,"logout.html")