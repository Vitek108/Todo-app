from django.urls import path

from todo_app.views import todo_list, todo_detail, todo_create, todo_update, todo_delete, LoginView, RegistrationView, LogoutView

app_name = "todos"

urlpatterns = [
    path("", todo_list),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("create/", todo_create),
    path("<id>/", todo_detail), #musí být druhé, jinak by se nenašlo create, create za / by se hledalo jako chybně zadané id
    path("<id>/update/", todo_update),
    path("<id>/delete/", todo_delete),
]