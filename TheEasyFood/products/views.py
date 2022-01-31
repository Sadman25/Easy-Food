from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import profile
from accounts.forms import userRegistration,profileRegistration
from .models import product,images,review,order
from .forms import reviewForm
import datetime

# Create your views here.
@login_required(login_url='loginPage')
def homePage(request):
    products = product.objects.all().order_by('-id') #Latest products will be shown at 1st
    context = {'products':products}
    return render (request, 'homepage.html',context)

@login_required(login_url='loginPage')
def productDetails(request,pk):
    product_details = product.objects.get(id=pk)  #Contains information of a particular product
    product_images = images.objects.filter(product=product.objects.get(id=pk)) #Contains information of a particular product's images
    new_review = reviewForm()
    reviews = review.objects.filter(product=product.objects.get(id=pk)).order_by('-id')

    if request.method == 'POST':
        new_review = reviewForm(request.POST)
        if new_review.is_valid():
            new_review = new_review.save(commit=False)
            new_review.product = product_details
            new_review.user = request.user
            new_review.time = datetime.datetime.now()
            new_review.save()
            return HttpResponseRedirect(product_details.get_absolute_url())

    context = {'product_details':product_details,
    'product_images':product_images,
    'new_review':new_review,
    'reviews':reviews
    }
    return render (request,'product_details.html',context)

@login_required(login_url='loginPage')
def search(request):
    query = request.GET.get('query')
    if query:
        products = product.objects.filter(product_name__icontains=query)
        context = {'products':products}
        return render(request,'search.html',context)
    else:
        return redirect('homePage')

@login_required(login_url='loginPage')
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')        
        address = request.POST.get('address', '')        
        phone = request.POST.get('phone', '')
        newOrder = order(items_json=items_json, customer=request.user, address=address,phone=phone)
        newOrder.save()        
        id = order.order_id
        messages.info (request, 'Your Order is accepted !!!')               
        return render (request,'checkout.html',{'id': id})
    return render (request,'checkout.html')

@login_required(login_url='loginPage')
def myOrders(request):
    orders = order.objects.all().order_by('-order_id') 
    context = {'orders':orders}
    print(orders[0].items_json)
    

    return render(request,'myorders.html',context)

@login_required(login_url='loginPage')
def myProfile(request,pk):
    previousInfo = profile.objects.get(id=pk)
    editUser = userRegistration(instance=request.user)
    editProfile = profileRegistration(instance=previousInfo)

    if request.method == 'POST':
        editUser = userRegistration(request.POST,instance=request.user)
        editProfile = profileRegistration(request.POST,request.FILES,instance=previousInfo)
        if editUser.is_valid() and editProfile.is_valid():
            editUser.save()
            editProfile.save()
            messages.success(request,'Account information is edited. Please login again..')
            return redirect('/')
    
    else:
        context = {'previousInfo':previousInfo,
        'editUser':editUser,
        'editProfile':editProfile}
        return render (request, 'myprofile.html',context)   


@login_required(login_url='loginPage')
def about(request):
    return render(request,'about.html')