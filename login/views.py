from django.shortcuts import render,redirect
import mysql.connector as sql
from login.models import BooksDetails

em = ''
pwd = 0
k_name=""
author_name=""
category=""
quantity = 0


# Creating the login function after succeful login request.
def loginaction(request):
    """ This Function is to store the data into data base after succesful logingup then redirecting it to Add books page , Add password field on line 18 """
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="*********", database='library_system')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = f"select * from admin_info where ad_email='{em}' and password={pwd}"
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return redirect('/addbooks')


    return render(request, 'login_page.html')


def home(request):
    """ This Function is to store the data of books into data base after succesfully adding the book then redirecting it to langing page page , Add password field on line 43 """
    global bk_name, author_name, category, quantity
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="*********", database='library_system')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "bk_name":
                bk_name = value
            if key == "author_name":
                author_name = value

            if key == "quantity":
                quantity = value

        c = f"insert into book_db Values('{bk_name}','{author_name}',{quantity});"
        cursor.execute(c)
        m.commit()
        return redirect('/')

    return render(request, 'welcome.html')




def landing(request):
    """ This Function is to Retrive the data from the database and showing it on landing page"""
    resultsDetails = BooksDetails.objects.all()
    context = {'BooksDetails':resultsDetails}
    return render(request,"landing_page.html",context)