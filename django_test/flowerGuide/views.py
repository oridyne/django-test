import os

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Flower


class IndexView(generic.TemplateView):
    template_name = 'flowerGuide/index.html'


def detailView(request, slug):
    flower = get_object_or_404(Flower, slug=slug)
    path = settings.STATIC_ROOT
    img_list = []
    try:
        img_list = os.listdir(path + '\\images\\' + flower.slug)
    except FileNotFoundError:
        return render(request, 'flowerGuide/detail.html', {'flower': flower, 'images': img_list})
    else:
        for i, s in enumerate(img_list):
            img_list[i] = 'flowerGuide/images/' + flower.slug + '/' + s
        return render(request, 'flowerGuide/detail.html', {'flower': flower, 'images': img_list})


class ListView(generic.ListView):
    template_name = 'flowerGuide/list.html'
    context_object_name = 'flower_list'

    def get_queryset(self):
        return Flower.objects.order_by('id').all()
