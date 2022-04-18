
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import *
from django.db.models import Q
from django.contrib.auth import authenticate,login
from . forms import *



# Create your views here.
def blogs(request,pk):
    if 'p' in request.GET:
        p = request.GET['p']
        #blog = Blog.objects.filter(blog_name__icontains=q)
        multiple_Q = Q(Q(blog_name__icontains=p)|Q(blog_content__icontains=p)|Q(blog_date__icontains=p))

        blog = Blog.objects.filter(multiple_Q)

    else:

        blog = Blog.objects.get(id=pk)
    context = {'blog':blog}
    return render(request,'blogs.html', context)


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_Q = Q(Q(blog_name__icontains=q)|Q(blog_content__icontains=q)|Q(blog_date__icontains=q))
        blog = Blog.objects.filter(multiple_Q)

    else:
        blog=Blog.objects.all()
    context = {'blog':blog}
    return render(request, 'index.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not  None:
            auth.login(request, user)
            return redirect('/')


        else:
            messages.error(request,'bad credentials')
            return redirect('login')
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass2 = request.POST['pass2']

        if len(username)>10:
            messages.error(request,"username must be at least 10 charaters")
            return redirect('signup')
        if len(username)<3:
            messages.error(request,"username must be greater than 3")
            return redirect('signup')


        if username == fname:
            messages.info(request,"Your first name can't be your username")
            return redirect('signup')

        if username == lname:
            messages.info(request,"Your last name can't be your username")
            return redirect('signup')




        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request,'account created succesfully')
        return redirect('login')
    return render(request, 'signup.html')





def logout(request):
    auth.logout(request)
    messages.info(request,'logged out successfully')
    return redirect('/')

def add_comment(request,pk):
    eachBlog = Blog.objects.get(id=pk)
    form = CommentForm(instance=eachBlog)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachBlog)
        if form.is_valid():
            if  request.user.is_authenticated:
                name=request.user.username
                email = form.cleaned_data['email'];
                body = form.cleaned_data['body'];

                c = Comment(post=eachBlog,name=name,email=email,body=body,created=datetime.now())
                c.save()
                return redirect('index')
            else:
                body = form.cleaned_data['body'];
                name = form.cleaned_data['name'];
                email = form.cleaned_data['email'];
                c = Comment(post=eachBlog,name=name,email=email,body=body,created=datetime.now())
                c.save()
                return redirect('index')
        else:
            print('form is invalid')
    else:
        form = CommentForm()


    context = {
        'form':form
    }
    return render(request,'add_comment.html',context)




def handler404(request,exception):
    return render(request,'404.html')


def join(request):
    return render(request,'join.html')