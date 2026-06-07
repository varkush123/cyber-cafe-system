from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
import mysql.connector as sql

def addcunation(request):
    if request.method == "POST":
        k = sql.connect(host="localhost", user="root", passwd="Varsha@27", database='cyber')
        cursor = k.cursor()
        
        id_no = request.POST.get("id_no") 
        cursor.execute("SELECT * FROM cusd WHERE id_no=%s ", (str(id_no),))
        id_row = cursor.fetchone()
        
        if id_row:
            messages.error(request, 'ID no already exists. Please write a unique ID No.')
        else:
            it = request.POST.get("id_type")
            no = request.POST.get("id_no")
            na = request.POST.get("name")
            ag = request.POST.get("age")
            mn = request.POST.get("mobile_no")
            em = request.POST.get("email")
            ad = request.POST.get("address")
            da = request.POST.get("check_in_datetime")
            ti = request.POST.get("time_spend_minutes")
            ci = request.POST.get("computer_id")

            if da:  # Check if da is not empty
                da_datetime = datetime.strptime(da, '%Y-%m-%d %H:%M:%S')
            else:
                da_datetime = None  # Handle the case when da is empty
            
            q = "INSERT INTO cusd VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(q, (it, no, na, ag, mn, em, ad, da_datetime, ti, ci))
            k.commit()

            messages.success(request, 'Customer details added successfully!')

        return redirect('addcus_html')  # Redirect to the addcus page

    return render(request, 'addcus.html')
