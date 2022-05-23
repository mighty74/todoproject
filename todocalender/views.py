from django.shortcuts import render
from django.views import generic
from todo.models import TodoModel
import datetime
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.
class CalendarList(generic.ListView):
    template_name = 'calender.html'
    model = TodoModel
    context_objects_name = 'calendar'
    def get(self, request, *args, **kwargs):
        dates = datetime.datetime.today()
        year = dates.year
        month = dates.month
        day = dates.day
        days = [dates + datetime.timedelta(days=i) for i in range(30)]
        calendar = TodoModel.objects.all()
        paginator = Paginator(days, 10) # 1ページに10件表示
        p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
        articles = paginator.get_page(p) # 指定のページのArticleを取得
        return render(request, 'calender.html', {
                'year': year,
                'month': month,
                'day': day,
                'days': days,
                'calendar': calendar,
                'articles': articles
            })
    


class TodoCreate(generic.CreateView):
    template_name = 'create2.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('list')

class TodoDetail(generic.DetailView):
    template_name = 'detail2.html'
    model = TodoModel

class TodoUpdate(generic.UpdateView):
    template_name = 'update2.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('list')

class TodoDelete(generic.DeleteView):
    template_name = 'delete2.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoList(generic.ListView):
    template_name = 'todolist.html'
    model = TodoModel
    