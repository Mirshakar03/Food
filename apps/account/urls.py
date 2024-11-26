from django.urls import path
from apps.account.views import HomeView, MenuView, BookView, AboutView

app_name = 'account'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu.html', MenuView.as_view(), name='menu'),
    path('book.html', BookView.as_view(), name='book'),
    path('about.html', AboutView.as_view(), name='about'),
    path('index.html', HomeView.as_view(), name='index'),

]