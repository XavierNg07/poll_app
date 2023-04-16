from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))

    # Since it is common idiom to load a template, fill a context
    # and return an HttpResponse object with the result of the rendered template
    # Django provides a shortcut
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
