from django.views.generic import ListView

from .models import Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10
