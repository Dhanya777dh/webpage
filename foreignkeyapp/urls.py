from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.forfun,name='forfun'),
   path('add_course',views.add_course,name='add_course'),
   path('add_student',views.add_student,name='add_student'),
   path('edit/<int:pk>',views.edit,name='edit'),
   path('editdb/<int:pk>',views.editdb,name='editdb'),
   path('delete/<int:pk>',views.delete,name='delete'),

   path('addcourse_db',views.addcourse_db,name='addcourse_db'),
   path('addstudent_db',views.addstudent_db,name='addstudent_db'),
   path('show_details',views.show_details,name='show_details'),

]