from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})

def about(request):
    return render(request, 'articles/about.html')

def homepage(request):
    return render(request, 'articles/homepage.html')

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})