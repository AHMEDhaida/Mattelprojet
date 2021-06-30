from pyexpat.errors import messages
from django.contrib import messages
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404

from installation.models import Installation, Direction

from .forms import EquipementForm, EquipInstall,EquipementFormm, CategorieForm,DirectionForm
from .models import Equipement,Category
from mathfilters.templatetags.mathfilters import sub

from .filter import EquipementFilter
from django.contrib.auth.decorators import login_required
from equipement import models
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from accounts.models import Profile
from django.contrib.admin.models import LogEntry

from django.contrib.auth.decorators import permission_required





# Create your views here.
def pie_chart(request):
    equipement_service = Installation.objects.filter(service='En service')
    list_quip = Equipement.objects.all()
    equipement_panne = Installation.objects.filter(service='En panne')
    labels = ["En service", "Hors service", "En panne"]
    data = [10,40,40]


    return render(request, 'pie.html', {
        'labels': labels,
        'data': data,
    })
#Equipement

@login_required(login_url='login')
@admin_only
def home(request):
        object_E = Equipement.objects.all()
        list_quip = Equipement.objects.all()
        list_I = Installation.objects.all()
        object_T = Category.objects.all()
        object_D = Direction.objects.all()
        Num_E = Equipement.objects.all().count()
        Num_I = Installation.objects.all().count()
        Num_D = Direction.objects.all().count()
        Num_U = User.objects.all().count()
        profile = Profile.objects.all()
        user = User.objects.all()
        logs = LogEntry.objects.all()  # or you can filter, etc.
        equipement_service = Installation.objects.filter(service='En service')
        equipement_panne = Installation.objects.filter(service='En panne')
        
        
       

        paginator = Paginator(object_D, 2)
        page_numbre = request.GET.get('page')
        page_obj = paginator.get_page(page_numbre)

        context = {
            'list_quip': list_quip,
            'list_I': list_I,

            'object_E': object_E,

            'object_T': object_T,
            'filter': filter,
            'Num_E': Num_E,
            'Num_I': Num_I,
            'Num_D': Num_D,
            'Num_U': Num_U,
            'profile':profile,
            'user':user,
            'object_D': page_obj,
            'logs': logs,
            # 'labels': labels,
            #'data': data,

            'equipement_service':equipement_service,
            'equipement_panne':equipement_panne,
           
            

        }
        return render(request, 'base.html', context)


@login_required(login_url='accounts/login/')

def listEquipement(request):
    object_E = Equipement.objects.all()
    list_quip = Equipement.objects.all()
    object_T = Category.objects.all()
    object_D = Direction.objects.all()
    Num_E = Equipement.objects.all().count()
    Num_I = Installation.objects.all().count()
    Num_D = Direction.objects.all().count()
    profile = Profile.objects.all()
    user = User.objects.all()
    logs = LogEntry.objects.all()  # or you can filter, etc.
    equipement_service = Installation.objects.filter(service='En service')
    equipement_panne = Installation.objects.filter(service='En panne')
    equipement_remplace = Installation.objects.filter(service='A remplace')

    # filters
    filter = EquipementFilter(request.GET, queryset=object_E)
    list_quip = filter.qs

    # paginator = Paginator(object_E, 5)
    # page_numbre = request.GET.get('page')
    # page_obj = paginator.get_page(page_numbre)

    context = {
        'list_quip': list_quip,
        # 'object_E': page_obj,
        'object_T': object_T,
        'filter': filter,
        'Num_E': Num_E,
        'Num_I': Num_I,
        'Num_D': Num_D,
        'profile': profile,
        'user': user,
        'object_D': object_D,
        'logs': logs,

        'equipement_service': equipement_service,
        'equipement_panne': equipement_panne,
        'equipement_remplace': equipement_remplace,

    }
    return render(request, 'list_equipement.html', context)

