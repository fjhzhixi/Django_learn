# Django学习demo

## demo

### 初始化项目文件夹

```
django-admin startproject mysite
```

### 创建项目的一个应用

```
python manage.py startapp polls
```

### 项目启动运行

```
python manage.py runserve
```

### urls.py模块

定义`url`与响应的函数之间的对应关系

```python

from django.contrib import admin
from django.urls import include, path
# 定义映射关系
#---------------------------#
# 在项目的总体即mysite下的urls.py中
urlpatterns = [
    # 所有的应用的url映射关系通过include采用相对路径导入
    # 具体应用内部的url映射关系由自己定义(polls/urls.py)
    # 例如下面即为polls应用的导入
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),# 项目自动生成的
]

#--------------------------#
# 在一个应用中定义映射关系
from django.urls import path
from . import views	# 导入view.py
urlpatterns = [
    # 即定义首页为view.py中定义的index函数响应
    path('', views.index, name='index'),
]

#--------------------------#
# 即上面完成http://127.0.0.1:8000/polls/ ----> index()函数的映射
```

**path函数**

```python
path(route, view, kwargs=None, name=None)
# route 匹配Http请求的URl中的部分(不包括GET/POST参数以及域名)
# view 为视图模块中的一个函数
```

### 链接mysql数据库

```python
# mysite/setting.py中进行配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# 为默认应用创建表检查配置是否成功
python manage.py migrate
```

### 创建模型

**`models.py`中的每一个`class`与数据库中的一个`table`对应** :

1. 类的属性对应着数据库的字段

### 将应用添加到项目中

分3步进行

```python
# 修改mysite/setting.py中的INSTALLED_APPS,添加
'polls(应用文件夹名).apps.PollsConfig'
# 为模型的改变生成迁移文件
python manage.py makemigrations polls(项目名字)
# 为应用建立数据库
python manage.py migrate
```

### 视图(view.py)

```python
# poll/view.py
# 每一个函数对应处理一种request请求
# request为必需的参数,其他参数可选,从请求的URL字段获得
# 返回值多为HttpResponse类型
def funct(request, *args):
    return HttpResponse()

# 使用render函数可以简化
context = {
    "key" : values
}
render(request, "path/to/UI.html(模板文件)", context)
```

#### 通用视图概念

自己定义的视图可以继承自通用视图模板

```python
# ListView视图显示一个对象列表
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# DetailView视图显示一个对象的具体信息
# model 属性决定其作用于哪个模型
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```

### 测试

1. 简单测试
   1. 在应用目录下的`test.py`文件中进行
   2. 每一个测试的`case`继承自`django.test.TestCase`
   3. 测试函数以`test`开头
   4. 运行的测试 : `python manage.py test polls`(应用名)
2. 针对于视图的测试
   1. `Client`工具

### 静态文件

样式和图片

1. 存在形式 : 在每个应用根目录下的`static`文件夹中

   `polls/static/polls/style.css`

2. 使用

   ```html
   {% load static %} 
   <!-- 上面的语句加载静态文件存放的文件夹根目录,即polls/static-->
   <link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
   <!-- static 'polls/style.css' 即代表了决定路径 polls/static/polls/style.css-->
   ```

## 模块

### 模块配合

1. 根据`htttp`请求在`urls.py`中寻找匹配的`view.py`中的处理函数,传递给必要的参数 : 
   1. 如果为`GET`请求多从`url`匹配捕捉而来
   2. 如果为`POST`请求则通过`request`对象的属性来获得
2. 在`view`中的处理请求函数中利用传入的参数**从`Models.py`中的模型获得数据**,之后传递给对应的模板`html`文件
3. 模板文件根据传入的参数填写数据并返回给请求端

### 模型(models.py)

1. 一个模型类代表一张数据表，一个模型类的实例代表数据库表中的一行记录。

2. `Django`会自动生成一系列对数据库的操作

   1. 创建对象 : 用关键字参数初始化它，然后调用`save()`将其存入数据库。

   2. 检索对象

      ```python
      # 检索单个对象
      Entry.objects.get(pk=1)	#pk即为主键primary key
      # 检索对象集合
      Entry.objects.all() # 检索所有对象
      Entry.objects.filter(**kwargs) # 检索满足的
      Entry.objects.exclude(**kwargs) # 检索不满足的
      # 所有的返回值都是一个全新的QuerySet
      # 上述方法可以链式组合
      # 字段查询语句生成
      field__lookuptype=value。（有个双下划线）
      # 注意理论上所有的SQL SELECT语句都可以转换为上面三个函数的参数形式
      
      ```

      

3. 你可以自己在对象中自定义方法

### 视图(view.py)

最主要的逻辑处理模块

## pycharm调试设置

https://www.cnblogs.com/Rocky_/p/6187275.html

https://www.cnblogs.com/atuotuo/p/8724515.html

