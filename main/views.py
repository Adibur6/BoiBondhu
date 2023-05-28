from email import message
from turtle import mode

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import models
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from datetime import datetime,date




def logout_view(request):
  logout(request)
  return redirect('home')

def home(request):
  flg=False
  log_in=False
  notify=False
  text=''
  if request.method=='POST' and 'sign-up' in request.POST:
    newuser=models.User.objects.filter(username=request.POST['username'] )
    if len(newuser)>0 :
      text='Already username exists'
      flg=True
    else:  
      flg=True
      username=request.POST['username'] 
      email=request.POST['email'] 
      password1=request.POST['password1'] 
      password2=request.POST['password2'] 
      if password1!=password2:
        text="Passwords don't match."      
      elif len(password1)<8:
        text="Passwords too short."
      else:
        user = User.objects.create_user(username=username,email=email, password=password1)
        user.save()
        text="New user created."
  elif request.method=='POST' and 'login' in request.POST:
    
    username=request.POST['username'] 
    password=request.POST['password'] 
    user=authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
    else:
      flg=True
      text="User doesn't exist"
  username=''
  if request.user.is_authenticated:
    log_in=True
    ppp=models.profile.objects.get_or_create(user=request.user)
    if request.user.profile.first_name is None:
      username=request.user.username
    else:
      username=request.user.profile.first_name+' '+request.user.profile.last_name
    notify=request.user.profile.notify


  context={
    'flg':flg,
    'login':log_in,
    'message':text,
    'username':username,
    'notify':notify
    }
    


  return render(request,'home/index.html',context)

def about_us(request):
  login=False
  notify=False
  if request.user.is_authenticated:
    login=True
    notify=request.user.profile.notify
    
  context={
    
    'login':login,
    'notify':notify
    
  }
    

  return render(request,'about us/index.html',context)

def how_to_swap(request):
  login=False
  notify=False
  
  if request.user.is_authenticated:
    login=True
    notify=request.user.profile.notify
    
  context={
    
    'login':login,
    'notify':notify
    
  }
  return render(request,'how-to-swap/index.html',context)

def profile(request):
  user=User.objects.get(username=request.user.username)
  
  userprofile,created=models.profile.objects.get_or_create(user=user)
  userimg,created=models.profile_image.objects.get_or_create(user=user)
  img_url=''
  if userimg.img:
    img_url=userimg.img.url
  
  

  
  fullname=''
  if userprofile.first_name is not None and userprofile.last_name is not None:
    fullname=userprofile.first_name+' '+ userprofile.last_name

    
    


  context={
    'img_url':img_url,
    'username':user.username,
    'fullname':fullname,
    'total_coins':userprofile.total_coins,
    'books_recieved':userprofile.books_recieved,
    'books_shared':userprofile.books_shared,
    'first_name':userprofile.first_name,
    'last_name':userprofile.last_name,
    'location':userprofile.location,
    'email':user.email,
    'profession':userprofile.profession,
    'phone':userprofile.phone,
    'birthday':userprofile.birthday,
    'workplace':userprofile.workplace,
    'about':userprofile.about,
    'facebook':userprofile.facebook,
    'insta':userprofile.insta,
    'twitter':userprofile.twitter,
    'pinterest':userprofile.pinterest,
    'notify':request.user.profile.notify
    


  }
  return render(request,'profile/index.html',context)

def blogs(request):
  login=False
  notify=False
  
  if request.user.is_authenticated:
    login=True
    notify=request.user.profile.notify
    
  context={
    'login':login,
    'notify':notify
  }
  return render(request,'blogs/index.html',context)
    
    

