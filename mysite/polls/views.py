from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse
# Create your views here.


# 首页视图,展示最近发布的5个问题
def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {
        'last_question_list' : last_question_list
    }
    return render(request, 'polls/index.html', context)

# 展示问题详情
def detail(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

# 展示问题结果
def results(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})


# 展示投票结果
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set().get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExit):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "choice does not exit"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id)))

