from django.shortcuts import render
from .models import studd,S,User,Food,Nutrition,Sports,SportsCategory
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
    objs = Food.objects.filter(fcid_id=type)
    # print(obj[0])
    # return render(request,'login.html')
    result = []
    for i in range(len(objs)):
        result.append({})
        foodid = objs[i].fid
        result[-1]['id'] = foodid
        result[-1]['foodcalorie'] = objs[i].fk
        # result[-1]['ap'] = objs[0].ap
        result[-1]['foodname'] = objs[i].fn
        nutrition = Nutrition.objects.filter(fid=foodid)
        result[-1]['carbohydrate'] = nutrition[0].nc
        result[-1]['protein'] = nutrition[1].nc
        result[-1]['fat'] = nutrition[2].nc
        result[-1]['fibrin'] = nutrition[3].nc
        # for j in range(len(nutrition)):
        #     result[-1]['carbohydrate'] = nutrition[j].nc
        #     result[-1]['protein'] = nutrition[j].nc
        #     result[-1]['fat'] = nutrition[j].nc
        #     result[-1]['fibrin'] = nutrition[j].nc
        print(result)
    return JsonResponse({'code': 1, 'data': result})
    # return render(request, "search", {'data': result})


def searchByPage(request):
    type = request.GET.get('type')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize*(currentPage-1)
    endIndex = fromIndex+pageSize
    total = Food.objects.filter(fcid_id=type).count()
    print('食物种类：', type)
    objs = Food.objects.filter(fcid_id=type)[fromIndex:endIndex]
    result = []
    for i in range(len(objs)):
        result.append({})
        foodid = objs[i].fid
        result[-1]['id'] = foodid
        result[-1]['foodcalorie'] = objs[i].fk
        # result[-1]['foodimage'] = objs[i].fp
        result[-1]['foodname'] = objs[i].fn
        nutrition = Nutrition.objects.filter(fid=foodid)
        result[-1]['carbohydrate'] = nutrition[0].nc
        result[-1]['protein'] = nutrition[1].nc
        result[-1]['fat'] = nutrition[2].nc
        result[-1]['fibrin'] = nutrition[3].nc
        # for j in range(len(nutrition)):
        #     result[-1]['carbohydrate'] = nutrition[j].nc
        #     result[-1]['protein'] = nutrition[j].nc
        #     result[-1]['fat'] = nutrition[j].nc
        #     result[-1]['fibrin'] = nutrition[j].nc
    print(result)
    return JsonResponse({'code': 1, 'data': result, 'total': total})
    # return render(request, "search", {'data': result})


def findByInput(request):
    foodname = request.GET.get('foodname')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize*(currentPage-1)
    endIndex = fromIndex+pageSize
    total = Food.objects.filter(fn__contains=foodname).count()
    objs = Food.objects.filter(fn__contains=foodname)[fromIndex:endIndex]
    result = []
    for i in range(len(objs)):
        result.append({})
        foodid = objs[i].fid
        result[-1]['id'] = foodid
        result[-1]['foodcalorie'] = objs[i].fk
        # result[-1]['ap'] = objs[i].ap
        result[-1]['foodname'] = objs[i].fn
        nutrition = Nutrition.objects.filter(fid=foodid)
        result[-1]['carbohydrate'] = nutrition[0].nc
        result[-1]['protein'] = nutrition[1].nc
        result[-1]['fat'] = nutrition[2].nc
        result[-1]['fibrin'] = nutrition[3].nc
    print(result)
    print(total)
    return JsonResponse({'code': 1, 'data': result, 'total': total})


def sportByPage(request):
    type = request.GET.get('type')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize*(currentPage-1)
    endIndex = fromIndex+pageSize
    total = Sports.objects.filter(scid_id=type).count()
    print('运动种类：', type)
    objs = Sports.objects.filter(scid_id=type)[fromIndex:endIndex]
    result = []
    for i in range(len(objs)):
        result.append({})
        sportid = objs[i].sid
        result[-1]['sportname'] = objs[i].sn
        result[-1]['id'] = sportid
        result[-1]['sportcalorie'] = objs[i].sk
        # result[-1]['sportimage'] = objs[i].sp
    print(result)
    return JsonResponse({'code': 1, 'data': result, 'total': total})


def findSportByInput(request):
    sportname = request.GET.get('sportname')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize*(currentPage-1)
    endIndex = fromIndex+pageSize
    total = Sports.objects.filter(sn__contains=sportname).count()
    objs = Sports.objects.filter(sn__contains=sportname)[fromIndex:endIndex]
    result = []
    for i in range(len(objs)):
        result.append({})
        sportid = objs[i].sid
        result[-1]['sportname'] = objs[i].sn
        result[-1]['id'] = sportid
        result[-1]['sportcalorie'] = objs[i].sk
        # result[-1]['sportimage'] = objs[i].sp
    print(result)
    print(total)
    return JsonResponse({'code': 1, 'data': result, 'total': total})


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


