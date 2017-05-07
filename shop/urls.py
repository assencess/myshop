from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    # url(r'^$', views.product_list, name='product_list'),
    url(r'^$', views.ProductListView.as_view(), name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.product_list,
    #     name='product_list_by_category'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.ProductListView.as_view(),
        name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,
    #     name='product_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.ProductDetailView.as_view(),
        name='product_detail'),
]
