from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger    # Для общего представления
from django.views.generic import ListView                                   # Для представления на основе класса
from .models import Post


class PostListView(ListView):
    # Представление на основе классов
    # queryset = Post.publish.all()     # Так на сайте предлагается фильтровать опубликованные посты
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
    # Предсталение (views) общее
#     # posts = Post.objects.all()
#     # posts = Post.objects.filter(status='published')
#     object_list = Post.objects.filter(status='published')
#     paginator = Paginator(object_list, 3)               # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts
#                    })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             # status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post,
                             )
    return render(request, 'blog/post/detail.html', {'post': post})
