
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


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        fname =request.POST['fname']
        lname = request.POST['lname']
        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already in use')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'Email already in use')
                return redirect('signup')

            elif username == fname:
                messages.info(request,"Your first name can't be your username")
                return redirect('signup')

            elif username == lname:
                messages.info(request,"Your last name can't be your username")
                return redirect('signup')
            elif pass1 == username:
                messages.info(request,'Using username as password is not allowed')
                return redirect('signup')

        myuser = User.objects.create_user(username,pass1,email)
        myuser.first_name = fname.title()
        myuser.lname = lname.title()
        myuser.save()
        messages.info(request,'Account created succesfully')
        return redirect('/')

    else:
        return render(request, 'signup.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        

        user = authenticate(username=username,password=pass1)
        
        if user is not None:
            auth.login(request,user)
            fname=user.first_name
            messages.info(request,'logged in successfully')
            return redirect('/',{'fname':fname})
        else:
            messages.info(request,'Invalid Credetials')
            return redirect('/')
    
    else:
        return render(request,'login.html')


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