from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render


from .models import Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"

def singlepostview(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    return render(request, "blog/single.html", {"post": post})
