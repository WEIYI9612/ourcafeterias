from django.contrib import admin
from .models import Category,Product

#把模型注册到管理站点，可管理产品和产品分类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    #list_editable设置可被编辑的字段，并且都在管理站点的列表页被列出
    #任何在list_editable的字段也必须在list_display中
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

