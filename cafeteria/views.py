from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
#列出所有产品或者给出筛选后的产品
#category_slug通过所给产品类别来有选择性的筛选
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 
                  'cafeteria/product/list.html', 
                  {'category': category,
                  'categories': categories,
                  'products': products})
#接受id和slug来检索product实例
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
            'cafeteria/product/detail.html',
            {'product': product,
            'cart_product_form': cart_product_form})
