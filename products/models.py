from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)

    """
    Remember to add 'comma' after ordering element. Otherwise you will get an error like below
    ERRORS: 'ordering' must be a tuple or list (even if you want to order by only one field).
    """

    def __str__(self):
        return self.name
