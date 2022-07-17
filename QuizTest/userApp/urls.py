from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('quizStartPage/<id>',views.quizStartPage),
    path('TestPage/<id>',views.TestPage),
    path('login',views.login),
    path('logout',views.logout),
    path('signUp',views.signUp),
    path('performance',views.performance),
    path('viewResult/<id>',views.viewResult),
]
    