from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Local, Producto, Promocion

def crear_promocion(request):
    if request.method == 'POST':
        # Aquí capturas los datos y los guardas (Django llamará al clean() automáticamente)
        # Por simplicidad en esta guía, nos enfocaremos en mostrar el formulario.
        pass
    
    locales = Local.objects.all()
    return render(request, 'core/crear_promo.html', {'locales': locales})

# Endpoint para cargar el Dropdown de Productos según el Local
def cargar_productos(request):
    local_id = request.GET.get('local_id')
    productos = Producto.objects.filter(local_id=local_id).values('id', 'nombre')
    return JsonResponse(list(productos), safe=False)