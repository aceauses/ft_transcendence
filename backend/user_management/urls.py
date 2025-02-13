from django.urls import include, path

from . import views
from .api_views import OauthCallBackView, OauthView

app_name = 'users'

# urls under `/users/api/friends/`
friends_urls = [
	path('active/', views.friends_users_active, name='friends'),
	path('active/<str:username>/', views.friends_users_active, name='friends-public'),
	path('inactive/', views.friends_requests, name='friends-requests'),
	path('request/<str:username>/', views.friends_send_request, name='friends-send-request'),
	path('cancel/<str:username>/', views.friends_cancel, name='friends-cancel-request'),
	path('accept/<str:username>/', views.friends_accept, name='friends-accept-request'),
	path('deny/<str:username>/', views.friends_deny, name='friends-deny-request'),
	path('remove/<str:username>/', views.friends_remove, name='friends-remove'),
]

urlpatterns = [
	path('api/oauth/', OauthView.as_view(), name='oauth'),
	path('api/oauth-callback/', OauthCallBackView.as_view(), name='api-callback'),
	path('api/blocked/', views.blocked_users, name='blocked_users'),
	path('api/block/<str:username>/', views.block_user, name='block_user'),
	path('api/unblock/<str:username>/', views.unblock_user, name='unblock_user'),
	path('api/friends/', include(friends_urls)),
	path('api/register/', views.register, name='register'),
	path('api/login/', views.login_view, name='login'),
	path('api/logout/', views.logout_view, name='logout'),
	path('api/get_account_details/', views.get_account_details, name='get-account-details'),
	path('api/update_profile/', views.update_profile, name='update-profile'),
	path('api/change_password/', views.change_password, name='change-password'),
	path('api/check_authentication/', views.check_authentication, name='check-authentication'),
	# TODO: remove once dashboard is feature complete @follow-up
	path('<str:query_user>', views.public_profile, name='public-profile'),
]
