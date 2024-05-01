# # portfolio/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
    
#     path('contact/', views.contact, name='contact'),
#     path('login/', views.user_login, name='login'), 
#     path('register/', views.register, name='register'),
#     path('logout/', views.user_logout, name='logout'),
#     path('submit_contact/', views.submit_contact, name='contact_submit'),
#     path('project_details/', views.project_details, name='project_details'),
#       path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'), 
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('submit_contact/', views.submit_contact, name='contact_submit'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),

]
