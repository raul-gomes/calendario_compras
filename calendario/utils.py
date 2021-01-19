import datetime
from calendar import HTMLCalendar
from calendario.models import Compras


class Calendario(HTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        self.soma = 0
        super(Calendario, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(data_compra__day=day)
        d = ''
        if day > 0:
            data = datetime.date(self.year, self.month, day)

        for event in events_per_day:
            if data in event.data_parcelas():
                d += '<li> {} - R$ {:.2f} </li>'.format(event.nome_compra, event.valor_parcela)
                Calendario.somar(self, event.valor_parcela)
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
        events = Compras.objects.all()
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

    # soma o valor de débitos do mês
    def somar(self, parcela):
        self.soma += parcela

    @property
    def get_valor_soma(self):
        return self.soma
