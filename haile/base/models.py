from django.db import models
from django.contrib.auth.models import User

class StudentActivity(models.Model):
    programming_language = models.CharField(max_length=20)
    frontend = models.CharField(max_length=20)
    backend = models.CharField(max_length=20)
    def __str__(self):
        return self.programming_language

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    section = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    # detail = models.ForeignKey(StudentActivity,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null= True,blank=True)
    message = models.ManyToManyField('Message',blank=True,null = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Message(models.Model):

    body = models.CharField(max_length=30,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body
