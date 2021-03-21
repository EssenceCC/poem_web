from django.db import models

# Create your models here.

class Dynasty(models.Model):
    dynasty = models.CharField(max_length=10)

    def __str__(self):
        return self.dynasty


class Author(models.Model):
    author = models.CharField(max_length=10)
    author_info = models.TextField(default='', blank=True)
    dynasty = models.ForeignKey(to='Dynasty',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.author




class Theme(models.Model):
    theme = models.CharField(max_length=10)

    def __str__(self):
        return self.theme


class Poem(models.Model):

    title = models.CharField(max_length=60)
    author = models.ForeignKey(to='Author',on_delete=models.CASCADE)
    body = models.TextField()
    dynasty = models.ForeignKey(to='Dynasty',on_delete=models.CASCADE)
    annotation = models.TextField(default='',blank = True)
    translation = models.TextField(default='' , blank= True)
    background = models.TextField(default='',blank=True)
    remark = models.TextField(default='',blank=True)
    theme = models.ManyToManyField('Theme',blank=True)

    def __str__(self):
        return self.title

class Usr(models.Model):
    username = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=12)

    email = models.EmailField(unique=True,blank=True)
    icon = models.ImageField()

    def __str__(self):
        return self.username





