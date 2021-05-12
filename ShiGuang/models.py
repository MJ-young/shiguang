from django.db import models

# Create your models here.
class studd(models.Model):
    user_name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    age = models.IntegerField()
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    enable = models.BooleanField(default=True)

class S(models.Model):
    # 学生表
    xh = models.IntegerField(primary_key=True, verbose_name='学号')
    xm = models.CharField(max_length=10, verbose_name='姓名')
    xb = models.CharField(max_length=4, verbose_name='性别')
    csrq = models.DateField(verbose_name='出生日期')
    jg = models.CharField(max_length=10, verbose_name='籍贯')
    sjhm = models.CharField(max_length=22, verbose_name='手机号码')
    mm = models.CharField(max_length=22, verbose_name='密码')

    # yxh = models.ForeignKey('D', on_delete=models.CASCADE, verbose_name='院系')  # 实际上为院系号

    class Meta:
        verbose_name = '学生大表'
        verbose_name_plural = '学生大表'

    def values(self):
        return [self.xh, self.xm, self.xb, self.csrq, self.jg, self.sjhm, self.yxh]

    def __str__(self):
        return str(self.xh)

class FoodCategory(models.Model):
    # 食物类别
    fcid = models.IntegerField(primary_key=True, verbose_name='食物类别id')
    fcn = models.CharField(max_length=50, verbose_name='食物类别名称')

    class Meta:
        verbose_name = '食物类别表'
        verbose_name_plural = '食物类别表'

class Food(models.Model):
    # 食物
    fid = models.IntegerField(primary_key=True, verbose_name='食物id')
    fcid = models.ForeignKey('FoodCategory', on_delete=models.CASCADE, verbose_name='食物类别id')
    fn = models.CharField(max_length=256, verbose_name='食物名称')
    fk = models.IntegerField(verbose_name='每克卡路里')
    ap = models.CharField(max_length=256, verbose_name='适宜人群')
    nap = models.CharField(max_length=256, verbose_name='不适人群')
    fp = models.CharField(max_length=256, verbose_name='食物图片')

    class Meta:
        verbose_name = '食物表'
        verbose_name_plural = '食物表'

    def __str__(self):
        return str(self.fk)

class SportsCategory(models.Model):
    # 运动类别
    scid = models.IntegerField(primary_key=True, verbose_name='运动类别id')
    scn = models.CharField(max_length=50, verbose_name='运动类别名称')

    class Meta:
        verbose_name = '运动类别表'
        verbose_name_plural = '运动类别表'

class Sports(models.Model):
    # 运动
    sid = models.IntegerField(primary_key=True, verbose_name='运动id')
    scid = models.ForeignKey('SportsCategory', on_delete=models.CASCADE, verbose_name='运动类别id')
    sn = models.CharField(max_length=256, verbose_name='运动名称')
    sk = models.IntegerField(verbose_name='每小时卡路里')
    sp = models.CharField(max_length=256, verbose_name='运动图片')

    class Meta:
        verbose_name = '运动表'
        verbose_name_plural = '运动表'

class NutritionCategory(models.Model):
    # 营养物质类别
    nid = models.IntegerField(primary_key=True, verbose_name='营养物质id')
    nn = models.CharField(max_length=50, verbose_name='营养物质名称')

    class Meta:
        verbose_name = '营养物质类别表'
        verbose_name_plural = '营养物质类别表'

class Nutrition(models.Model):
    # 食物营养
    fid = models.IntegerField(primary_key=True, verbose_name='食物id')
    nid = models.ForeignKey('NutritionCategory', on_delete=models.CASCADE, verbose_name='营养物质id')
    nc = models.IntegerField(verbose_name='含量')

    class Meta:
        verbose_name = '营养物质表'
        verbose_name_plural = '营养物质表'

class User(models.Model):
    # 用户信息
    userid = models.IntegerField(primary_key=True, verbose_name='用户id')
    username = models.CharField(max_length=256, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    sex = models.CharField(max_length=256, verbose_name='性别')
    height = models.IntegerField(verbose_name='身高')
    weight = models.IntegerField(verbose_name='体重')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'


class DietRecord(models.Model):
    # 饮食记录
    userid = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户id')
    drid = models.IntegerField(primary_key=True, verbose_name='饮食记录id')
    fid = models.ForeignKey('Food', on_delete=models.CASCADE, verbose_name='食物id')
    fw = models.IntegerField(verbose_name='食物重量')
    dd = models.DateField(verbose_name='饮食日期')

    class Meta:
        verbose_name = '饮食记录表'
        verbose_name_plural = '饮食记录表'

class SportsRecord(models.Model):
    # 运动记录
    userid = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户id')
    srid = models.IntegerField(primary_key=True, verbose_name='运动记录id')
    sid = models.ForeignKey('Sports', on_delete=models.CASCADE, verbose_name='运动id')
    st = models.IntegerField(verbose_name='运动时长')
    sd = models.DateField(verbose_name='运动日期')

    class Meta:
        verbose_name = '运动记录表'
        verbose_name_plural = '运动记录表'