def edit_profile(request):
  user=User.objects.get(username=request.user.username)
  pass_error=''
  userprofile,created=models.profile.objects.get_or_create(user=user)
  userimg,created=models.profile_image.objects.get_or_create(user=user)
  img_url=''
  if userimg.img:
    img_url=userimg.img.url
  
  if request.method == 'POST' and 'img-upload' in request.POST:
    userimg.img = request.FILES['img1']
    userimg.save()
    img_url=userimg.img.url   
    img_name=userimg.img.name 
    
  elif request.method=="POST":
    userprofile.first_name=request.POST['first_name']
    userprofile.last_name=request.POST['last_name']
    userprofile.location=request.POST['location']
    userprofile.about=request.POST['about']
    userprofile.profession=request.POST['profession']
    print(request.POST['birthday'])
    userprofile.birthday=request.POST['birthday']
    if request.POST['password1']:
      if len(request.POST['password1'])<8:
        pass_error="Password less than 8 characters"
      elif request.POST['password1']!=request.POST['password2']:
        pass_error="Password doesn't match"
      else:
        user.set_password(request.POST['password1'])
        user.save()
        login(request,user)
    userprofile.phone=request.POST['phone']
    userprofile.facebook=request.POST['facebook']
    userprofile.insta=request.POST['insta']
    userprofile.twitter=request.POST['twitter']
    userprofile.pinterest=request.POST['pinterest']
    userprofile.workplace=request.POST['workplace']
    user.email=request.POST['email']
    user.save()
    userprofile.save()
  
  

  
  fullname=''
  if userprofile.first_name is not None and userprofile.last_name is not None:
    fullname=userprofile.first_name+' '+ userprofile.last_name

    
    


  context={
    'img_url':img_url,
    'username':user.username,
    'pass_error':pass_error,
    'fullname':fullname,
    'first_name':userprofile.first_name,
    'last_name':userprofile.last_name,
    'location':userprofile.location,
    'email':user.email,
    'profession':userprofile.profession,
    'phone':userprofile.phone,
    'birthday':userprofile.birthday,
    'workplace':userprofile.workplace,
    'about':userprofile.about,
    'facebook':userprofile.facebook,
    'insta':userprofile.insta,
    'twitter':userprofile.twitter,
    'pinterest':userprofile.pinterest,
    'notify':request.user.profile.notify
    


  }
  return render(request,'edit-profile/index.html',context)


def browsing(request,category='all',page=1):
  login=False
  msg=''
  notify=False
  if request.user.is_authenticated:
    login=True
    notify=request.user.profile.notify
  
  if request.method=="POST" and 'not-interested' in request.POST:
    rev,created=models.interest.objects.get_or_create(book_instance=request.POST['not-interested'],user=request.user)
    rev.interest_value=rev.interest_value+1
    rev.save()
 
  if request.method=="POST" and 'query' in request.POST:
    book_instances=models.book_instances.objects.filter(is_recieved=False,bookname__icontains=request.POST['query']).order_by('-post_date')
    category='query'+request.POST['query']
    msg="Search Results For : "+request.POST['query']
    if len(book_instances)==0:
      msg=msg+' (No matches found)'
  elif category[:5]=='query':
    book_instances=models.book_instances.objects.filter(is_recieved=False,bookname__icontains=category[5:]).order_by('-post_date') 
    msg="SEARCH RESULTS FOR: "+category[5:]
  elif category=="all":
    book_instances=models.book_instances.objects.filter(is_recieved=False).order_by('-post_date') 
  else:
    book_instances=models.book_instances.objects.filter(is_recieved=False,category__icontains=category).order_by('-post_date') 
  
  if login:
    book_instances = sorted(book_instances, key=lambda x: models.interest.objects.get_or_create(book_instance=x,user=request.user)[0].interest_value)
  
  req_list=[]
  is_my_book=[]
  rating_list=[]
  
  p=Paginator(book_instances,4)
  booklist=p.get_page(page)
  for book in booklist:
    reqp=False
    if login:
      req,created=models.req_user.objects.get_or_create(user=request.user,book=book)
      reqp=req.req
      print(req.book)
      print(req.req)
      is_my_book.append(book.owner==request.user)
    else:
      reqp=False
      is_my_book.append(True)
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    rating_list.append((sum,int(book.price*.25)))


    
    
    req_list.append(reqp)
  booklist1=zip(is_my_book,booklist,req_list,rating_list)
    
  context={
    
    'user':request.user,
    'category':category,
    'book_instances':booklist1,
    'p':booklist,  #paginator
    'login':login,
    'msg':msg,
    'notify':notify
    
    
  }
  return render(request,'browsing/index.html',context)

def check(request):
  return render(request,'check.html')

