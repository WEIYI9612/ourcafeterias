from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    #name是产品类名
    name = models.CharField(max_length=200,
                            db_index=True)
    #slug用来为这个类创建URL
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    #检索一个对象的URL
    def get_absolute_url(self):
            return reverse('cafeteria:product_list_by_category',
                           args=[self.slug])
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    #category是一个链接向Category的ForeignKey，是多对一的关系
    category = models.ForeignKey(Category, 
                                 related_name='products')
    #name是产品的名字
    name = models.CharField(max_length=200, db_index=True)
    #slug用来为这个产品建立URL
    slug = models.SlugField(max_length=200, db_index=True)
    #image是可选的产品图片
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    #description是可选的产品描述
    description = models.TextField(blank=True)
    #price是十进制字段，产品价格，使用DecimalField可以避免精度问题
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #stock保存产品的库存
    stock = models.PositiveIntegerField()
    #available记录产品是否可供购买
    available = models.BooleanField(default=True)
    #created当对象被创建时这个字段被保存
    created = models.DateTimeField(auto_now_add=True)
    #update当对象最后一次被更新时这个字段被保存
    updated = models.DateTimeField(auto_now=True)
    #检索一个对象的URL
    def get_absolute_url(self):
        return reverse('cafeteria:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        #指定id和slug字段的共同索引，使用这两个字段来查询产品
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name


    