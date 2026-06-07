from django.shortcuts import render

# Create your views here.
import mysql.connector as sql

def customer_details(request):
    if request.method == "POST":
        id_no = request.POST.get("id_no") 
        k = sql.connect(host="localhost", user="root", passwd="Varsha@27", database='cyber')
        cursor = k.cursor()
        cursor.execute("SELECT * FROM cusd WHERE id_no=%s", (str(id_no),))
        customer_details = cursor.fetchone()
        if customer_details:
            customer_details = {
                'id_type': customer_details[0],
                'id_no': customer_details[1],
                'name': customer_details[2],
                'age': customer_details[3],
                'mobile_no': customer_details[4],
                'email': customer_details[5],
                'address': customer_details[6],
                'check_in_datetime': customer_details[7],
                'time_spend_minutes': customer_details[8],
                'computer_id': customer_details[9],
                
            }
            return render(request, 'cus_det.html', {'customer_details': customer_details})
        else:
            return render(request, 'cus_det.html', {'error_message': 'Customer with ID number {} does not exist.'.format(id_no)})
    else:
        return render(request, 'cus_det.html')

def billnation(request):
    if request.method == "POST":
        id_no = request.POST.get("id_no")
        time_spend_minutes = request.POST.get("time_spend_minutes")
        
        # Calculate billing amount (e.g., 30 times time_spend_minutes)
        billing_amount = 30 * str(time_spend_minutes)
        
        # Render the template with billing amount
        return render(request, 'cus_det.html', {'customer_details': None, 'billing_amount': billing_amount})
    else:
        # Redirect or handle the case where there's no POST request
        return render(request, 'cus_det.html')