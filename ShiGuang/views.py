from django.shortcuts import render
from .models import studd, S, User, Food, Nutrition, Sports, SportsCategory, DietRecord, SportsRecord
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import time

# Create your views here.
def test(request):
    return JsonResponse({"status": 0, "message": "this is django aaaa"})


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    result_login = 0
    user = User.objects.filter(username=username, password=password).first()
    if user:
        result_login = 1
        userid = user.userid
        print("result", result_login)
    return JsonResponse({'code': 1, 'result_login': result_login, 'userid': userid})


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
        result[-1]['img'] = objs[0].fp
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
    fromIndex = pageSize * (currentPage - 1)
    endIndex = fromIndex + pageSize
    total = Food.objects.filter(fcid_id=type).count()
    print('食物种类：', type)
    objs = Food.objects.filter(fcid_id=type)[fromIndex:endIndex]
    result = []
    for i in range(len(objs)):
        result.append({})
        foodid = objs[i].fid
        result[-1]['id'] = foodid
        result[-1]['foodcalorie'] = objs[i].fk
        result[-1]['img'] = objs[i].fp
        result[-1]['foodname'] = objs[i].fn
        result[-1]['isshow'] = 10
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
    fromIndex = pageSize * (currentPage - 1)
    endIndex = fromIndex + pageSize
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
        result[-1]['isshow'] = 10
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
    fromIndex = pageSize * (currentPage - 1)
    endIndex = fromIndex + pageSize
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
        result[-1]['img'] = objs[i].sp
        result[-1]['isshow'] = 0.1
    print(result)
    return JsonResponse({'code': 1, 'data': result, 'total': total})


def findSportByInput(request):
    sportname = request.GET.get('sportname')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize * (currentPage - 1)
    endIndex = fromIndex + pageSize
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
        result[-1]['isshow'] = 0.1
    print(result)
    print(total)
    return JsonResponse({'code': 1, 'data': result, 'total': total})


def addFoodRecord(request):
    userid = request.GET.get('userid')
    foodid = int(request.GET.get('foodid'))
    weight = int(request.GET.get('weight'))
    # 写个触发器添加时间、自动计算卡路里、生成记录ID到数据库
    DietRecord.objects.create(userid_id=userid, fid_id=foodid, fw=weight)
    objs = DietRecord.objects.all()
    result = []
    for i in range(len(objs)):
        result.append({})
        drid = objs[i].drid
        result[-1]['userid'] = objs[i].userid_id
        result[-1]['id'] = drid
        result[-1]['weight'] = objs[i].fw
    print(result)
    return JsonResponse({'code': 1, 'data': '添加成功'})


def addSportRecord(request):
    userid = request.GET.get('userid')
    sportid = int(request.GET.get('sportid'))
    time = float(request.GET.get('time'))
    print(time)
    # 写个触发器添加时间、自动计算卡路里、生成记录ID到数据库
    SportsRecord.objects.create(userid_id=userid, sid_id=sportid, st=time)

    objs = SportsRecord.objects.all()
    result = []
    for i in range(len(objs)):
        result.append({})
        srid = objs[i].srid
        result[-1]['userid'] = objs[i].userid_id
        result[-1]['id'] = srid
        result[-1]['time'] = objs[i].st
    print(result)
    return JsonResponse({'code': 1, 'data': '添加成功'})


def RecordByDate(request):
    userid = request.GET.get('userid')
    date = request.GET.get('date')
    objs1 = DietRecord.objects.filter(userid_id=userid, dd=date)
    dietlist = []
    for i in range(len(objs1)):
        dietlist.append({})
        dietlist[-1]['recardid'] = objs1[i].drid
        fid = objs1[i].fid_id
        dietlist[-1]['foodname'] = Food.objects.get(fid=fid).fn
        dietlist[-1]['foodweight'] = objs1[i].fw
        dietlist[-1]['foodcalorie'] = objs1[i].fkk
        dietlist[-1]['type'] = 'diet'
    print(dietlist)
    objs2 = SportsRecord.objects.filter(userid_id=userid, sd=date)
    sportlist = []
    for i in range(len(objs2)):
        sportlist.append({})
        sportlist[-1]['recardid'] = objs2[i].srid
        sid = objs2[i].sid_id
        sportlist[-1]['sportname'] = Sports.objects.get(sid=sid).sn
        sportlist[-1]['sporttime'] = objs2[i].st
        sportlist[-1]['sportcalorie'] = objs2[i].skk
        sportlist[-1]['type'] = 'sport'
    print(sportlist)
    return JsonResponse({'code': 1, 'dietlist': dietlist, 'sportlist': sportlist, 'message': '每日热量表'})


def DelRecard(request):
    type = request.GET.get('type')
    id = request.GET.get('recardid')
    print('recardid', id)
    if type == 'diet':
        DietRecord.objects.filter(drid=id).delete()
    else:
        SportsRecord.objects.filter(srid=id).delete()
    return JsonResponse({'code': 1, 'data': '删除成功'})

