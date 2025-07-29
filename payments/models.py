from django.db import models

class Bill(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagada'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"{self.title} - ${self.amount}"

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
