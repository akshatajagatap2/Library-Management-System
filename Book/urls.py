from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('book_entry/', views.Entry_form, name='book_entry'),  # get and post req. for insert operation
    path('<int:id>/', views.Entry_form, name='book_update'),  # get and post req. for update operation
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('', views.book_list, name='book_list')  # get req. to retrieve and display all records
]
