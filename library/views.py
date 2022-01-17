from django.shortcuts import render
from rest_framework import generics
from library.models import Book
# from rest_framework import filters
from rest_framework.filters import SearchFilter
# import django_filters.rest_framework


from library.serializers import BookSerializer
# Create your views here.
class BookList(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class=BookSerializer
	filter_backends =[SearchFilter]
	search_fields=['title', 'author', 'isbn', 'id']
	


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book
	serializer_class=BookSerializer


