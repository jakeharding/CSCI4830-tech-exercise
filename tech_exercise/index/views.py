"""
views.py - (C) Copyright - 2017

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Views for the BlogEntry pages
"""

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.forms import ModelForm
from django.views.generic.base import ContextMixin
from django.db.models import Q

from tech_exercise.index.models import BlogEntry


class BlogEntryForm(ModelForm):
    readonly = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control mb-4'
            f.field.widget.attrs['placeholder'] = f.label
            if self.readonly:
                # f.field.widget.attrs['readonly'] = True
                f.field.widget.attrs['placeholder'] = ''
                f.field.widget.attrs['class'] += ' form-control-plaintext'
            else:
                f.label = ''

    class Meta:
        model = BlogEntry
        exclude = ['created_at']


class ReadOnlyBlogEntryForm(BlogEntryForm):
    readonly = True


class BlogContextMixin(ContextMixin):
    page_heading = ""

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt.update({
            "page_heading": self.get_page_heading(),
        })
        return cxt

    def get_page_heading(self):
        return self.page_heading


class BlogEntryListView(ListView, BlogContextMixin):
    model = BlogEntry
    page_heading = "Blog Entry List"
    template_name = "index/blogentry_search.html"

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt.update({
            "search": self.request.GET.get('search'),
        })
        return cxt

    def get_queryset(self):
        qs = super().get_queryset()
        qp = self.request.GET.get('search')
        if qp:
            qs = qs.filter(Q(author__icontains=qp) | Q(title__icontains=qp) | Q(article__icontains=qp) | Q(email__icontains=qp))
        return qs


class CreateBlogEntryView(CreateView, BlogEntryListView):
    page_heading = "Create Blog Entry"
    form_class = BlogEntryForm
    success_url = "/"
    template_name = "index/blogentry_form.html"


class BlogEntryDetailView(UpdateView, BlogContextMixin):
    page_heading = ""
    model = BlogEntry
    template_name = 'index/blogentry_detail.html'
    form_class = ReadOnlyBlogEntryForm

    def get_page_heading(self):
        return self.object.title
