from .models import Post
from django.views.generic import ListView


class Desk(ListView):
    model = Post
    template_name = 'desk.html'
