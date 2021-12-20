from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.contrib import messages

from todo_app.forms import TodoForm, TodoForm2, RegistrationForm
from todo_app.models import Todo


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class LoginView(FormMixin, TemplateView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Log in successfully')
            return redirect('/')

        messages.error(request, 'Wrong credentials')
        return redirect('login')


class RegistrationView(FormMixin, TemplateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def post(self, request,  *args, **kwargs):
        registration_data = request.POST
        form = self.form_class(registration_data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account {form.cleaned_data.get("username")} successfully created')
            return redirect('login')
        else:
            messages.error(request, f'Something wrongs')
            return TemplateResponse(request, 'accounts/registration.html', context={'form': form})


def todo_list(request):
    todos = Todo.objects.all().order_by("-create_date")
    context = {
        "todo_list": todos
    }
    return render(request, "todo_app/todo_list.html", context)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo_detail": todo
    }
    return render(request, "todo_app/todo_detail.html", context)


@login_required(login_url='/login/')
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # name = form.cleaned_data["name"]
        # due_date = form.cleaned_data["due_date"]
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo_app/todo_create.html", context)


@login_required(login_url='/login/')
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm2(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo_app/todo_update.html", context)


@login_required(login_url='/login/')
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")