from django.urls import path
from .views import *

urlpatterns = [
    # path("html/",html_view, name="html"),
    # path('session1/',session_data,name="sessiondata"),
    # path('getsession/',get_session,name="getsession"),
    # path('delsession/',del_session,name="delsession"),
    path("student/create/",student_view,name="student-add"),
    path("student/delete/<int:stu_id>/",student_delete,name="stu-del"),
    path("std/edit/",stuent_edit,name="stu-edit"),
    path("student/form/<int:id>/",student_create,name="stu-form"),
    path("student/form/",student_create,name="stu-forms"),
    path("student/edit_form/",student_update,name="stu-update"),
    path("product/create/",product_view,name="pro-create"),
    path("pro/edit/<int:pro_id>/",pro_edit,name="pro-edit"),
    path("query/",product_query,name="query"),
    path("orm/",orm_view,name="orm"),
    path('image/',image_view,name="image"),
    path('student/api/getall',student_getall),
    path('std/api/getall',StudentView.as_view())
]