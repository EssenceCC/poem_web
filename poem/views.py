from django.shortcuts import render,redirect
from poem import models
#要用到Poem这个类来操作数据库，所以导入
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    if 'username' in request.session:
        username = request.session['username']


    #获取所有诗词
    all_poems = models.Poem.objects.all().order_by('id')  #对象列表

    return render(request, 'index.html', locals())


#登录
def login(request):
    if request.method == 'POST':
        login_name = request.POST['username']
        login_password = request.POST['password']
        try:
            user = models.Usr.objects.get(username=login_name)
            if user.password == login_password:
                request.session['username'] = user.username
                request.session['password'] = user.password
                return redirect('/')
            else:
                message = "密码错误，请再检查一次"

        except:
            message = '找不到用户'
    return render(request,'login.html',locals())

#注销
def logout(request):
    if 'username' in request.session:
        #删除所有用户的cookie包括后台管理员
        # Session.objects.all().delete()
        request.session['username'] = None #只删除当前用户的cookie
    return redirect('/')

#新增诗词
def poem_add(request):
    # post请求获取用户提交的数据
    if request.method == 'POST':
        poem_title = request.POST.get('poem_title')
        # print(poem_title)
        if not poem_title:
            #输入为空
            return render(request,'poem_add.html',{'error':'诗词标题不可为空'})
        elif models.Poem.objects.filter(title = poem_title):
            #表示数据库中有重复的名字
            return render(request,'poem_add.html',{'error':'该诗词已存在'})

        # 将数据新增到数据库中
        ret = models.Poem.objects.create(title=poem_title)
        print(ret, type(ret))

        # 返回一个重定向到展示出版社的页面
        return redirect('/')
    # get请求返回一个页面，页面中包含form表单
    return render(request,'poem_add.html')

#删除诗词
def poem_del(request):
    #获取要删除诗词的Id
    pk = request.GET.get('pk')
    # print(pk)
    #根据ID到数据库进行删除
    # models.Poem.objects.get(pk = pk).delete() #查询到一个对象，删除该对象
    models.Poem.objects.filter(pk = pk).delete() #查询到一个对象列表，删除该列表中所有对象
    #返回重定向到展示出版社的页面
    return redirect('/')


#修改诗词
def poem_edit(request):
    pk = request.GET.get('pk')
    poem_obj = models.Poem.objects.get(pk = pk)
    all_dynasty = models.Dynasty.objects.all()


    if request.method == 'GET':
    #返回一个页面 页面包含form表单   input原始数据
        return render(request,'poem_edit.html',{'poem_obj':poem_obj},{'all_dynasty':all_dynasty})
    else:
        #post
        #修改数据库中相应的数据
        poem_title = request.POST.get('poem_title')
        poem_obj.title = poem_title   #在内存中修改
        poem_obj.save()   #将修改操作提交到数据库
        #返回重定向到展示诗词页面
        return redirect('/')

def poem_show(request):
    pk = request.GET.get('pk')
    poem_obj = models.Poem.objects.get(pk=pk)

    if request.method == 'GET':
    #返回一个页面 页面包含form表单   input原始数据
        return render(request,'poem_show.html',{'poem_obj':poem_obj})

def index1(request):
    return render(request,'index.html')


def test(request):
    return render(request,'poem_edit.html')