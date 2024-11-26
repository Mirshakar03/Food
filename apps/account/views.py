from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, template_name='article/index.html')

class MenuView(View):
    def get(self, request):
        return render(request, template_name='article/menu.html')

class AboutView(View):
    def get(self, request):
        return render(request, template_name='article/about.html')

class BookView(View):
    def get(self, request):
        return render(request, template_name='article/book.html')
