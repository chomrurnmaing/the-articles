from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, render_to_response

from pages.forms.news_form import NewsForm
from pages.models import Post


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


# @login_required
class DashboardPageView(TemplateView):

    @login_required
    def dashboard(self):
        return render(self, 'admin/dashboard.html')


# @login_required
class NewsPageView(TemplateView):

    @login_required
    def index(request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }

        return render_to_response('admin/news/index.html', context)

    @login_required
    def create(request):
        return render(request, 'admin/news/create.html')

    @login_required
    def store(request):
        form = NewsForm(request.POST)

        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()

            return redirect('/news')
        else:
            return redirect('/news/create')

    @login_required
    def edit(request, id):

        post = Post.objects.get(id=id)

        return render(request, 'admin/news/edit.html', {'post': post})

    @login_required
    def update(request, id):
        post = Post.objects.get(id=id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return redirect('/news')
