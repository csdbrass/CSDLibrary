from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pieces/', views.PieceListView.as_view(), name='pieces'),
    path('piece/<int:pk>', views.PieceDetailView.as_view(), name='piece-detail'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('persons/', views.PersonListView.as_view(), name='person'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('composers/', views.ComposerListView.as_view(), name='composer'),
    path('composer/<int:pk>', views.ComposerDetailView.as_view(), name='composer-detail'),
]

# Add URLConf to create, update, and delete persons
urlpatterns += [
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]

# Add URLConf to create, update, and delete pieces
urlpatterns += [
    path('piece/create/', views.PieceCreate.as_view(), name='piece_create'),
#    path('piece/<int:pk>/update/', views.PieceUpdate.as_view(), name='piece_update'),
    path('piece/<int:pk>/delete/', views.PieceDelete.as_view(), name='piece_delete'),
    path('pieceUpdate',views.PieceUpdateView,name='pieceUpdate'),
    url(r'^search/$', views.search, name='search'),
    url(r'^searchPerson/$', views.searchPerson, name='searchPerson'),
    url(r'^searchList/$', views.searchList, name='searchList'),
    url(r'^check/$', views.PieceSearch, name='piece_search'),
	url(r'^updateList/$', views.PieceEdit, name='pieceEdit'),
#	url(r'^updateList/<int:pk>$', views.PieceUpdateList, name='pieceUpdateList'),
	path('piece/<int:pk>/update/', views.PieceEdit, name='pieceEdit'),
	path('piece/<int:pk>/updateList', views.PieceEditList, name='pieceEditList'),
#    path('search', views.search, name='search'),
    path('pieces/listComposers',views.listComposers,name='listComposers'),
	
	path('FindPiece',views.findPiece,name='findPiece'),
	path('AddPerson',views.addPerson,name='addPerson'),
	path('AddPiece',views.addPiece,name='addPiece'),
#	path('PersonUpdate',views.PersonUpdate,name='personUpdate'),
#    path('userLogin',auth_views.LoginView.as_view(template_name='catalogue/userLogin.html'),name='userLogin'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userLogout',views.userLogout,name='userLogout'),
]

