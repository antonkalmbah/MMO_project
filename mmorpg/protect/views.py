from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/default.html'

# protect/index.html переводит на страничку где "Страница авторизованного пользователя" папки protect
# flatpages/default.html переводит на страничку доски объявлений из папки flatpages
