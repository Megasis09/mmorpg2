from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ad, AdResponse
from .forms import AdForm, AdResponseForm

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.created_by = request.user
            ad.save()
            return redirect('view_ad', ad_id=ad.id)
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})

def view_ads(request):
    ads = Ad.objects.all()
    return render(request, 'view_ads.html', {'ads': ads})

def view_ad(request, ad_id):
    ad = Ad.objects.get(pk=ad_id)
    if request.method == 'POST':
        form = AdResponseForm(request.POST)
        if form.is_valid():
            ad_response = form.save(commit=False)
            ad_response.user = request.user
            ad_response.ad = ad
            ad_response.save()
            return redirect('view_ad', ad_id=ad_id)
    else:
        form = AdResponseForm()
    return render(request, 'view_ad.html', {'ad': ad, 'form': form})

@login_required
def edit_ad(request, ad_id):
    ad = Ad.objects.get(pk=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.save()
            return redirect('view_ad', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)
    return render(request, 'edit_ad.html', {'form': form})

@login_required
def view_responses(request):
    ads = Ad.objects.filter(created_by=request.user)
    responses = []
    for ad in ads:
        ad_responses = AdResponse.objects.filter(ad=ad)
        responses.append({'ad': ad, 'responses': ad_responses})
    return render(request, 'view_responses.html', {'responses': responses})