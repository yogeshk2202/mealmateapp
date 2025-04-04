from django.urls import path,include
from . import views

app_name = 'delivery' 
urlpatterns = [
    path('',views.index, name = "index"),
    path('signin/',views.sign_in, name="sign_in"),
    path('signup/',views.sign_up, name="sign_up"),
    path('handle_signin/',views.handle_signin, name= "handle_signin"),
    path('handle_signup/',views.handle_signup, name= "handle_signup"),
]