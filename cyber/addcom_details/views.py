from django.shortcuts import render

# Create your views here.
import mysql.connector as sql

def computer_details(request):
    if request.method == "POST":
        computer_id = request.POST.get("computer_id") 
        k = sql.connect(host="localhost", user="root", passwd="Varsha@27", database='cyber')
        cursor = k.cursor()
        cursor.execute("SELECT * FROM computers WHERE computer_id=%s", (str(computer_id),))
        computer_details = cursor.fetchone()
        if computer_details:
            computer_details = {
                'computer_id': computer_details[0],
                'computer_name': computer_details[1],
                'company': computer_details[2],
                'type': computer_details[3],
                'model_no': computer_details[4],
                'series': computer_details[5],
                'ram': computer_details[6],
                
            }
            return render(request, 'com_det.html', {'computer_details': computer_details})
        else:
            return render(request, 'com_det.html', {'error_message': 'Computer with ID number {} does not exist.'.format(computer_id)})
    else:
        return render(request, 'com_det.html')

