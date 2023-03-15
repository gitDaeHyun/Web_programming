from django.shortcuts import render

# Create your views here.
def price(request,name,cnt) :
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if name in product_price :
        context = {
            'num' : 1,
            'price' : int(product_price[name]),
            'cnts' : cnt,
            'product' :  name
        }
    elif name not in product_price :
        context = {
            'num' : 2,
            'name' : name
            
            
        }
    return render(request, 'price.html',context)