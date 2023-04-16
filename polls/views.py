from django.http import Http404
from django.shortcuts import render
from .models import Question


# from django.template import loader


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
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    pass


def vote(request, question_id):
    pass
