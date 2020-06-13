from django.urls import path,include
from . import views
urlpatterns = [
    path('add-exam',views.add_exam,name="add-exam"),
    path('quest/edit/<int:id>/<sha>',views.edit_question,name="edit-question"), # dhyam de yaha par id matlab exam ki 'id' se h
    path('question/<task>/<sha>',views.add_question,name="add-question"), # dhyam de yaha par id matlab exam ki 'id' se h

]
