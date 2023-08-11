from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_books')
    else:
        book = BookStoreForm()
    return render(request, 'store_and_update_book.html', {'form': book})

def show_books(request):
    books = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'books': books})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'store_and_update_book.html', {'form': form})

def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('show_books')