def add_books(request):
  user=User.objects.get(username=request.user.username)
  fullname=user.username
  if user.profile.first_name is not None and user.profile.last_name is not None:
    fullname=user.profile.first_name+' '+ user.profile.last_name
  text=''
  if request.method =="POST":
    boook,created=models.book.objects.get_or_create(isbn=request.POST["isbn"])
    instance=models.book_instances()
    instance.bookname=request.POST['bookname']
    if boook.name is None:
      boook.name=request.POST['bookname']
    instance.author=request.POST['author']
    if boook.author is None:
      boook.author=request.POST['author']
    instance.publisher=request.POST['publisher']
    if boook.publisher is None:
      boook.publisher=request.POST['publisher']
    
    instance.pubdate=request.POST['date']
    if boook.pubdate is None:
      boook.pubdate=request.POST['date']
    instance.edition=request.POST['edition']
    instance.age=request.POST['age']
    if 'hardcover' in request.POST:
      instance.hard_cover=True
    if 'paperback' in request.POST:
      instance.paper_back=True
    cc=request.POST.getlist('category')

    instance.category=", ".join(cc)
    instance.price=request.POST['price']      
    instance.details=request.POST['details']
    if 'img' in request.FILES:
      instance.img=request.FILES['img']
    text="Successfully added"
    instance.owner=user
    instance.book=boook
    instance.save()
    boook.save()



  context={
    'user':user,
    'text':text,
    'img_url':user.profile_image.img.url,
    'username':fullname,
    'about':user.profile.about,
    'notify':request.user.profile.notify
  }
  return render(request,'add_books/index.html',context)







def read_more(request,pk):
  login=False
  book=models.book_instances.objects.get(id=pk)
  req,created=models.req_user.objects.get_or_create(user=request.user,book=book)
  
  is_my_book=(book.owner==request.user)
  msg=''
 
  if request.user.is_authenticated:
    login=True
  if login==False:
    return redirect('home') 
  if request.method=="POST" and 'rating' in request.POST:
    rev,created=models.review.objects.get_or_create(book=book.book,user=request.user)
    rev.rating=int(request.POST['rating'])
    rev.save()
  elif request.method=="POST" and 'req' in request.POST:
    coin_needed=int(book.price*.25)
    if req.req==False and request.user.profile.total_coins>=coin_needed:
      request.user.profile.total_coins=request.user.profile.total_coins-coin_needed
      req.req_date=datetime.now()
      req.req=True
      request.user.profile.save()
      book.owner.profile.notify=True
      book.owner.profile.save()
    elif req.req==False:
      msg='Not Enough coins'
    elif req.req==True:
      req.req=False
      request.user.profile.total_coins=request.user.profile.total_coins+coin_needed
      request.user.profile.save()
  elif request.method=='POST' and 'postid' in request.POST:
    book.is_recieved=True
    book.recieved_date=datetime.now()
    user=book.owner
    user.profile.total_coins+=int(book.price*user.profile.coin_bonus/100)
    user.profile.books_shared+=1
    request.user.profile.books_recieved+=1
    if user.profile.books_shared%3==0:
      user.profile.coin_bonus+=1
    user.profile.save()
    request.user.profile.save()
    
    book.save()
  
  req.save()
  book.save()
  review_set=models.review.objects.filter(book=book.book)
  sum=0
  for rev in review_set:
    sum+=rev.rating
  if len(review_set):
    sum=int(sum/len(review_set))
  context={
    'rating':sum,
    'user':request.user,
    'req':req.req,
    'book':book,
    'login':login,
    'is_my_book':is_my_book,
    'msg':msg,
    'notify':request.user.profile.notify

    
  }
  return render(request,'read_more/index.html',context)

