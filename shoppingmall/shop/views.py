from django.shortcuts import render, get_object_or_404
from shop.models import Item, Order
# Create your views here.

def index(request):
    context={}
    return render(request,'index.html',context)

def itemdetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'itemdetail.html',{'item':item})

def orderlist(request):
    return render(request, 'orderlist.html')