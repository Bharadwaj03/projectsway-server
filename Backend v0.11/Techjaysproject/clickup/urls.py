from django.urls import path,include
from clickup import views


urlpatterns = [
    path('get_task/',views.get_task, name="get_task"),
    path('task_list/',views.get_task_from_list,name="task_list"),
    path('get_list/',views.get_list,name="get_list"),
    path('tasks/',views.get_filtered_list,name="tasks"),

]
