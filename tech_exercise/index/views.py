"""
views.py - (C) Copyright - 2017

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Views for the BlogEntry pages
"""

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import ContextMixin
from tech_exercise.index.models import BlogEntry


class BlogContextMixin(ContextMixin):
    page_heading = ""

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt.update({
            "page_heading": self.page_heading
        })
        return cxt


class BlogEntryListView(ListView , BlogContextMixin):
    model = BlogEntry
    page_heading = "Blog Entry List"


class CreateBlogEntryView(CreateView, BlogContextMixin):
    model = BlogEntry
    fields = ['title', 'author', 'email', 'article']
    page_heading = "Create Blog Entry"

