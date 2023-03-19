from django.shortcuts import render
from django.db import connection
from .forms import *


def createtable(request) :
    
    outputOfQuery1 = []
    outputOfQuery2 = []
    outputOfQuery3 = []
    outputOfQuery4 = []
    
    with connection.cursor() as cursor:
        sqlQuery1 = "CREATE table product (maker char(1), model int, type char(10), primary key (model))"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()
        
        sqlQuery2 = "CREATE table pc (model int, speed float, ram int, hd int, price int, \
                    primary key (model), foreign key (product.model))"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()
        
        sqlQuery3 = "CREATE table laptop (model int, speed float, ram int, hd int, screen float, price int, \
                    primary key (model), foreign key (product.model))"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()
        
        sqlQuery4 = "CREATE table printer (model int, color char(5), type char(10), price int, \
                    primary key (model), foreign key (product.model))"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()
        
        connection.commit()
        connection.close()
    
        for temp in fetchResultQuery1:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputOfQuery1.append(eachRow)
            
        for temp in fetchResultQuery2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputOfQuery2.append(eachRow)
            
        for temp in fetchResultQuery3:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4], 'price': temp[5]}
            outputOfQuery3.append(eachRow)
            
        for temp in fetchResultQuery4:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputOfQuery4.append(eachRow)
    
    return render(request, 'myApp/index', {"product": outputOfQuery1, "pc": outputOfQuery2, "laptop": outputOfQuery2, "printer": outputOfQuery3})
    

def insertProduct(request) :
    if request.method == "POST":
        formProduct = ProductForm(request.POST)
        if formProduct.is_valid():
            formProduct.save()
    else:
        formProduct = ProductForm()
    return render(request, "myApp/input.html", {'form': formProduct})

def insertPc(request) :
    if request.method == "POST":
        formPc = PCForm(request.POST)
        if formPc.is_valid():
            formPc.save()
    else:
        formPc = PCForm()
    return render(request, "myApp/input.html", {'form': formPc})

def insertLaptop(request) :
    if request.method == "POST":
        formLaptop = LaptopForm(request.POST)
        if formLaptop.is_valid():
            formLaptop.save()
    else:
        formLaptop = LaptopForm()
    return render(request, "myApp/input.html", {'form': formLaptop})

def insertPrinter(request) :
    if request.method == "POST":
        formPrinter = PrinterForm(request.POST)
        if formPrinter.is_valid():
            formPrinter.save()
    else:
        formPrinter = PrinterForm()
    return render(request, "myApp/input.html", {'form': formPrinter})

def query1(request) :
    outputOfQuery1 = []
    
    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT avg(hd) FROM pc;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()
        
        connection.commit()
        connection.close()
    
        for temp in fetchResultQuery1:
                eachRow = {'avg_hd': temp[0]}
                outputOfQuery1.append(eachRow)
    
    return render(request, 'myApp/query1.html', {"query1": outputOfQuery1})

def query2(request) :
    outputOfQuery2 = []
    
    with connection.cursor() as cursor:
        sqlQuery2 = "SELECT product.maker, avg(laptop.speed) from laptop, product \
                    where product.model = laptop.model group by product.maker;"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()
        
        connection.commit()
        connection.close()
    
        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'avg_speed': temp[1]}
            outputOfQuery2.append(eachRow)
    
    return render(request, 'myApp/query2.html', {"query2": outputOfQuery2})

def query3(request) :
    outputOfQuery3 = []
    
    with connection.cursor() as cursor:
        sqlQuery3 = "SELECT laptop.model, product.maker, laptop.price from product, laptop \
                    where product.model = laptop.model group  by product.maker \
                    having count(product.maker)=1;"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()
        
        connection.commit()
        connection.close()
    
        for temp in fetchResultQuery3:
            eachRow = {'model': temp[0], 'maker': temp[1], 'price': temp[2]}
            outputOfQuery3.append(eachRow)
    
    return render(request, 'myApp/query3.html', {"query3": outputOfQuery3})

def query4(request) :
    outputOfQuery4 = []
    
    with connection.cursor() as cursor:
        sqlQuery4 = "SELECT printer.model, p.maker, printer.price from product p, printer \
                    where printer.model = p.model and printer.price >= (select max(price) from product, printer \
                    where printer.model = product.model and product.maker = p.maker) group by p.maker;"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()
        
        connection.commit()
        connection.close()
    
        for temp in fetchResultQuery4:
            eachRow = {'model': temp[0], 'maker': temp[1], 'price': temp[2]}
            outputOfQuery4.append(eachRow)
    
    return render(request, 'myApp/query4.html', {"query4": outputOfQuery4})
    

def display(request):
    outputProduct = []
    outputOfQuery1 = []
    outputPc=[]
    outputLaptop=[]
    outputPrinter=[]
    outputOfQuery2=[]
    outputOfQuery3=[]
    outputOfQuery4=[]
    
    with connection.cursor() as cursor:
        sqlQueryProduct = "SELECT maker, model, type FROM product ORDER BY maker asc;"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()
        
        sqlQueryPc = "SELECT model, speed, ram, hd, price FROM pc;"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()
        
        sqlQueryLaptop = "SELECT model, speed, ram, hd, screen, price FROM laptop;"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()
        
        sqlQueryPrinter = "SELECT model, color, type, price FROM printer;"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()
        
        ###############################################################

        sqlQuery1 = "SELECT avg(hd) FROM pc;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()
        
        sqlQuery2 = "SELECT product.maker, avg(laptop.speed) from laptop, product \
                    where product.model = laptop.model group by product.maker;"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()
        
        sqlQuery3 = "SELECT laptop.model, product.maker, laptop.price from product, laptop \
                    where product.model = laptop.model group  by product.maker \
                    having count(product.maker)=1;"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()
        
        sqlQuery4 = "SELECT printer.model, p.maker, printer.price from product p, printer \
                    where printer.model = p.model and printer.price >= (select max(price) from product, printer \
                    where printer.model = product.model and product.maker = p.maker) group by p.maker;"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultProduct:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct.append(eachRow)
            
        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc.append(eachRow)
            
        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4], 'price': temp[4]}
            outputLaptop.append(eachRow)
            
        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter.append(eachRow)

        ##########################################################

        for temp in fetchResultQuery1:
            eachRow = {'avg_hd': temp[0]}
            outputOfQuery1.append(eachRow)
            
        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'avg_speed': temp[1]}
            outputOfQuery2.append(eachRow)
            
        for temp in fetchResultQuery3:
            eachRow = {'model': temp[0], 'maker': temp[1], 'price': temp[2]}
            outputOfQuery3.append(eachRow)
            
        for temp in fetchResultQuery4:
            eachRow = {'model': temp[0], 'maker': temp[1], 'price': temp[2]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/index.html',{"product": outputProduct, "pc": outputPc, "laptop": outputLaptop, "printer": outputPrinter,\
                "query1": outputOfQuery1, "query2": outputOfQuery2, "query3": outputOfQuery3, "query4": outputOfQuery4})
