#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Poll
from .models import HowTo, Step


class IndexView(generic.ListView):
    template_name = 'doc_types/index.html'
    context_object_name = 'howto_list'

    def get_queryset(self):
        return HowTo.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = HowTo
    template_name = 'doc_types/detail.html'
    context_object_name = 'current_how_to'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'doc_types/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'doc_types/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('doc_types:results', args=(p.id,)))
