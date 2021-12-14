from django.urls import path

from todo_app.views import todo_list, todo_detail, todo_create

app_name = "todos"

urlpatterns = [
    path("", todo_list),
    path("create/", todo_create),
    path("<id>/", todo_detail), #musí být druhé, jinak by se nenašlo create, create za / by se hledalo jako chybně zadané id
]