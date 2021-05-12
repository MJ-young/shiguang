from django.shortcuts import render
from .models import studd,S,User,Food
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.
def test(request):
    return JsonResponse({"status": 0, "message": "this is django aaaa"})


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    result_login = 0
    if User.objects.filter(username=username, password=password).first():
        result_login = 1
        print("result", result_login)
    return HttpResponse(result_login)
    # return render(request,'login.html')

def getfood(request):
    fid = request.GET.get('foodid')
    obj = Food.objects.filter(fid=fid)
    # print(obj[0])
    # return render(request,'login.html')
    result = []
    result.append({})
    result[-1]['fk'] = obj[0].fk
    result[-1]['ap'] = obj[0].ap
    result[-1]['fn'] = obj[0].fn
    print(result)
    return JsonResponse({'code': 1, 'data': result[0]})

def search(request):
    type = request.GET.get('type')
    print('食物种类：', type)
    objs = Food.objects.filter(fcid=type)
    # print(obj[0])
    # return render(request,'login.html')
    result = []
    for i in range(len(objs)):
        result.append({})
        result[-1]['id'] = objs[0].fid
        result[-1]['foodcalorie'] = objs[0].fk
        # result[-1]['ap'] = objs[0].ap
        result[-1]['foodname'] = objs[0].fn
        print(result)
    return JsonResponse({'code': 1, 'data': result})
    # return render(request, "search", {'data': result})

def loginn(request):
    objs = S.objects.filter()
    # print(objs)
    result = []
    for i in range(len(objs)):
        # print(objs[i].values())
        result.append({})
        result[-1]['xh'] = objs[i].xh
        result[-1]['xm'] = objs[i].xm
        result[-1]['xb'] = objs[i].xb
        result[-1]['jg'] = objs[i].jg
        result[-1]['csrq'] = objs[i].csrq
        result[-1]['sjhm'] = objs[i].sjhm

    # print(result)
    canlogin = 1
    # {result, canlogin}
    return JsonResponse({'code': 1, 'data': canlogin, 'result' : result, 'message': '{result, canlogin}'})


def regist(request):
    return render(request,'regist.html')
class UserController:
    def userLogin(request):
        if request.method == 'POST':
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            user = studd.objects.get(user_name=user_name)
            if user.password != password :
                return HttpResponse("密码错误")
        return render(request,"userinfo.html",{'user':user})

    def userRegist(request):
        if request.method == 'POST':
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            age = request.POST.get("age")
            studd.objects.create(user_name=user_name, password=password, age=age)
        return render(request, "login.html")

    def userInfo(request,id):
        user = studd.objects.get(id=id)
        return render(request, "userinfo.html", {'user': user})


