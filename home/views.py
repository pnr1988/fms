from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from fms.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import messages
from .forms import AddressForm, BankDetailsForm, EducationalDocumentForm, TimesheetForm
from .models import Address, BankDetails, EducationalDocument, Timesheet

#home
@login_required
def home(request):
    address = Address.objects.filter(user=request.user).all()
    bank_details = BankDetails.objects.filter(user=request.user).all()
    educational_docs = EducationalDocument.objects.filter(user=request.user).all()
    # print(address)
    context = {
        'address': address,
        'bank_details': bank_details,
        'educational_docs': educational_docs
    }
    return render(request, "home.html", context)

#Personal Info
@login_required
def personal_info(request):
    user = request.user

    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        bank_details_form = BankDetailsForm(request.POST)
        document_form = EducationalDocumentForm(request.POST, request.FILES)
        # print(address_form)
        # print(bank_details_form)
        # print(document_form)

        if address_form.is_valid() and bank_details_form.is_valid() and document_form.is_valid():
            address_form.instance.user = user
            address_form.save()
            bank_details_form.instance.user = user
            bank_details_form.save()
            document_form.instance.user = user
            document_form.save()

            messages.success(request, "Personal info added successfull.")
            return redirect("home")
        else:
            messages.warning(request, "Please correct the details!")

    else:
        address_form = AddressForm(instance=user)
        bank_details_form = BankDetailsForm(instance=user)
        document_form = EducationalDocumentForm(instance=user)

    return render(request, "personalinfo.html", {'address_form':address_form,'bank_details_form': bank_details_form,'document_form':document_form})

#Personal Info
@login_required
def timesheet_submit(request):
    user = request.user

    if request.method == 'POST':
        timesheet_form = TimesheetForm(request.POST, request.FILES)
        if timesheet_form.is_valid():
            timesheet_form.instance.user = user
            timesheet_form.save()

            messages.success(request, "You have successfully submitted your timesheet.")
            return redirect("home")
        else:
            messages.warning(request, "Please correct the details!")
    else:        
        timesheet_form = TimesheetForm()

    return render(request, "timesheet.html", {'timesheet_form':timesheet_form})
