from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index_view),
    path('add_question_answer', views.add_question_answer),
    path('search_question_answer', views.search_question_answer),
    path('del_question_answer', views.del_question_answer),
    path('ch_question_answer/<int:q_id>', views.ch_question_answer),
    # path('ch_question_answer', views.ch_question_answer),

]