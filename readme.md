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



## 模块

