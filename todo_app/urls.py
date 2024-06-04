from django.urls import path
from .views import register, login_view, logout_view, task_list, task_create, task_update, task_delete, task_complete

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('task_list/', task_list, name='task_list'),
    path('task/create/', task_create, name='task_create'),
    path('task/<int:pk>/update/', task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/<int:pk>/complete/', task_complete, name='task_complete'),

]
