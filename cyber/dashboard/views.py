from django.shortcuts import render

# Create your views here.
def dashnation(request):
    return render(request,'dashboard.html')