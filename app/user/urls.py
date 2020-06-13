# this file is located in the user paths
# this is different than the urls.py file in the app folder
from django.urls import path
#from user import views
from user import views
app_name = 'user'

urlpatterns = [path('create/', views.CreateUserView.as_view(), name= 'create'),]
