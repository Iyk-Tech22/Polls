from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_pub = Question.objects.order_by("-pub_date")[:5]
    #response = ",".join([q.question_text for q in late_question_pub])
    template = loader.get_template("polls/index.html")
    context = {
        "latest_questions":latest_question_pub
    }
    return HttpResponse(template.render(context, request))
    
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
           "question":question
        }
    except Question.DoesNotExit:
        raise Http404("Question does not exit.")
    return render(request, "polls/detail.html", context)
    
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
       "question":question
    }
    return render(request, "polls/results.html", context)
    
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST["choice"]
        choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        context = {
           "question":question,
           "error_message": "You didn't select a choice."
        }
        return render(request, "polls/detail.html", context)
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))









