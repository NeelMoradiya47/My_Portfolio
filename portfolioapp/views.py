from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact, Projects

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about_me.html')

def projects(request):
    return render(request, 'projects.html')

def contact_me(request):
    return render(request, 'contact_me.html')

def insert_data(request):
    if request.method == 'POST':
        try:
            name = request.POST['user_name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']

            data = Contact(name=name, email_id=email, mobile_no=mobile, message=message)
            data.save()

            return render(request, 'contact_me.html')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
