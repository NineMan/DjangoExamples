from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger    # Для общего представления
from django.views.generic import ListView                                   # Для представления на основе класса
from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from taggit.models import Tag
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


class PostListView(ListView):
    # Представление на основе классов
    # queryset = Post.publish.all()     # Так на сайте предлагается фильтровать опубликованные посты
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    # Представление (views) общее
    # posts = Post.objects.all()
    # posts = Post.objects.filter(status='published')
    object_list = Post.objects.filter(status='published')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)               # 3 поста на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не целое число, то поставим первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница выскакивает за диапазон - показываем последнюю страницу
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag,
                   })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             # status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post,
                             )
    # Список активных комментов для этого поста
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # Комментарий запостили
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создается объект Comment, но ещё не сохраняется в базу
            new_comment = comment_form.save(commit=False)
            # Назначаем текущий пост для коммента
            new_comment.post = post
            # Сохраняем коммент в базу данных
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = Post.objects.filter(status='published')
    similar_posts = similar_posts.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'coment_form': comment_form,
                   'similar_posts': similar_posts,
                    }
                  )


def post_share(request, post_id):
    # Извлечение поста по id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form была отправлена (заполнена и отправлена "submit")
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # если поля Form прошли проверку (valid), то используем "чистые" данные (cleaned_data)
            cd = form.cleaned_data
            # send mail
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommended you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            # send_mail(subject, message, admin@myblog.com, cd['to'])
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [cd['to']],
                      fail_silently=False)
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
