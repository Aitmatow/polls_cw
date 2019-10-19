
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.models import Poll, Answer, Choice


class PollList(ListView):
    template_name = 'poll/polls_list.html'
    model = Poll
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'
    ordering = ['-created_at']

class PollDetail(DetailView):
    template_name = 'poll/polls_detail.html'
    model = Poll
    context_key = 'object'

class PollCreate(CreateView):
    template_name = 'poll/polls_form.html'
    model = Poll
    fields = ['question']
    success_url = reverse_lazy('poll_list')

class PollUpdate(UpdateView):
    template_name = 'poll/polls_form.html'
    model = Poll
    fields = ['question']
    success_url = reverse_lazy('poll_list')

class PollDelete(DeleteView):
    template_name = 'poll/polls_delete.html'
    model = Poll
    success_url = reverse_lazy('poll_list')

class AnswerShow(View):
    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        choices = Choice.objects.filter(poll=poll)

        return render(request, 'poll/polls_answers.html', {'poll' : poll, 'choices':choices })

    def post(self,request,pk):
        poll = Poll.objects.get(pk=pk)
        choice = Choice.objects.get(pk=request.POST.get('selected_choice'))
        Answer.objects.create(
            poll=poll,
            choice=choice
        ).save()
        return redirect('poll_view', pk=pk)

class AnswerStatistic(View):
    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        choices = Choice.objects.filter(poll=poll)
        count = []
        cur_count = Answer.objects.filter(poll=poll).count()
        for i in Choice.objects.filter(poll=poll):
            count.append(str(i) + "-" + str(Answer.objects.filter(poll=poll, choice=i).count()) + " (" + '{0:.2f}'.format(Answer.objects.filter(poll=poll, choice=i).count() / cur_count * 100)  + "%)" )
        return render(request, 'poll/polls_statistic.html', {'poll' : poll, 'choices':choices, 'all' : count })



