
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.models import Poll


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
