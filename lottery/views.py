from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CashBox, FamilyMember, Membership


# Views

@login_required
def box_list(request):
    """Displays the list of all CashBoxes."""
    boxes = CashBox.objects.all()
    return render(request, 'lottery/box_list.html', {'boxes': boxes})


@login_required
def box_detail(request, box_id):
    """Displays details of a specific CashBox."""
    box = CashBox.objects.get(id=box_id)
    members = Membership.objects.filter(cash_box=box, cycle=box.current_cycle)
    return render(request, 'lottery/box_detail.html', {
        'box': box,
        'members': members
    })


def register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a FamilyMember for the user
            FamilyMember.objects.create(user=user)
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# URL Patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views
    path('', box_list, name='box_list'),  # Main page showing box list
    path('box/<int:box_id>/', box_detail, name='box_detail'),  # Box detail page
    path('register/', register, name='register'),  # User registration
]
