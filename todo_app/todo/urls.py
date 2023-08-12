from django.urls import path 
from todo.views import add_task, incomplete_tasks, delete_task, update_task, completed_tasks, mark_completed

urlpatterns = [
    path('', incomplete_tasks, name='incompleted_tasks'),
    path('add_tasks/', add_task, name='add_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('completed_tasks/', completed_tasks, name='completed_tasks'),
    path('mark_completed/<int:task_id>/', mark_completed, name='mark_completed'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]