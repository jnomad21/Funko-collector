from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('funko/', views.FunkoList.as_view(), name='funko_index'),
    path('funko/create/',views.FunkoCreate.as_view(), name='funko_create'),
    path('funko/<int:pk>/', views.FunkoDetail.as_view(), name='funko_detail'),
    path('funko/<int:pk>/update', views.FunkoUpdate.as_view(), name= 'funko_update'),
    path('funko/<int:pk>/delete', views.FunkoDelete.as_view(), name= 'funko_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('funko/<int:funko_id>/add_to_collection/<int:profile_id>/', views.add_to_collection, name='add_to_collection'),
    path('funko/<int:funko_id>/add_to_wishlist/<int:profile_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('profile/', views.profile, name="profile"),
    path('profile/collection', views.CollectionList.as_view(), name="collection"),
    path('profile/wishlist', views.WishList.as_view(), name="wishlist")
    # path('funko/<int:pk>/add_review/', views.add_review, name='add_review')
]