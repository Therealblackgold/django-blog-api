from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializer
from django.shortcuts import render, get_object_or_404


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


def homepage(request):
    # creating blogs variable to hold blogs from the database
    blogs = Blog.objects.order_by("-date")
    # creating context to display blogs on blogs html page
    context = {"blogs": blogs}
    # return request and displaying blogs on blogs.html
    return render(request, "home.html", context)
