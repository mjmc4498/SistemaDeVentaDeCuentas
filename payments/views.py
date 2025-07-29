from django.shortcuts import render
from .models import Bill

def bill_list(request):
    """
    Muestra una lista de todas las cuentas pendientes.
    """
    pending_bills = Bill.objects.filter(status='pending').order_by('created_at')
    context = {
        'bills': pending_bills
    }
    return render(request, 'payments/bill_list.html', context)

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def pay_bill(request, bill_id):
    """
    Marca una cuenta como pagada y redirige a la lista de cuentas,
    mostrando un mensaje de éxito.
    """
    bill = get_object_or_404(Bill, pk=bill_id)
    bill.status = 'paid'
    bill.save()
    messages.success(request, f'¡El pago de "{bill.title}" se ha procesado con éxito!')
    return redirect('payments:bill_list')
