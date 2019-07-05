from django.urls import path

from .views import HomePageView, AboutPageView, DashboardPageView, NewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.dashboard, name='dashboard'),
    path('news/', NewsPageView.index, name='news'),
    path('news/create', NewsPageView.create, name='news-create'),
    path('news/store', NewsPageView.store, name='news-store'),
    path('news/<int:id>/edit', NewsPageView.edit, name='news-edit'),
    path('news/<int:id>/update', NewsPageView.update, name='news-update'),
]
