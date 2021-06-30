from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm, UserRole
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from pyexpat.errors import messages
from django.contrib import messages
from .models import Profile
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


# Create your views here.


@allowed_users(allowed_roles=['admin'])
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # group = Group.objects.get(name='superviseur')
            # us.groups.add(group)
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(
                request, f"L'utilisateur est bien Ajouer")
            return redirect('accounts:signup')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def Ajouterprofile(request):
    if request.method == "POST":
        object = ProfileForm(request.POST)
        if object.is_valid():
            myform = object.save(commit=False)
            myform.user = request.user
            myform.save()

            return redirect('accounts:profile')
    else:
        object = ProfileForm()
    return render(request, 'accounts/ajouterProfile.html', {'object': object})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    user = User.objects.all()
    logs = LogEntry.objects.all()  # or you can filter, etc.
    context = {
        'profile': profile,
        'user': user,
        'logs': logs,
    }
    return render(request, 'accounts/profile.html', context)


def Rolesuperuser(request, pk):
    user = User.objects.get(id=pk)
    form = UserRole(instance=user)

    if request.method == 'POST':
        form = UserRole(request.POST, instance=user)
        if form.is_valid():
            myform = form.save(commit=False)

            myform.save()

            return redirect('equip:listU')

    context = {'form': form}
    return render(request, 'accounts/rolesuperuser.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/password_change_form.html', args)


def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)
