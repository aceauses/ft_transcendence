from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'users'
urlpatterns = [
	path('', views.list, name='list'),
	path('register/', views.register, name='register'),
	path('account/', views.account, name='account'),
	path(
		'login/',
		auth_views.LoginView.as_view(template_name='users/login.html'),
		name='login',
	),
	path('logout/', views.custom_logout, name='logout'),
	# friendship management: both `user` and `users` prefix
	re_path(r'^user(s)?/(?P<query_user>[^/]+)$', views.public_profile, name='public-profile'),
	re_path(
		r'^user(s)?/(?P<target_username>[^/]+)/friend-request$',
		views.friend_request,
		name='friend-request',
	),
	re_path(
		r'^user(s)?/(?P<target_username>[^/]+)/cancel-friend-request$',
		views.cancel_friend_request,
		name='cancel-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<origin_username>[^/]+)/deny-friend-request$',
		views.deny_friend_request,
		name='deny-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<origin_username>[^/]+)/accept-friend-request$',
		views.accept_friend_request,
		name='accept-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<other_username>[^/]+)/remove-friend$',
		views.remove_friend,
		name='remove-friend',
	),
	# friendship management: both `user` and `users` prefix
	re_path(r'^user(s)?/(?P<query_user>[^/]+)$', views.public_profile, name='public-profile'),
	re_path(
		r'^user(s)?/(?P<target_username>[^/]+)/friend-request$',
		views.friend_request,
		name='friend-request',
	),
	re_path(
		r'^user(s)?/(?P<target_username>[^/]+)/cancel-friend-request$',
		views.cancel_friend_request,
		name='cancel-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<origin_username>[^/]+)/deny-friend-request$',
		views.deny_friend_request,
		name='deny-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<origin_username>[^/]+)/accept-friend-request$',
		views.accept_friend_request,
		name='accept-friend-request',
	),
	re_path(
		r'^user(s)?/(?P<other_username>[^/]+)/remove-friend$',
		views.remove_friend,
		name='remove-friend',
	),
]
