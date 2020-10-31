from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    # return HttpResponse("from blogHome")
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)   
    context = {'post':post,'comments':comments,'user':request.user,'repDict': repDict}
    return render(request,'blog/blogPost.html',context)

def PostComment(request):
    if request.method=='POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno=="":
            comment = BlogComment(comment=comment,post=post,user=user)
            comment.save()
            messages.success(request,"your comment has been posted successfully!")            
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,post=post,user=user,parent=parent)
            comment.save()
            messages.success(request,"your replay has been posted successfully!")
    return redirect(f"/blog/{post.slug}")
    