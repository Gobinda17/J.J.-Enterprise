from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    if request.method == "POST" :
        name = request.POST['name']
        company_name = request.POST['company']
        email = request.POST['email_id']
        phone = request.POST['phone']
        message = request.POST['message']
        date = request.POST['date']
        ins = Contact(name = name, company_name = company_name, email = email, phone = phone, message = message, date = date)
        ins.save()

    return render(request, 'home.html')
        

