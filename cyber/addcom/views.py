from django.shortcuts import render
#from addcom.models import Addcom
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

@method_decorator(csrf_protect, name='dispatch')
class addcomation(TemplateView):
    template_name = 'addcom.html'
import mysql.connector as sql
ci=''
cn=''
co=''
ty=''
mo=''
se=''
ra=''

# Create your views here.
def addcomation(request):
    global ci,cn,co,ty,mo,se,ra
    if request.method=="POST":
        v=sql.connect(host="localhost",user="root",passwd="Varsha@27",database='cyber')
        cursor=v.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="computer_id":
                ci=value
            if key=="computer_name":
                cn=value
            if key=="company":
                co=value
            if key=="type":
                ty=value
            if key=="model_no":
                mo=value
            if key=="series":
                se=value
            if key=="ram":
                ra=value
        
        r="insert into computers values({},'{}','{}','{}','{}','{}','{}')".format(ci,cn,co,ty,mo,se,ra)
        cursor.execute(r)
        v.commit()
    #comps = Addcom.objects.all()    
    return render(request,'addcom.html')