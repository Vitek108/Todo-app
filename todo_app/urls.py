from django.urls import path

from todo_app.views import todo_list, todo_detail, todo_create, todo_update, todo_delete

app_name = "todos"

urlpatterns = [
    path("", todo_list),
    path("create/", todo_create),
    path("<id>/", todo_detail), #musí být druhé, jinak by se nenašlo create, create za / by se hledalo jako chybně zadané id
    path("<id>/update/", todo_update),
    path("<id>/delete/", todo_delete),
]