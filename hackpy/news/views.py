from django.shortcuts import render

# Create your views here.
# news/views.py

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News, Comment, Vote
from django.shortcuts import get_object_or_404, redirect
from .models import News, Comment, Vote
from .forms import NewsForm, CommentForm

class NewsListView(ListView):
    model = News
    paginate_by = 30
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

def vote_news(request, pk, vote_type):
    news = get_object_or_404(News, pk=pk)
    vote, created = Vote.objects.get_or_create(user=request.user, news=news)
    vote.vote_type = vote_type
    vote.save()
    return redirect('news_list')
