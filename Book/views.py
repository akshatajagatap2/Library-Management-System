from django.shortcuts import render, redirect
from .models import Book
from .forms import EntryForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('book_list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'Book/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('book_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('book_list')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'Book/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def book_list(request):
    context = {'book_list': Book.objects.all()}
    return render(request, "Book/book_list.html", context)


@login_required(login_url='login')
def Entry_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EntryForm()
        else:
            book = Book.objects.get(pk=id)
            form = EntryForm(instance=book)
        return render(request, "Book/entryForm.html", {'form': form})
    else:
        if id == 0:
            form = EntryForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = EntryForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/')

@login_required(login_url='login')
def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/')