def requested(request,page='1'):

  msg=''
  request.user.profile.notify=False
  request.user.profile.save()
  if request.method=="POST":
    a,b=tuple(request.POST['decline'].split())
    print(a,b)
    models.req_user.objects.filter(book__id=a,user__username=b).delete()
    msg='Request has been declined'
  

  booklist=models.req_user.objects.filter(book__owner=request.user,book__is_pending=True)
  
  req_list=[]
  for req in booklist:
    review_set=models.review.objects.filter(book=req.book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(req.book.price*.25)
    if req.req:
      req_list.append((req.user,req.book,sum,coins))
  req_list.sort(key=lambda x:x[1].post_date,reverse=True)
  p=Paginator(req_list,4)
  booklist=p.get_page(int(page))

  
  

  
  context={
    'req_list':booklist,
    'msg':msg,
    'notify':request.user.profile.notify
  }

  return render(request,'request/index.html',context)


def read_more2(request,pk,username):
  book=models.book_instances.objects.get(id=pk)
  user=User.objects.get(username=username)



  if request.method=="POST":
    if book.is_pending==True:
      book.reciever=user
      models.req_user.objects.filter(book=book).exclude(user=user).delete()

    book.is_pending=not book.is_pending
    book.save()



  context={
    'book':book,
    'user':user,
    'notify':request.user.profile.notify

  }
  return render(request,'read_more2/index.html',context)





def my_posts(request,page):

  msg=''
  if request.method=="POST":
    id=request.POST['postid']
    models.book_instances.objects.filter(id=id).delete()
    msg='The Post has been deleted.'

  req_list=models.book_instances.objects.filter(owner=request.user,is_recieved=False)
  booklist=[]
  for book in req_list:
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(book.price*.25)
    booklist.append(( book ,sum ,coins ))
  
  booklist.sort(key=lambda x:x[0].post_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  
  context={
   'req_list':booklist,
   'user':request.user,
   'msg':msg,
   'notify':request.user.profile.notify
  }
  return render(request,'my_posts/index.html',context)



def books_giveaway(request,page):

  

  req_list=models.book_instances.objects.filter(owner=request.user,is_recieved=True)
  booklist=[]
  for book in req_list:
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(book.price*.25)
    booklist.append(( book ,sum ,coins,book.recieved_date.strftime(" %d %B, %Y") ))
  
  booklist.sort(key=lambda x:x[0].post_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  
  context={
   'req_list':booklist,
   'user':request.user,
   'notify':request.user.profile.notify

  }
  return render(request,'books_giveaway/index.html',context)


def waiting(request,page):

    

  req_list=models.book_instances.objects.filter(reciever=request.user,is_pending=False,is_recieved=False)
  booklist=[]
  for book in req_list:
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(book.price*.25)
    booklist.append(( book ,sum ,coins ))
  
  booklist.sort(key=lambda x:x[0].post_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  
  context={
   'req_list':booklist,
   'user':request.user,
   'notify':request.user.profile.notify

  }
  return render(request,'waiting/index.html',context)

def pending(request,page):

  
  req_list=models.book_instances.objects.filter(owner=request.user,is_pending=False,is_recieved=False)
  booklist=[]
  for book in req_list:
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(book.price*.25)
    req=models.req_user.objects.get(book=book,user=book.reciever)
    booklist.append(( book ,sum ,coins,book.post_date.strftime(" %d %B, %Y"),req.req_date.strftime(" %d %B, %Y")))
  
  booklist.sort(key=lambda x:x[0].post_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  
  context={
   'req_list':booklist,
   'user':request.user,
   'notify':request.user.profile.notify
  }
  return render(request,'pending/index.html',context)


def books_recieved(request,page):

  
  req_list=models.book_instances.objects.filter(reciever=request.user,is_recieved=True)
  booklist=[]
  for book in req_list:
    review_set=models.review.objects.filter(book=book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(book.price*.25)
    booklist.append(( book ,sum ,coins,book.recieved_date.strftime(" %d %B, %Y")))
  
  booklist.sort(key=lambda x:x[0].recieved_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  
  context={
   'req_list':booklist,
   'user':request.user,
   'notify':request.user.profile.notify

  }
  return render(request,'books_recieved/index.html',context)


def my_requests(request,page):

  req_list=models.req_user.objects.filter(req=True,book__is_pending=True,user=request.user)
  booklist=[]
  for req in req_list:
    review_set=models.review.objects.filter(book=req.book.book)
    sum=0
    for rev in review_set:
      sum+=rev.rating
    if len(review_set):
      sum=int(sum/len(review_set))
    coins=int(req.book.price*.25)
    booklist.append(( req.book ,sum ,coins ))
  
  booklist.sort(key=lambda x:x[0].post_date,reverse=True)
  p=Paginator(booklist,4)
  booklist=p.get_page(int(page))
  print(booklist)
  
  context={
   'req_list':booklist,
   'user':request.user,
   'notify':request.user.profile.notify
  }
  return render(request,'my_requests/index.html',context)


  

def price_plan(request):
  msg=''
    
  
  if request.method=="POST":
    coupon=request.POST['coupon']
    if coupon=='give me 100':
      user=request.user
      user.profile.total_coins+=100
      user.profile.save()
      msg="100 coins added to Your Account."
    elif coupon=='give me 500':
      user=request.user
      user.profile.total_coins+=500
      user.profile.save()
      msg="500 coins added to Your Account."
    elif coupon=='give me 200':
      user=request.user
      user.profile.total_coins+=200
      user.profile.save()
      msg="200 coins added to Your Account."
    else:
      msg='No offer available for this coupon'
    

      
  context={
    'message':msg,
   'notify':request.user.profile.notify
    
  }
  return render(request,'price_plan/index.html',context)


  
