from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from . import models
# Create your views here.

class BlogIndex(generic.ListView):
	queryset = models.Entry.objects.published()
	template_name = "home.html"
	paginate_by = 2

class BlogDetail(generic.DetailView):
	model = models.Entry
	template_name = "post.html"