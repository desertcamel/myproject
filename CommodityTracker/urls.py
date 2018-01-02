from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='commodity-index'),
]

# List Urls
urlpatterns += [
    # List
    url(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    url(r'^commodities/$', views.CommodityListView.as_view(), name='commodities'),
    url(r'^apisources/$', views.APISourceListView.as_view(), name='apisources'),
    url(r'^timeseries/$', views.TimeSeriesListView.as_view(), name='timeseries'),
]



# List Urls
urlpatterns += [
    # Detail
    url(r'category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'commodity/(?P<pk>\d+)$', views.CommodityDetailView, name='commodity-detail'),
]

# List Urls
urlpatterns += [
    # Create
    url(r'category/add/$', views.CategoryCreateView.as_view(), name='category-create'),
    
]

urlpatterns += [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^signup/ajax/validate_username/$', views.validate_username, name='validate-username'),
]


