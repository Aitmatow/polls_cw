
# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from webapp.models import Choice, Poll


class ChoicesList(ListView):
    template_name = 'choices/choices_list.html'
    model = Choice

class ChoicesDetail(DetailView):
    template_name = 'choices/choices_detail.html'
    model = Choice
    context_key = 'object'

class ChoicesCreate(CreateView):
    template_name = 'choices/choices_form.html'
    model = Choice
    fields = ['text']
    success_url = reverse_lazy('choices_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = Choice.objects.create(
                text=form.cleaned_data['text'],
                poll=Poll.objects.get(pk=kwargs.get('pk'))
            )
            obj.save()
            return redirect('poll_view',pk=kwargs.get('pk'))
        else:
            return self.form_invalid(form)

class ChoicesUpdate(UpdateView):
    template_name = 'choices/choices_form.html'
    model = Choice
    fields = ['text']
    success_url = reverse_lazy('poll_list')


class ChoicesDelete(DeleteView):
    template_name = 'choices/choices_delete.html'
    model = Choice
    success_url = reverse_lazy('poll_list')
