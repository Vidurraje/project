from django.shortcuts import render,redirect
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = 0


# Creating the views for signaction after click the signup button

def signaction(request):
    """ This Function is to store the data into data base after succesful signing up then redirecting it to login page , Add password field on line 16 """
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="*********", database='library_system')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = f"insert into admin_info values('{fn}','{ln}','{em}',{pwd});"
        cursor.execute(c)
        m.commit()
        return redirect('/login')

        # if True:
        #     return render(request,'login_page.html')

    return render(request, 'signup_page.html')

