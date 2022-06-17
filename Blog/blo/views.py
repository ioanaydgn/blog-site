from django.db.models import Q
from django.views.generic import ListView, DetailView
from blo.models import Post

def get_qs():
    return Post.objects.filter(draft=False)

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return get_qs()

class SearchView(IndexView):

    def get_queryset(self):
        q = self.request.GET.get("q")
        return get_qs().filter(
                    Q(title__icontains=q) |
                    Q(keywords__icontains=q) |
                    Q(content__icontains=q)
               )
    

class PostView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
    slug_field = "slug"
