from django.shortcuts import render
from django.contrib import messages
import mysql.connector as sql

def logination(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Assuming your MySQL connection is working properly
        m = sql.connect(host="localhost", user="root", passwd="Varsha@27", database='cyber')
        cursor = m.cursor()
        cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            return render(request, 'dashboard.html')
        else:
            messages.error(request, 'Incorrect username or password. Please try again.')

    return render(request, 'login.html')
