from django.urls import path
from .views import CalendarList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete, TodoList

urlpatterns = [
    path('', CalendarList.as_view(), name='list'),
    path('create/', TodoCreate.as_view(), name = 'create2'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name = 'detail2'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name = 'update2'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name = 'delete2'),
    path('todolist/', TodoList.as_view(), name = 'todolist'),
]