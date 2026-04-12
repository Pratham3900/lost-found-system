from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import RegisterForm, LoginForm, LostItemForm, FoundItemForm, ClaimRequestForm
from .models import LostItem, FoundItem, ClaimRequest, Notification


def index(request):
    return render(request, 'lostfound_app/index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'lostfound_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('dashboard_home')
                else:
                    return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'lostfound_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def report_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            LostItem.objects.create(
                item_name=form.cleaned_data['item_name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                lost_date=form.cleaned_data['lost_date'],
                location=form.cleaned_data['location'],
                image=form.cleaned_data['image'],
                contact_name=request.user.username,
                contact_email=request.user.email
            )

            Notification.objects.create(
                message=f"Lost item '{form.cleaned_data['item_name']}' reported successfully."
            )

            return redirect('lost_list')
    else:
        form = LostItemForm()

    return render(request, 'lostfound_app/report_lost.html', {'form': form})


@login_required
def report_found_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            FoundItem.objects.create(
                item_name=form.cleaned_data['item_name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                found_date=form.cleaned_data['found_date'],
                location=form.cleaned_data['location'],
                image=form.cleaned_data['image'],
                finder_name=request.user.username,
                finder_email=request.user.email
            )

            Notification.objects.create(
                message=f"Found item '{form.cleaned_data['item_name']}' submitted successfully."
            )

            return redirect('found_list')
    else:
        form = FoundItemForm()

    return render(request, 'lostfound_app/report_found.html', {'form': form})



def lost_item_list(request):
    lost_items = LostItem.objects.all()
    return render(request, 'lostfound_app/lost_list.html', {'lost_items': lost_items})


def found_item_list(request):
    found_items = FoundItem.objects.all()
    return render(request, 'lostfound_app/found_list.html', {'found_items': found_items})



def match_items(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    matched_items = []

    for lost in lost_items:
        for found in found_items:
            if (
                lost.item_name.lower() == found.item_name.lower()
                or lost.category.lower() == found.category.lower()
            ):
                matched_items.append({
                    'lost_item': lost,
                    'found_item': found
                })

    return render(request, 'lostfound_app/match_list.html', {'matched_items': matched_items})


@login_required
def claim_item(request, item_id):
    lost_item = get_object_or_404(LostItem, id=item_id)

    if request.method == 'POST':
        form = ClaimRequestForm(request.POST)
        if form.is_valid():
            ClaimRequest.objects.create(
                lost_item=lost_item,
                claimant_name=request.user.username,
                claimant_email=request.user.email,
                proof_details=form.cleaned_data['proof_details']
            )

            Notification.objects.create(
                message=f"Claim request submitted for '{lost_item.item_name}'."
            )

            return redirect('notification_list')
    else:
        form = ClaimRequestForm()

    return render(request, 'lostfound_app/claim_item.html', {
        'form': form,
        'lost_item': lost_item
    })



def notification_list(request):
    notifications = Notification.objects.all().order_by('-created_at')
    return render(request, 'lostfound_app/notification.html', {'notifications': notifications})

@login_required
def dashboard_home(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    total_lost = LostItem.objects.count()
    total_found = FoundItem.objects.count()
    total_claims = ClaimRequest.objects.count()
    pending_claims = ClaimRequest.objects.filter(claim_status='Pending').count()
    approved_claims = ClaimRequest.objects.filter(claim_status='Approved').count()
    rejected_claims = ClaimRequest.objects.filter(claim_status='Rejected').count()

    context = {
        'total_lost': total_lost,
        'total_found': total_found,
        'total_claims': total_claims,
        'pending_claims': pending_claims,
        'approved_claims': approved_claims,
        'rejected_claims': rejected_claims,
    }
    return render(request, 'lostfound_app/dashboard.html', context)


@login_required
def dashboard_lost_items(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    lost_items = LostItem.objects.all().order_by('-id')
    return render(request, 'lostfound_app/dashboard_lost_items.html', {'lost_items': lost_items})


@login_required
def dashboard_found_items(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    found_items = FoundItem.objects.all().order_by('-id')
    return render(request, 'lostfound_app/dashboard_found_items.html', {'found_items': found_items})


@login_required
def dashboard_match_items(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    matched_items = []

    for lost in lost_items:
        for found in found_items:
            if (
                lost.item_name.lower() == found.item_name.lower()
                or lost.category.lower() == found.category.lower()
            ):
                matched_items.append({
                    'lost_item': lost,
                    'found_item': found
                })

    return render(request, 'lostfound_app/dashboard_match_items.html', {'matched_items': matched_items})


@login_required
def dashboard_claim_requests(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    claim_requests = ClaimRequest.objects.all().order_by('-id')
    return render(request, 'lostfound_app/dashboard_claim_requests.html', {'claim_requests': claim_requests})

@login_required
def reject_claim(request, claim_id):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    claim = get_object_or_404(ClaimRequest, id=claim_id)
    claim.claim_status = 'Rejected'
    claim.save()

    Notification.objects.create(
        message=f"Claim for '{claim.lost_item.item_name}' has been rejected."
    )

    return redirect('dashboard_claim_requests')


@login_required
def approve_claim(request, claim_id):
    if not request.user.is_staff:
        return HttpResponse("Unauthorized")

    claim = get_object_or_404(ClaimRequest, id=claim_id)

    if request.method == 'POST':
        note = request.POST.get('handover_note')

        claim.claim_status = 'Approved'
        claim.handover_note = note
        claim.save()

        Notification.objects.create(
            message=f"Your claim for '{claim.lost_item.item_name}' is approved."
        )

        return redirect('dashboard_claim_requests')

    return render(request, 'lostfound_app/approve_claim.html', {'claim': claim})
@login_required
def dashboard_approved_claims(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to access this page.")

    approved_requests = ClaimRequest.objects.filter(claim_status='Approved').order_by('-id')
    return render(request, 'lostfound_app/dashboard_approved_claims.html', {'approved_requests': approved_requests})

@login_required
def approved_claims(request):
    approved_requests = ClaimRequest.objects.filter(
        claimant_email=request.user.email,
        claim_status='Approved'
    )
    return render(request, 'lostfound_app/approved_claims.html', {'approved_requests': approved_requests})


@login_required
def rejected_claims(request):
    rejected_requests = ClaimRequest.objects.filter(
        claimant_email=request.user.email,
        claim_status='Rejected'
    )
    return render(request, 'lostfound_app/rejected_claims.html', {'rejected_requests': rejected_requests})