def addSport(request):
    print(request.GET.get('typeid'))
    scid = int(request.GET.get('typeid'))
    sn = request.GET.get('sportname')
    # sid = Sports.objects.all().count()+1
    sid =time.time()
    print(sn)
    sk = int(request.GET.get('sportk'))
    Sports.objects.create(scid_id=scid, sn=sn, sk=sk, sid=sid, sp=7)
    return JsonResponse({'code': 1, 'data': '添加成功'})


def delSport(request):
    sid = int(request.GET.get('sportid'))
    Sports.objects.filter(sid=sid).delete()
    return JsonResponse({'code': 1, 'data': '删除成功'})


def addFood(request):
    fcid = int(request.GET.get('typeid'))
    fn = request.GET.get('foodname')
    fk = int(request.GET.get('foodk'))
    # fid = Food.objects.all().count()+1
    fid = time.time()
    carbohydrate=int(request.GET.get('c1'))
    protein=int(request.GET.get('c1'))
    fat=int(request.GET.get('c1'))
    fibrin=int(request.GET.get('c1'))
    Food.objects.create(fcid_id=fcid, fn=fn, fk=fk, fid=fid, fp=4)
    Nutrition.objects.create(nid_id=1,fid=fid,nc=carbohydrate)
    Nutrition.objects.create(nid_id=2, fid=fid, nc=protein)
    Nutrition.objects.create(nid_id=3, fid=fid, nc=fat)
    Nutrition.objects.create(nid_id=4, fid=fid, nc=fibrin)
    return JsonResponse({'code': 1, 'data': '添加成功'})


def delFood(request):
    fid = int(request.GET.get('foodid'))
    Sports.objects.filter(fid=fid).delete()
    return JsonResponse({'code': 1, 'data': '删除成功'})


def propose(request):
    r1 = 0.3
    r2 = 0.5
    r3 = 0.2
    total = int(request.GET.get('totalCalorie'))
    c11 = r1*0.4*total
    c12 = r1*0.6*total
    c21 = r2 * 0.4 * total
    c22 = r2 * 0.6 * total
    c31 = r3 * 0.4 * total
    c32 = r3 * 0.6 * total
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    # obj1 = Food.objects.filter(fcid_id=2, fk__gte=c11, fk__lte=c12)[0:5]
    # for i in range(len(obj1)):
    #     result1.append({})
    #     result1[-1]['foodid'] = obj1[i].fid
    #     result1[-1]['foodname'] = obj1[i].fn
    #     result1[-1]['foodweight'] = 100
    # 蛋类 肉类
    i1 = 1
    obj1 = Food.objects.filter(fcid_id=2, fk__gte=c11/i1, fk__lte=c12/i1)[0:5]
    for i in range(len(obj1)):
        result1.append({})
        result1[-1]['foodid'] = obj1[i].fid
        result1[-1]['foodname'] = obj1[i].fn
        result1[-1]['foodweight'] = 100*i1
    # 蔬果
    i2 = 3
    obj2 = Food.objects.filter(fcid_id=4, fk__gte=c11/i2, fk__lte=c12/i2)[0:5]
    for i in range(len(obj2)):
        result2.append({})
        result2[-1]['foodid'] = obj2[i].fid
        result2[-1]['foodname'] = obj2[i].fn
        result2[-1]['foodweight'] = 100*i2
    # 主食
    i3=4
    obj3 = Food.objects.filter(fcid_id=1, fk__gte=c21/i3, fk__lte=c22/i3)[0:5]
    for i in range(len(obj3)):
        result3.append({})
        result3[-1]['foodid'] = obj3[i].fid
        result3[-1]['foodname'] = obj3[i].fn
        result3[-1]['foodweight'] = 100*i3
    # 菜肴
    i4=3
    obj4 = Food.objects.filter(fcid_id=10, fk__gte=c21/i4, fk__lte=c22/i4)[0:5]
    for i in range(len(obj4)):
        result4.append({})
        result4[-1]['foodid'] = obj4[i].fid
        result4[-1]['foodname'] = obj4[i].fn
        result4[-1]['foodweight'] = 100*i4
    # 饮料
    i5=3
    obj5 = Food.objects.filter(fcid_id=5, fk__gte=c31/i5, fk__lte=c32/i5)[0:5]
    for i in range(len(obj5)):
        result5.append({})
        result5[-1]['foodid'] = obj5[i].fid
        result5[-1]['foodname'] = obj5[i].fn
        result5[-1]['foodweight'] = 100*i5
    # 豆制品
    i6= 3
    obj6 = Food.objects.filter(fcid_id=6, fk__gte=c31/i6, fk__lte=c32/i6)[0:5]
    for i in range(len(obj6)):
        result6.append({})
        result6[-1]['foodid'] = obj6[i].fid
        result6[-1]['foodname'] = obj6[i].fn
        result6[-1]['foodweight'] = 100*i6

    return JsonResponse({'code': 1, 'data': '返回数据', 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'result6': result6})


