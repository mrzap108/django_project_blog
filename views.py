from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


#this is not needed anymore because there is already a query for the database

#dummy data, fake post
# posts = [
#     {
#         'author': 'Zante Palermo',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'October 5, 2021'
#     },
#     {
#         'author': 'Rhea Palermo',
#         'title': 'Blog Post 2',
#         'content': 'Marketing Post Content',
#         'date_posted': 'September 5, 2021'
#     }
# ]

def home(request):      #example of a function
    #return HttpResponse('<h1> Blog Home</h1>')
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)    #blog is folder inside template folder

def about(request):
    #return HttpResponse('<h1> Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})