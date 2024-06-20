from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate
# from .models import login_detail
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate,logout
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_started():
    return redirect("/form")


def form(request):
    return render(request, 'form.html')

# def login_view(request):
#      if request.method == "POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
        
#         # check if user has entered correct creditentals or not
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/dashboard")
           
#         else:
#             return redirect("/")
        
# def logout_view(request):
#     logout(request)
#     return redirect('/form')

def dashboard(request):
    return render(request, 'dashboard.html')

def issueBook(request):
    return render(request, 'issueBook.html')

    
  
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books.html', {'books': books})

def books(request):
    # return render(request, 'books.html')
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def add_book(request):
    book_item =(title = request.POST['title'],
                 author = request.POST['author'],
                 type = request.POST['types'],
                 quantity = request.POST['quantity'])
    book_item.save()
    return redirect('/books')

def students(request):
    return render(request, 'student.html')

def reports(request):
    return render(request, 'reports.html')

def settings(request):
    return render(request, 'settings.html')