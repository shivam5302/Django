from django.shortcuts import render,HttpResponse,redirect
from Home.models import contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    # return HttpResponse("from Home")
    return render(request,'home/home.html')

def about(request):
    # return HttpResponse("from about")
    return render(request,'home/about.html') 

def Contact(request):
    # return HttpResponse("from contact")
    
    if(request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['content']
        if len(name)<2 or len(email)<2 or len(phone)<10 or len(msg)<4:
            messages.error(request, 'please fill correct values')
        else:     
            messages.success(request, 'your problem is submitted')
            contact1 = contact(name=name,email=email,phone=phone,content=msg)
            contact1.save()
       
    return render(request,'home/contact.html')       

def search(request):
    # allPost = Post.objects.all()
    query = request.GET['query']
    if len(query) >70:
        allPost = Post.objects.none()
    else:    
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)
    # if(allPost.count()==0):
    #     message.error(requet,"please write correct url")    
    params = {'allPost': allPost}
    return render(request,'home/search.html',params)   

def handleSignUp(request):

    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myUser = User.objects.create_user(uname,email,pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        messages.success(request, 'your problem is submitted')
        # redirect('Home')
        return render(request,'home/home.html')
        # return render(request,"/")
    else:
        return HttpResponse('404 - not Found!')       

def handleLogIn(request):
      if request.method=='POST':
        loginuname = request.POST['loginuname']
        loginpass1 = request.POST['loginpass1']
        user = authenticate(username=loginuname,password=loginpass1)
        if user is not None:
            login(request,user)
            messages.success(request, 'your problem is submitted')
            return render(request,'home/home.html')
        else:
            messages.error(request,"invalid credential")    
            return render(request,'home/home.html')
    

def handleLogOut(request):
    logout(request)
    messages.success(request, 'you successfully logout!')
    return redirect('Home')
    # return HttpResponse("logout")                