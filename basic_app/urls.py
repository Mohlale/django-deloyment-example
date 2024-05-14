from django.urls import path
from basic_app import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('user_login',views.user_login,name='user_login')
]
