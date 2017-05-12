from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                        verbose_name=_('category'))
    slug = models.SlugField(max_length=200, db_index=True, unique=True,
                        verbose_name=_('slug'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                    verbose_name=_('category'))
    name = models.CharField(max_length=200, db_index=True,
                    verbose_name=_('name'))
    slug = models.SlugField(max_length=200, db_index=True,
                    verbose_name=_('slug'))
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,
                    verbose_name=_('image'))
    description = models.TextField(blank=True,
                    verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2,
                    verbose_name=_('price'))
    stock = models.PositiveIntegerField(verbose_name=_('stock'))
    available = models.BooleanField(default=True,
                    verbose_name=_('available'))
    created = models.DateTimeField(auto_now_add=True,
                    verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True,
                    verbose_name=_('updated'))

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name

