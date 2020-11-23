from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path(r'task/', TaskListView, name = 'task_veiw_url'),
    path(r'task/<int:id>', TaskDetailView, name = 'task_detail_url'),
    path(r'task/create', TaskCreateView, name = 'task_create_url'),
]