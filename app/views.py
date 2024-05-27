from django.shortcuts import redirect, render

from app.models import Product

# Create your views here.
def index(request):
    data=Product.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if  request.method=="POST":
        Name=request.POST.get('Name')
        Number=request.POST.get('Number')
        Cost=request.POST.get('Cost')
        
        query=Product(Name=Name,Number=Number,Cost=Cost)
        query.save()
    return render(request,"index.html")
def updateData(request,id):
    d=Product.objects.get(id=id)
    context={"d":d}
    if request.method=="POST":
        Name=request.POST.get('Name')
        Number=request.POST.get('Number')
        Cost=request.POST.get('Cost')
        
        edit=Product.objects.get(id=id)       
        edit.Name=Name
        edit.Number=Number
        edit.Cost=Cost
        
        edit.save()
        
        return redirect("/")
    return render(request,"edit.html",context)
def deleteData(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    
    return redirect("/")  
    



