from django.db import models


class Product(models.Model):
    name        = models.CharField(max_length=200, db_index=True)
    slug        = models.SlugField(max_length=200, db_index=True, null=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='products/', blank=True, null=True)
    stock       = models.PositiveIntegerField()
    available   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True, null=True)
    updated     = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('name',)

    """
    Remember to add 'comma' after ordering element. Otherwise you will get an error like below
    ERRORS: 'ordering' must be a tuple or list (even if you want to order by only one field).
    """

    def __str__(self):
        return self.name
