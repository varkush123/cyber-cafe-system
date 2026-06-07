from django.shortcuts import render
import mysql.connector as sql

# Function to handle billing operation
def calculate_billing(request):
    if request.method == "POST":
        id_no = request.POST.get("id_no")
        k = sql.connect(host="localhost", user="root", passwd="Varsha@27", database='cyber')
        cursor = k.cursor()
        cursor.execute("SELECT id_no, time_spend_minutes, (time_spend_minutes * 15) AS total_billing FROM cusd WHERE id_no=%s", (str(id_no),))
        #calculate_billing = cursor.fetchone()
        calculate_billing = cursor.fetchall()
        if calculate_billing:
            row = calculate_billing[0] 
            id_no = row[0]
            time_spend_minutes = row[1]
            total_billing = row[2]
        cursor.close()
        k.close()
            
            

        # Calculate billing amount (e.g., 30 times time_spend_minutes)
        
        # Render the template with billing amount
        return render(request, 'billing.html', {'id_no': id_no, 'time_spend_minutes': time_spend_minutes, 'total_billing': total_billing})
    else:
        # Redirect or handle the case where there's no POST request
        return render(request, 'billing.html')