@login_required(login_url='accounts/login/')
@allowed_users(allowed_roles=['admin'])
def listuser(request):
    profile = Profile.objects.all()

    user = User.objects.all()
    Num_E = Equipement.objects.all().count()
    Num_I = Installation.objects.all().count()
    Num_D = Direction.objects.all().count()
    paginator = Paginator(user, 10)
    page_numbre = request.GET.get('page')
    page_obj = paginator.get_page(page_numbre)
    context = {
        'profile': profile,
        'user': page_obj,
        'Num_E': Num_E,
        'Num_I': Num_I,
        'Num_D': Num_D,

    }
    return render(request, 'users.html', context)

@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])

def Ajout_E(request):
    if request.method == "POST":
        equipementform = EquipementForm(request.POST)
        if equipementform.is_valid():
            myform = equipementform.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"L'equipemet du numero  {myform.num_serie} est bien ajoute")

            return redirect('/ajouter')
    else:
        equipementform = EquipementForm()
    return render(request, 'ajouter.html', {'equipementform': equipementform})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def update_E(request, pk):

    equipement = Equipement.objects.get(id=pk)
    form = EquipementForm(instance=equipement)

    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            myform = form.save(commit=False)
            form.author = request.user
            myform.save()


            return redirect('/')

    context = {'form':form}
    return render(request, 'update_equipement.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])


def delete_E(request, pk):
    equipement = Equipement.objects.get(id=pk)
    if request.method == "POST":
        equipement.delete()
        return redirect('/')

    context = {'item':equipement}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])


def EquipementDetail(request, equipement_id):
    equipement_installe= get_object_or_404(Equipement, pk=equipement_id)
    inst= Installation.objects.filter(equipement_installe=equipement_id)
    # inst_id = Installation.objects.get(id=equipement_installe.installation_equipement.id)

    # equip_id = Installation.objects.get(id=equipement_installe.id)

    # inst_equip = Installation.equipement_installe
    # installation_equipement:releted_name between equipement and installation
    # check before save data from comment form
    if request.method == 'POST':
        installation_form = EquipInstall(data=request.POST)
        if installation_form.is_valid():
            deja_installe = installation_form.save(commit=False)
            deja_installe.author = request.user
            deja_installe.equipement_installe = equipement_installe
            # group = Group.objects.get(name='customer')
            # deja_installe.groups.add(group)
            deja_installe.save()
            messages.success(
                request, f"Felicitation l'equipemet est bien installer")
            return redirect('equip:detail_equipement', equipement_id)
        # else:
        #     return redirect('equip:detail_equipement', equipement_id)
    else:
        installation_form = EquipInstall()

    context = {
        'title': 'detail equipement',
        'equipement_installe': equipement_installe,
        # 'inst_equip': inst_equip,
        'inst':inst,
        'installation_form': installation_form,
        # 'inst_id':inst_id,

    }

    return render(request, 'detail_equipement.html', context)

@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])
def EquipementCreate(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"L'equipemet du numero  {myform.num_serie} est bien ajoute")
            return redirect(reverse('equip:add_equipement'))
    else:
        form = EquipementForm()

    return render(request, 'add_equipement.html', {'form': form})



#afficher info d'equipement
def EquipementDetail(request, equipement_id):
    equipement_installe= get_object_or_404(Equipement, pk=equipement_id)
    inst= Installation.objects.filter(equipement_installe=equipement_id)
    if request.method == 'POST':
        installation_form = EquipInstall(data=request.POST)
        # Atribut_inst = AtributForm(data=request.POST)
        if installation_form.is_valid():
            deja_installe = installation_form.save(commit=False)
            deja_installe.author = request.user
            deja_installe.equipement_installe = equipement_installe
            # Atribut_inst.equipement_installe.etat_equipement='1'
            # Atribut_inst.save()

            deja_installe.save()
            messages.success(
                request, f"Felicitation l'equipemet est bien installer")
            return redirect('equip:detail_equipement', equipement_id)
        # else:
        #     return redirect('equip:detail_equipement', equipement_id)
    else:
        installation_form = EquipInstall()

    context = {
        'title': 'detail equipement',
        'equipement_installe': equipement_installe,
        # 'inst_equip': inst_equip,
        'inst':inst,
        'installation_form': installation_form,
        # 'Atribut_inst':Atribut_inst
        #  'inst_id':inst_id,
        # 'insID':insID,

    }

    return render(request, 'detail_equipement.html', context)
