from django.shortcuts import render


def add_to_menu(menu, parental, parent, n):
    menu.append((parent, n))
    if parent.pk in parental.keys():
        for item in parental[parent.pk]:
            menu = add_to_menu(menu, parental, item, n+1)
    return menu


def menu(request):
    return render(request, 'base.html')
