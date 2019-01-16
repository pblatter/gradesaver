from django.conf.urls import url
from fileupload.views import HomeView, Find_Class, FileUploads, Domain_View #,upload_file

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^find/$', Find_Class.as_view(), name='find'),
    url(r'^exam_upload/$', FileUploads.as_view(), name='exam_upload'),
    url(r'^domain/$', Domain_View.as_view(), name='domain_page'),
]