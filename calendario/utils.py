import datetime
from calendar import HTMLCalendar

from django.shortcuts import get_object_or_404

from calendario.models import Compras


class Calendario(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendario, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(data_compra__day=day)
        d = ''
        for event in events_per_day:
            d += '<li> {} - R$ {:.2f} </li>'.format(event.nome_compra, event.valor_compra)
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Compras.objects.filter(data_compra__year=self.year, data_compra__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

    # soma o valor de débitos do mês


def soma(self, withyear=True):
    events = Compras.objects.filter(data_compra__year=self.year, data_compra__month=self.month)
    soma = 0
    for event in events:
        soma += event.valor_compra
    return 'R$ {:.2f}'.format(soma)
