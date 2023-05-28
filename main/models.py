from code import interact
from configparser import ExtendedInterpolation
from distutils.command.upload import upload
from email.policy import default
from operator import mod
from re import T
from sys import modules
from unicodedata import category
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date


class profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    workplace=models.CharField(max_length=100,null=True,blank=True)
    profession=models.CharField(max_length=50,null=True,blank=True)
    about=models.CharField(max_length=101,null=True,blank=True)
    total_coins=models.IntegerField(default=500)
    books_recieved=models.IntegerField(default=0)
    books_shared=models.IntegerField(default=0)
    coin_bonus=models.IntegerField(default=15)
    birthday=models.CharField(max_length=20,null=True,blank=True)
    facebook=models.CharField(max_length=101,null=True,blank=True)
    insta=models.CharField(max_length=101,null=True,blank=True)
    twitter=models.CharField(max_length=101,null=True,blank=True)
    pinterest=models.CharField(max_length=101,null=True,blank=True)
    notify=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.username

class profile_image(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,blank=True)
    img=models.ImageField(upload_to='documents/',null=True,blank=True)
    def __str__(self) -> str:
        return self.user.username


class book(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    isbn=models.CharField(max_length=50,primary_key=True,unique=True,blank=True)
    author=models.CharField(max_length=50,null=True,blank=True)
    publisher=models.CharField(max_length=50,null=True,blank=True)
    pubdate=models.CharField(max_length=50,null=True,blank=True)
    

    def __str__(self) -> str:
        return self.name

class review(models.Model):
    rating=models.IntegerField(null=True,blank=True)
    book=models.ForeignKey(book,on_delete=models.CASCADE,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    def __str__(self) -> str:
        return self.user.username+' '+self.book.name+' '+str(self.rating)





class book_instances(models.Model):
    bookname=models.CharField(max_length=50,null=True,blank=True)
    book=models.ForeignKey(book,on_delete=models.CASCADE,blank=True)
    author=models.CharField(max_length=50,null=True,blank=True)
    publisher=models.CharField(max_length=50,null=True,blank=True)
    pubdate=models.CharField(max_length=50,null=True,blank=True)
    img=models.ImageField(upload_to='documents/',null=True,blank=True)
    edition=models.CharField(max_length=20,blank=True)
    hard_cover=models.BooleanField(null=True,blank=True)
    paper_back=models.BooleanField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    category=models.CharField(max_length=500,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='requesters_users',blank=True)
    is_pending=models.BooleanField(default=True,blank=True)
    is_recieved=models.BooleanField(default=False,blank=True)
    reciever=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    details=models.CharField(max_length=300,null=True,blank=True)
    post_date=models.DateTimeField(auto_now_add=False,auto_now=False,default=datetime.now,blank=True)
    recieved_date=models.DateTimeField(null=True,blank=True)
 
    def __str__(self) -> str:
        return str(self.id)+' '+self.bookname


class req_user(models.Model):
    req_date=models.DateTimeField(null=True,blank=True)
    req=models.BooleanField(default=False,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    book=models.ForeignKey(book_instances,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.id)+' '+str(self.req_date)+' '+self.user.username+' '+self.book.bookname



class interest(models.Model):
    interest_value=models.IntegerField(null=True,default=0,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    book_instance=models.ForeignKey(book_instances,on_delete=models.CASCADE,blank=True)
   

    def __str__(self) -> str:
        return str(self.id)+' '+self.book_instance.bookname+' '+str(self.interest_value)






    