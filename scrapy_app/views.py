from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views import generic

from .models import Series, NewItems


def index(request):
    num_series = Series.objects.all().count()
    num_newitems = NewItems.objects.all().count()
    return render(request, 'index.html',
                  context={'num_series': num_series,
                           'num_newitems': num_newitems}, )


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        series = Series.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {'series': series,
                                                          'query': q})
    else:
        return HttpResponse('What are you doing? Empty form!?')


class SeriesView(generic.ListView):
    model = Series
    paginate_by = 30


class SeriesDetailView(generic.DetailView):
    model = Series
