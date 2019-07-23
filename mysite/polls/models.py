from django.db import models

# Create your models here.

# 定义问题模型
# 类的属性即对应数据块的键值
class Question(models.Model):
    # 最大为200字符的文字描述
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    def __str__(self):
        return self.question_text

# 定义选择模型
class Choice(models.Model):
    # 使用ForeignKey的性质定义 : 每个choice对应唯一的question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 默认值为0的选择数目
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text