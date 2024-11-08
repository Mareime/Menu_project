from django.shortcuts import redirect, render
from .models import menu

def home(request):
    return render(request, 'home.html')

from django.shortcuts import redirect, render
from django import forms
from .models import menu  

class MenuForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ['nom', 'description', 'prix']

def home(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()  
            menu_items = menu.objects.all()
            return render(request, 'home.html', {'menu_items': menu_items})
           
    else:
        form = MenuForm()

    return render(request, 'home.html', {'form': form})
def delete_menu_item(request):
    if request.method == "POST":
        menu_item_id = request.POST.get('menu_item_id')
        menu_item = menu.objects.get(id=menu_item_id)
        menu_item.delete()
        return redirect('home')

