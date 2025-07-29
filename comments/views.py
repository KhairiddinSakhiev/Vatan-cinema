from django.shortcuts import render,redirect
from .models import Comment
from accounts.models import CustomUser
from movies.models import Movie


def create_comment_view(request):
    if request.method == 'GET':
        return render(request,'/')#html
    elif request.method == 'POST':
        user = request.POST.get('user')
        movie = request.POST.get('user')
        description = request.POST.get('description')

        Comment.objects.create(
            user = CustomUser.objects.filter(id=user).first(),
            movie = Movie.objects.filter(id=movie).first(),
            description = description
        )
        return redirect('')#url name 
    

def detail_comment_view(request):
    comment = Comment.objects.all()
    if request.method == 'GET':
        context = {
            "comments":comment
        }
        return render(request,'/',context)#html
    

def update_comment_view(request,pk):
    comment = Comment.objects.filter(id=pk).first()
    if request.method == 'GET':
        return render(request,'/')#html
    elif request.method == 'POST':
        user = request.POST.get('user')
        movie = request.POST.get('user')
        description = request.POST.get('description')

        comment.user = CustomUser.objects.filter(id=user).first()
        comment.movie = Movie.objects.filter(id=movie).first()
        comment.description = description
        comment.save()

        return redirect('')#url name 
    
def delete_comment_view(request,pk):
    comment = Comment.objects.filter(id=pk).first()
    if request.method == 'GET':
        return render(request,'/')#html
    comment.delete()
    return redirect('')#url name