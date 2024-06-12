from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from .models import QNA
import time

def index_view(request):
    return render(request, 'admin_server/index.html')

def search_question_answer(request):
    if request.method == "GET":
        result = QNA.objects.all()
        return render(request, 'admin_server/search_question_answer.html', locals())

def add_question_answer(request):
    if request.method == "GET":
        return render(request, 'admin_server/add_question_answer.html')
    elif request.method == "POST":
        part = request.POST['part']
        question = request.POST['question']
        answer = request.POST['answer']
        add_date = time.strftime('%Y-%m-%d %H:%M:%S')
        ch_date = time.strftime('%Y-%m-%d %H:%M:%S')
        add = QNA(part=part, question=question, answer=answer, add_date=add_date, ch_date=ch_date)
        add.save()
        return HttpResponseRedirect('search_question_answer')
    return HttpResponseRedirect('search_question_answer')

def del_question_answer(request):
    if request.method == "GET":
        return HttpResponseRedirect('search_question_answer')
    elif request.method == "POST":
        id = request.POST['id_to_delete']
        d1 = QNA.objects.get(id=id)
        d1.delete()
        return HttpResponseRedirect('search_question_answer')

def ch_question_answer(request, q_id):
    try:
        q_a = QNA.objects.get(id=q_id)
    except Exception as e:
        print(f'Error: {e}')
        return HttpResponse("Error: id is not found")
    if request.method == "GET":
        return render(request, 'admin_server/ch_question_answer.html', locals())
    elif request.method == "POST":
        part = request.POST['part']
        question = request.POST['question']
        answer = request.POST['answer']
        ch_date = time.strftime('%Y-%m-%d %H:%M:%S')

        q_a.part = part
        q_a.question = question
        q_a.answer = answer
        q_a.ch_date = ch_date
        q_a.save()

        return HttpResponseRedirect('/admin_server/search_question_answer')