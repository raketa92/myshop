from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorations.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = 
