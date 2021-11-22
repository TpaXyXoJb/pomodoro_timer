from django.urls import path, include
from .views import TasksView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView, delete_tasks, \
    LoopDetailView ,LoopCreateView, LoopUpdateView, LoopDeleteView, delete_loops

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('task/', TasksView.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/all/delete/', delete_tasks, name='task_delete_all'),
    path('loop/<int:pk>/', LoopDetailView.as_view(), name='loop_detail'),
    path('loop/new/', LoopCreateView.as_view(), name='loop_new'),
    path('loop/<int:pk>/edit', LoopUpdateView.as_view(), name='loop_edit'),
    path('loop/<int:pk>/delete', LoopDeleteView.as_view(), name='loop_delete'),
    path('loop/finished/delete', delete_loops, name='loop_delete_finished'),

]
