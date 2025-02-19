from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Payroll, Contact
from .forms import PayrollForm

@login_required
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        ins = Contact(first_name=first_name, last_name=last_name, contact_number=contact_number, email=email)
        ins.save()
        print(first_name, last_name, contact_number, email)
    
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contact.html', context)






def delete_payroll(request, payroll_id):
    payroll = get_object_or_404(Payroll, pk=payroll_id)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'payroll_confirm_delete.html', {'payroll': payroll})


def update_payroll(request, payroll_id):
    payroll = get_object_or_404(Payroll, pk=payroll_id)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'payroll_update.html', {'form': form})




def register_payroll(request):
    if request.method=='POST':
        name=request.POST['name']
        department=request.POST['department']
        phone=request.POST['phone']
        salary=request.POST['salary']
        print(name, department, phone, salary)
        ins=Payroll(name=name, department=department,phone=phone,salary=salary)
        ins.save()
    
    return render(request, 'payroll_register.html')




@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    context = {'payrolls': payrolls}
    return render(request, 'payroll_list.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'loging.html')

def logout_user(request):
    logout(request)
    return redirect('home')
