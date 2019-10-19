from django.urls import path
from webapp.views import ChoicesList, ChoicesUpdate, ChoicesDetail, ChoicesDelete, ChoicesCreate

urlpatterns = [
    path('', ChoicesList.as_view(), name='choices_list'),
    path('choices/<int:pk>', ChoicesDetail.as_view(), name='choices_view'),
    path('choices/add/<int:pk>', ChoicesCreate.as_view(), name='choices_new'),
    path('choices/update/<int:pk>', ChoicesUpdate.as_view(), name='choices_edit'),
    path('choices/delete/<int:pk>', ChoicesDelete.as_view(), name='choices_delete')
    ]