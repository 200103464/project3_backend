from  django.urls import path
from . import views
urlpatterns=[

    path('',views.main,name = 'home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('send/', views.send_message, name='sendmessage'),
]