# def proposeSport(request):
#     r1 = 0.3
#     r2 = 0.3
#     r3 = 0.4
#     total = int(request.GET.get('totalCalorie'))
#     type1 = int(request.GET.get('type1'))
#     type2 = int(request.GET.get('type2'))
#     type3 = int(request.GET.get('type3'))
#     c11 = r1*0.4*total
#     c12 = r1*0.6*total
#     c21 = r2 * 0.4 * total
#     c22 = r2 * 0.6 * total
#     c31 = r3 * 0.4 * total
#     c32 = r3 * 0.6 * total
#     result1 = []
#     result2 = []
#     result3 = []
#     obj1 = Food.objects.filter(scid_id=type1, sk__gte=c11, sk__lte=c12)[0:5]
#     for i in range(len(obj1)):
#         result1.append({})
#         result1[-1]['sportid'] = obj1[i].fid
#         result1[-1]['foodname'] = obj1[i].fn
#         result1[-1]['foodweight'] = 100
#     obj2 = Food.objects.filter(fcid_id=4, fk__gte=c11, fk__lte=c12)[0:5]
#     for i in range(len(obj2)):
#         result1.append({})
#         result1[-1]['foodid'] = obj2[i].fid
#         result1[-1]['foodname'] = obj2[i].fn
#         result1[-1]['foodweight'] = 100
#
#     obj3 = Food.objects.filter(fcid_id=1, fk__gte=c21, fk__lte=c22)[0:5]
#     for i in range(len(obj3)):
#         result2.append({})
#         result2[-1]['foodid'] = obj3[i].fid
#         result2[-1]['foodname'] = obj3[i].fn
#         result2[-1]['foodweight'] = 100
#     obj4 = Food.objects.filter(fcid_id=10, fk__gte=c21, fk__lte=c22)[0:5]
#     for i in range(len(obj4)):
#         result2.append({})
#         result2[-1]['foodid'] = obj4[i].fid
#         result2[-1]['foodname'] = obj4[i].fn
#         result2[-1]['foodweight'] = 100
#     obj5 = Food.objects.filter(fcid_id=5, fk__gte=c31, fk__lte=c32)[0:5]
#     for i in range(len(obj5)):
#         result3.append({})
#         result3[-1]['foodid'] = obj5[i].fid
#         result3[-1]['foodname'] = obj5[i].fn
#         result3[-1]['foodweight'] = 100
#     obj6 = Food.objects.filter(fcid_id=6, fk__gte=c31, fk__lte=c32)[0:5]
#     for i in range(len(obj6)):
#         result3.append({})
#         result3[-1]['foodid'] = obj6[i].fid
#         result3[-1]['foodname'] = obj6[i].fn
#         result3[-1]['foodweight'] = 100
#
#     return JsonResponse({'code': 1, 'data': '返回数据', 'result1': result1, 'result2': result2, 'result3': result3})


def getListByPage(request):
    type = request.GET.get('type')
    pageSize = int(request.GET.get('pageSize'))
    currentPage = int(request.GET.get('pageIndex'))
    fromIndex = pageSize * (currentPage - 1)
    endIndex = fromIndex + pageSize
    if type == 'food':
        total = Food.objects.all().count()
        objs = Food.objects.all()[fromIndex:endIndex]
        result = []
        for i in range(len(objs)):
            result.append({})
            result[-1]['id'] = objs[i].fid
            result[-1]['calorie'] = objs[i].fk
            result[-1]['name'] = objs[i].fn
        print(result)
    else:
        total = Sports.objects.all().count()
        objs = Sports.objects.all()[fromIndex:endIndex]
        result = []
        for i in range(len(objs)):
            result.append({})
            result[-1]['id'] = objs[i].sid
            result[-1]['calorie'] = objs[i].sk
            result[-1]['name'] = objs[i].sn
        print(result)

    return JsonResponse({'code': 1, 'list': result, 'total': total})

def edit(request):
    type = request.GET.get('type')
    id = int(request.GET.get('id'))
    name = request.GET.get('name')
    calorie = int(request.GET.get('calorie'))
    if type == 'food':
        Food.objects.filter(fid=id).update(fn=name, fk=calorie)
    else:
        Sports.objects.filter(sid=id).update(sn=name, sk=calorie)
    return JsonResponse({'code': 1, 'data': '修改成功'})

def delByid(request):
    type = request.GET.get('type')
    id = int(request.GET.get('id'))
    if type == 'food':
        Food.objects.filter(fid=id).delete()
    else:
        Sports.objects.filter(sid=id).delete()
    return JsonResponse({'code': 1, 'data': '修改成功'})

