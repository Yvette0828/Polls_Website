from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView

from polls.serizlizers import QuestionSerializer

from .forms import VoteForm
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:20]

class QuestionView(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # @swagger_auto_schema(
    #  operation_summary='GET',
    #  operation_description='get question',
    #  manual_parameters=[
    #     openapi.Parameter(name='question_text', 
    #     in_ = openapi.IN_BODY,
    #     description='Question Text',
    #     type=openapi.TYPE_STRING,
    #     )
    #  ]
    #  )
    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # queryset = Question.objects.all()
    # serializer_class = QuestionSerializer
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            name = request.POST['voter']
            selected_choice = question.choice_set.get(pk=request.POST['choice'])

            selected_choice.votes += 1
            selected_choice.save()

            user, _ = User.objects.get_or_create(username=name)  # 尋找或創建使用者記錄
            selected_choice.voters.add(user)  # 新增投票者至 voters 列表

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        form = VoteForm()

    return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         form = VoteForm(request.POST)
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
def popup_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'popup.html', {'question': question})
