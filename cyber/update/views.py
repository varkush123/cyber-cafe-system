from django.shortcuts import render, redirect
from django.contrib import messages
import mysql.connector as sql

def update_customer_by_id(request):
    if request.method == 'POST':
        try:
            k = sql.connect(host="localhost", user="root", passwd="var1234", database='cyber')
            cursor = k.cursor()

            id_no = request.POST['id_no']
            id_type = request.POST['id_type']
            name = request.POST['name']
            age = request.POST['age']
            mobile_no = request.POST['mobile_no']
            email = request.POST['email']
            address = request.POST['address']
            check_in_datetime = request.POST['check_in_datetime']
            time_spend_minutes = request.POST['time_spend_minutes']
            computer_id = request.POST['computer_id']

            # Execute SQL UPDATE statement based on id_no
            cursor.execute(
                "UPDATE cusd SET id_type = %s, name = %s, age = %s, mobile_no = %s, email = %s, address = %s, check_in_datetime = %s, time_spend_minutes = %s, computer_id = %s WHERE id_no = %s",
                [id_type, name, age, mobile_no, email, address, check_in_datetime, time_spend_minutes, computer_id, id_no]
            )

            # Commit the changes to the database
            k.commit()

            messages.success(request, 'Customer details updated successfully!')
            return redirect('dashboard.html')  # Redirect to dashboard or any other page

        except Exception as e:
            # If an error occurs, rollback the changes and display an error message
            k.rollback()
            messages.error(request, f'An error occurred: {e}')

        finally:
            # Close the database connection
            k.close()

    else:
        return render(request, 'update.html')
