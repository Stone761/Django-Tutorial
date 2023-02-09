from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function
## for q in, means every object in latest_question_list is represented as a smaller variable "q" 
# output = ', '.join([q.question_text for q in latest_question_list]) ## Basically this means every question will be joined together with seperation as a comma and a space in this case