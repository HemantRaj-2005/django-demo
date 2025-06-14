from django.urls import path
from members.views import show_memebers, member_detail

urlpatterns = [
    path('members/',show_memebers,name="all-members"),
    path('members/detail/<int:id>/',member_detail,name="detail-member"),
]