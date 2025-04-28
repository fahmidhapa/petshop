from django.shortcuts import render,redirect
from . models import Reg_tbl,pet_tbl,cart_tbl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . forms import Regform

# Create your views here.
def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method=='POST':
        fname=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        obj=Reg_tbl.objects.create(fnm=fname,mob=mobile,eml=email,psw=password,cpsw=cpassword)
        obj.save()
        if obj:
            return redirect('/login')
        else:
            return render(request,"signup.html")
    return render(request,"signup.html")


def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=Reg_tbl.objects.filter(eml=email,psw=password)
        if obj:
            request.session['ema']=email
            request.session['psa']=password
            for m in obj:
                idl=m.id
            request.session['idn']=idl
            return render(request,"index.html")
        else:
            msg="Invalid credentials...."
            return render(request,"signin.html",{"error":msg})
    return render(request,"signin.html")

def user(request):
    obb=Reg_tbl.objects.all()
    return render(request,'user.html',{'data':obb})   

def edit(request,pk):
    ob=Reg_tbl.objects.filter(id=pk)
    if request.method=='POST':
        fnm=request.POST.get('fn')
        idl=request.POST.get('idn')
        mobi=request.POST.get('mb')
        eml=request.POST.get('em')
        psw=request.POST.get('ps')
        obb=Reg_tbl.objects.filter(id=idl)
        obb.update(fnm=fnm,eml=eml,mob=mobi,psw=psw)
        return redirect('/users')
    return render(request,"oneuser.html",{'data':ob})


def delete(request,pk):
    ob=Reg_tbl.objects.filter(id=pk)
    ob.delete()
    return redirect('/users')

def pets(request):
    if request.method=='POST':
        pname=request.POST.get('pn')
        price=request.POST.get('pr')
        pimag=request.FILES.get('im')
        desc=request.POST.get('ds')
        obj=pet_tbl.objects.create(pnm=pname,prc=price,pim=pimag,des=desc)
        obj.save()
        if obj:
            return render(request,"pets.html",{"msg":"details uploaded" })
    return render(request,"pets.html")

def allpets(request):
  pob=pet_tbl.objects.all()
  return render(request,'allpets.html',{"data":pob})

def addtocart(request,pid):
    pobj=pet_tbl.objects.get(id=pid)
    uid=request.session['idn']
    uobj=Reg_tbl.objects.get(id=uid)
    cartitem,created = cart_tbl.objects.get_or_create(user=uobj,pet=pobj)
    if not created:
        cartitem.qty+=1
        cartitem.save()
        messages.success(request,"quantity changed...") 
    messages.success(request,"item added to cart....")
    return redirect('/allpet')

def viewcart(request):
    uid=request.session['idn']
    cobj= Reg_tbl.objects.get(id=uid)
    cartobj=cart_tbl.objects.filter(user=cobj)
    if cartobj:
        total_price = 0
        for m in cartobj:
            p=m.pet.prc * m.qty
            total_price+=p
        return render(request,"cart.html",{"cartitem":cartobj,"total":total_price})
    else:
        return render(request,"cart.html",{"em":"your cart is empty...."})
        # messages.success(request,"your cart is empty....")
        # return redirect('/viewcart')

def cartitem_delete(request,cid):
    cartobj =cart_tbl.objects.filter(id=cid)
    cartobj.delete()
    return redirect('/viewcart')

def sendmail(request):
    if request.method=="POST":
        mail=request.POST.get('mail')
        sub=request.POST.get('sub')
        msg=request.POST.get('msg')
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[mail],fail_silently=False)
        return render(request,"sendmail.html",{"success":"Mail send successfully..."})
    return render(request,"sendmail.html")


def formview(request):
    form=Regform()
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            fn=form.cleaned_data.get('fnm')
            mb=form.cleaned_data.get('mob')
            em=form.cleaned_data.get('eml')
            pw=form.cleaned_data.get('psw')
            cpw=form.cleaned_data.get('cpsw')
            obj=Reg_tbl.objects.create(fnm=fn,mob=mb,eml=em,psw=pw,cpsw=cpw)
            obj.save()
            if obj:
                msg='Registration successfull..........'
                return render(request,"formview.html",{"form":form,"success":msg})

    return render(request,"formview.html",{"form":form})