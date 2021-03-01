from django.urls import include, path
from .views import IndustryCreate, IndustryList, IndustryDetail, IndustryUpdate, IndustryDelete, AdvertiserCreate, AdvertiserList, AdvertiserDetail


urlpatterns = [
	path('create/', IndustryCreate.as_view(), name='create-Industry'),
    path('', IndustryList.as_view()),
    path('<int:pk>/', IndustryDetail.as_view(), name='retrieve-Industry'),
    path('update/<int:pk>/', IndustryUpdate.as_view(), name='update-Industry'),
    path('delete/<int:pk>/', IndustryDelete.as_view(), name='delete-Industry'),
    path('Advertisercreate/', AdvertiserCreate.as_view(), name='create-Advertiser'),
    path('Advertiserlist', AdvertiserList.as_view()),
    path('Advertiser/<int:pk>/', AdvertiserDetail.as_view(), name='retrieve-Advertiser'),
    #path('Advertiser/update/<int:pk>/', IndustryUpdate.as_view(), name='update-Industry'),
    #path('Advertiserdelete/<int:pk>/', IndustryDelete.as_view(), name='delete-Industry')
]