def UserDetail(request, user_id):
    profile = Profile.objects.get(id=user_id)
    user = User.objects.get(id=user_id)

    context = {
        'user': user,
        'profile': profile

    }

    return render(request, 'detail_user.html', context)



# modifier equipement
@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])
def EquipementUpdate(request, equipement_id):
    equipement=Equipement.objects.get(id=equipement_id)
    form=EquipementFormm(instance=equipement)

    if request.method == 'POST':
        form=EquipementFormm(request.POST, instance=equipement)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"L'equipemet du numero  {myform.num_serie} est bien modifier")
            return redirect('equip:detail_equipement',equipement_id)

    context = {
        'title': 'Modifier_equipement',
        'form': form
        }

    return render(request,'update_equipement.html', context)



# delet equipement

def EquipementDeleteView(request, equipement_id):
    equipement=Equipement.objects.get(id=equipement_id)
    if request.method == 'POST':
        equipement.delete()
        messages.success(
            request, f"Felicitation l'equipemet avec numero  {equipement.num_serie} est bien supprimer")
        return redirect('equip:listE')

    context = {
        'title': 'Supprimer_equipement',
        'equipement': equipement
        }

    return render(request,'equipement_confirm_delete.html', context)


def UserDeleteView(request, user_id):
    profile = Profile.objects.get(id=user_id)
    user=User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(
            request, f"Felicitation l'user de numero  {user.username} est bien supprimer")
        return redirect('equip:listU')

    context = {
        'title': 'Supprimer_user',
        'user': user,
        'profile': profile
        }

    return render(request,'user_confirm_delete.html', context)

#view cataegorie equipement
@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])
def category_table(request):
    list_cat=Category.objects.all()
    list_direction = Direction.objects.all()
    Num_E = Equipement.objects.all().count()
    Num_I = Installation.objects.all().count()
    Num_D = Direction.objects.all().count()

    context={
       'title':'Categorie des equipements et les directions',
        'list_cat':list_cat,
        'list_direction': list_direction,
        'Num_E': Num_E,
        'Num_I': Num_I,
        'Num_D': Num_D,
    }
    return render(request,'category_table.html',context)


#add categorie equipement
# @login_required(login_url='user_auth:login')
@allowed_users(allowed_roles=['admin'])
def CategorietCreate(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            myform=form.save()
            messages.success(
                request, f"Felicitations la categorie  {myform.name}  est bien ajoute")
            return redirect(reverse('equip:add_categorie'))
    else:
        form = CategorieForm()

    context = {
        'title': "Categorie D'equipement",
        'form':form,

    }
    return render(request, 'add_categorie.html', context)

#edit categorie equipement
# @login_required(login_url='user_auth:login')
@allowed_users(allowed_roles=['admin'])
def CategoryUpdate(request, categorie_id):
    category=Category.objects.get(id=categorie_id)
    form=CategorieForm(instance=category)

    if request.method == 'POST':
        form=CategorieForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation categorie {category.name} est bien modifier")
            return redirect('equip:home')

    context = {
        'title': 'Modifier_categorie',
        'form': form
        }

    return render(request,'update_categorie.html', context)




#direction
#add direction
# @login_required(login_url='user_auth:login')
@allowed_users(allowed_roles=['admin'])
def DirectionCreate(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            myform=form.save()
            messages.success(
                request, f"Felicitation nom de la direction  {myform.Nom} est bien ajoute")
            return redirect(reverse('equip:add_direction'))
    else:
        form = DirectionForm()

    context = {
        'title': "Adresse De La Direction",
        'form':form,

    }
    return render(request, 'add_direction.html', context)


#edit direction
# @login_required(login_url='user_auth:login')
@allowed_users(allowed_roles=['admin'])
def DirectionUpdate(request, direction_id):
    direction=Direction.objects.get(id=direction_id)
    form=DirectionForm(instance=direction)

    if request.method == 'POST':
        form=DirectionForm(request.POST, instance=direction)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation nom direction {direction.Nom} est bien modifier")
            return redirect('equip:home')

    context = {
        'title': 'Modifier_direction',
        'form': form
        }

    return render(request,'update_direction.html', context)


