from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request, 'delivery/sign_up.html')

def handle_signin(request):
    user = 'Yogesh'
    pasw = 'Yogesh@123'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user == username and password == pasw:
            return render(request,'delivery/success.html')
        else:
            return render(request,'delivery/failed.html')
    else:
        return HttpResponse('Invalid Request')
    
def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        data = {
            'username' : username,
            'password' : password,
            'email' : email,
            'mobile' : mobile,
            'address' : address,
        }
        return render(request, 'delivery/userdata.html',data)
    else:
        return HttpResponse('Invalid Request')