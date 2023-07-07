data=[]
creators = []



 #data order
#data_order = urlopen("http://admin.dswiftbd.com:9001/v0/order/details/")
#data_json_order = json.loads(data_order.read())
#data_o = data_json_order



#order datta loader................
def data_loader():
    data_order = urlopen("http://admin.dswiftbd.com:9001/v0/order/details/")
    data_json_order = json.loads(data_order.read())
    data_o = data_json_order
    return data_o


#Specific order data depends on user................
def specific_data(x,data_o):
    specific_user_data = []
    data_len = len(data_o)
    for data in range(data_len):
        creator = creators.append(data_o[data]['creator'])
        if data_o[data]['creator'] == x:
            specific_user_data.append(data_o[data])

    return specific_user_data
#Payment Status loader................
def payment_status_loader(y):
    all_user = y
    pass


#Delivery Status loader................
def delivery_status(x):
    all_status=[]
    created=0
    on_hub = 0
    on_the_way = 0
    delivered = 0
    canceled = 0
    data_len = len(x)
    for data in range(data_len):
        if x[data]['status']==1:
            created = created+1
        elif x[data]['status']==2:
            on_hub= on_hub+1
        elif x[data]['status']==3:
            on_the_way= on_the_way+1
        elif x[data]['status']==4:
            delivered= delivered+1
        else:
            canceled = canceled+1
    all_status.append(created)
    all_status.append(on_hub)
    all_status.append(on_the_way)
    all_status.append(delivered)
    all_status.append(canceled)

    return all_status

def get_all_users(phone):
    url2 = "http://admin.dswiftbd.com:9001/v0/user?phone="
    final_url = "".join([url2,phone])
    data1 = urlopen(final_url)
    data_json = json.loads(data1.read())
    return data_json



# Create your views here.
'''
def loginpage(request):
    user_data = data_loader()
    if request.method =="POST":
        phone = request.POST['phone']
        passw = request.POST['pass']
        request.session['phone'] = phone
        request.session['pass'] = passw

        data = get_all_users(phone)

        print("session number "+request.session['phone'])

        #data order
        #data_order = urlopen("http://admin.dswiftbd.com:9001/v0/order/details/")
        #data_json_order = json.loads(data_order.read())
        #data_o = data_json_order
        specific_user_data=specific_data(data[0]['id'],user_data)
        delivery_stat = delivery_status(specific_user_data)
        #print(object.filter(data_o__contains=[{"creator": 58}]))
    
        #data_j = json.dumps(data, indent=4)
        print(data[0]['password'])
        main_pass = data[0]['password']
        if passw==main_pass:

            return render(request,"dswiftweb/dashboard.html",{
                        "data": data[0],
                        "data1":specific_user_data,
                        "created": delivery_stat[0]+delivery_stat[1],
                        "on_the_way": delivery_stat[2],
                        "delivered": delivery_stat[3],
                        "canceled": delivery_stat[4]
                    })
        else:
            return render(request,"dswiftweb/pages-login.html",{

            })
    return render(request,"dswiftweb/pages-login.html")

def dashboard(request):
    return render(request,"dswiftweb/notmatch.html",{
    "data": request.session['phone']
    })

'''

# 2nd part
def home(request):
    if 'login' in request.session:
        status= 1
    else:
        status= 0
    
    return render(request,"dswiftweb/index.html",{
        "status": status,
        "active": "home"
    })
def about(request):
    if 'login' in request.session:
        status= 1
    else:
        status= 0
    return render(request,"dswiftweb/about.html",{
    "status": status,
    "active":"about"
    
    })
def services(request):
    if 'login' in request.session:
        status= 1
    else:
        status= 0
    return render(request,"dswiftweb/service.html",{
         "status": status,
         "active":"services"
    })
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # send mail
        send_mail(
        subject,
        'Hi I am '+name+' .\n'+message,
        email,
        ['info@dswiftbd.com'],
        )
        
        
        
    if 'login' in request.session:
        status= 1
    else:
        status= 0
    return render(request,"dswiftweb/contact.html",{
    "status": status,
    "active":"contact",
    
    })



def loginpage(request):
    if request.method =="POST":
        phone = request.POST['phone']
        passw = request.POST['pass']
        request.session['phone'] = phone
        request.session['pass'] = passw
        request.session['login']=True
        status = request.session['login']
        return HttpResponseRedirect('dashboard')
    else:
        return render(request,"dswiftweb/pages-login.html",{
    
        })
def dashboard(request):
    user_data = data_loader()
    
    
    if 'phone' in request.session:
        phone = request.session['phone']
        passw = request.session['pass']
        data = get_all_users(phone)
        specific_user_data=specific_data(data[0]['id'],user_data)
        delivery_stat = delivery_status(specific_user_data)
        main_pass = data[0]['password']
        if passw==main_pass:
             return render(request,"dswiftweb/dashboard.html",{
                        "data": data[0],
                        "data1":specific_user_data,
                        "created": delivery_stat[0]+delivery_stat[1],
                        "on_the_way": delivery_stat[2],
                        "delivered": delivery_stat[3],
                        "canceled": delivery_stat[4]
                    })
        else:
            return HttpResponseRedirect('login')
        
    else:
        return HttpResponseRedirect('login')
    '''
    data = get_all_users(phone)
    specific_user_data=specific_data(data[0]['id'],user_data)
    delivery_stat = delivery_status(specific_user_data)
    main_pass = data[0]['password']
    if passw==main_pass:
         return render(request,"dswiftweb/dashboard.html",{
                        "data": data[0],
                        "data1":specific_user_data,
                        "created": delivery_stat[0]+delivery_stat[1],
                        "on_the_way": delivery_stat[2],
                        "delivered": delivery_stat[3],
                        "canceled": delivery_stat[4]
                    })
    else:
        return HttpResponseRedirect('login')'''
    #return render(request,"dswiftweb/dashboard.html")
