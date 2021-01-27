from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime, date, timedelta
from django.utils.safestring import mark_safe
from django.views import generic
from calendario.forms import ComprasForm
from api.models import Compras
from calendario.utils import Calendario
import calendar


class index(generic.View):
    template_name = 'base.html'


def detail(request, pk):
    qs = list(Compras.objects.filter(pk=pk))
    data = serializers.serialize('json', qs)
    return render(request, '/calendario/', {'data': data}, content_type='application/json')


class CalendarioView(generic.ListView):
    model = Compras
    template_name = 'calendario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendario(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendario'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['soma'] = '{:.2f}'.format(cal.get_valor_soma)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def compras(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            Compras.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/calendario/')

    else:
        form = ComprasForm()

    return render(request, 'compras.html', {'form': form})
