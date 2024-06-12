from django.http import  HttpResponse ,HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse

def logout_view(request):
    logout(request)
    # 重定向到登录页面或其他页面
    return redirect('login')  # 假设你有一个名为'login'的URL别名指向登录页面

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success', 'message': '登出成功！'})
    else:
        # 如果不是POST请求，可以重定向到登录页面或其他页面
        # 但对于AJAX请求，我们通常会返回JSON响应
        return JsonResponse({'status': 'error', 'message': '请使用POST方法登出。'}, status=405)



def caculator_view(request):
    if request.method == "GET":
        return render(request, 'caculator.html')
    elif request.method == "POST":
        dic = {}
        a = request.POST['num1']
        b = request.POST['num2']
        op = request.POST['op']
        a = int(a)
        b = int(b)
        if op in ['add', 'sub', 'mul', 'div']:
            if op == 'add':
                result1 = a + b
            elif op == 'sub':
                result1 = a - b
            elif op == 'mul':
                result1 = a * b
            elif op == 'div':
                result1 = a / b
        else:
            return HttpResponseBadRequest
        dic['result'] = result1
        dic['numa'] = a
        dic['numb'] = b
        dic['rop'] = op
        return render(request, 'caculator.html', dic)

