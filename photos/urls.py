from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='landing'),
    path('myaccount/', views.mine, name='myaccount'),
    path('myaccount/edit/', views.edit, name='edit'),
    path('comment/<int:post_id>', views.comment_on, name='comment'),
    path('user/(?P<user_id>\d+)', views.user, name='aboutuser'),
    path('like/(?P<post_id>\d+)', views.like, name='like'),
    path('save/(?P<post_id>\d+)', views.save, name='save'),
    path('search/(?P<name>.+)', views.find, name='save'),
    path('follow_or_not/(?P<user_id>\d+)', views.togglefollow, name='follow_or_not'),
    path('unlike/(?P<post_id>\d+)', views.unlike, name='unlike')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)