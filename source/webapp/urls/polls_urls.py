from django.urls import path
from webapp.views import PollCreate, PollDelete, PollDetail, PollList, PollUpdate

urlpatterns = [
    path('', PollList.as_view(), name='poll_list'),
    path('poll/<int:pk>', PollDetail.as_view(), name='poll_view'),
    path('poll/add', PollCreate.as_view(), name='poll_new'),
    path('poll/update/<int:pk>', PollUpdate.as_view(), name='polls_edit'),
    path('poll/delete/<int:pk>', PollDelete.as_view(), name='poll_delete')
    ]