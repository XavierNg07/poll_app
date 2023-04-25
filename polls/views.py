from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
# from django.template import loader


# Create your views here.


# def index(request):
# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# # template = loader.get_template('polls/index.html')
# context = {
#     'latest_question_list': latest_question_list,
# }
# # return HttpResponse(template.render(context, request))
#
# # It is a common idiom to load a template, fill a context
# # and return an HttpResponse object with the result of the rendered template
# # Django provides a shortcut
# return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#
#     # It is a common idiom to use get() and raise Http404 if the object doesn't exist
#     # Django provides a shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# These views represent a common case of basic web development:
# getting data from the database according to a parameter passed in the URL,
# loading a template and returning the rendered template.
# => Django provides a shortcut, called the "generic views" system

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 'polls/detail.html',
            {
                'question': question,
                'error_message': 'You did not select a choice.'
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
