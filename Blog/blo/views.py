from django.views.generic import ListView, DeleteView
from blo.models import Post

def get_qs():
    return Post.objects.filter(draft=False)

class IndexView(ListView):
    template_name = "index.html"
    context_object_name: "Posts"

    def get_queryset(self):
        return get_qs()

class PostView(DeleteView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
    slug_field = "slug"
