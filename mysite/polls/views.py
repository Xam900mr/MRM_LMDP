from django.db.models import F
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import QuestionForm, ChoiceForm

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return render(request, "polls/success.html", {'question_text': question.question_text})
    else:
        form = QuestionForm()
    return render(request, 'polls/question_form.html', {'form': form})

def Choices(request):
    if request.method == "POST":
       form = ChoiceForm(request.POST)
       if form.is_valid():
          question = form.save()
          return render(request, "polls/choices.html", {'question_text': question.choice_text})
    else:
        form = ChoiceForm()
    return render(request, 'polls/question_form.html', {'form': form})