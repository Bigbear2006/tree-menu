from django.views.generic import DetailView, ListView

from .models import Menu


class MenuListView(ListView):
    queryset = Menu.objects.filter(parent=None)
    context_object_name = 'menu_set'
    template_name = 'index.html'


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'
