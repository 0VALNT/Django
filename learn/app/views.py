from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class BookList(ListView):
    model = Book
    fields = '__all__'
    template_name = 'book_list.html'
    context_object_name = "books"


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'create_book.html'
    success_url = reverse_lazy('index')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'create_book.html'
    success_url = reverse_lazy('index')


class BookDelete(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy('index')
