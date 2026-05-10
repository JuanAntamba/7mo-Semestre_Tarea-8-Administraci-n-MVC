from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse 
from .models import Local, Producto, Promocion

def crear_promocion(request):
    error_mensaje = None 
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        descuento = request.POST.get('porcentaje_descuento')
        inicio = request.POST.get('hora_inicio')
        fin = request.POST.get('hora_fin')

        try:
            producto = Producto.objects.get(id=producto_id)
            nueva_promo = Promocion(
                producto=producto,
                porcentaje_descuento=descuento,
                hora_inicio=inicio,
                hora_fin=fin
            )
            nueva_promo.save() 
            return redirect('crear_promo') 
            
        except ValidationError as e:
            error_mensaje = e.messages[0] if hasattr(e, 'messages') else str(e)
            
        except Exception:
            error_mensaje = "Error de integridad: Asegúrese de que todos los campos sean válidos."

    locales = Local.objects.all()
    return render(request, 'core/crear_promo.html', {
        'locales': locales, 
        'error': error_mensaje 
    })

def cargar_productos(request):
    local_id = request.GET.get('local_id')
    productos = Producto.objects.filter(local_id=local_id).values('id', 'nombre')
    return JsonResponse(list(productos), safe=False)