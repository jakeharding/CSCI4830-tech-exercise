from django.conf.urls import url
from tech_exercise.index.views import BlogEntryListView, CreateBlogEntryView

urlpatterns = [
    url(r'^$', BlogEntryListView.as_view(), name="blog-entry-list"),
    url(r'^create/$', CreateBlogEntryView.as_view(), name="blog-entry-create"),
    url(r'^detail/(?P<pk>\d+)/$', CreateBlogEntryView.as_view(), name="blog-entry-detail"),
]
