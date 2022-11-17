from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.oneTextField import OneTextField
from common.fileUpload.userPath import userDirectoryPath


class ProductCategory(OneTextField):

    def __str__(self):
        return str(self.text)

    def products_list(self):
        data = Products.objects.filter(type=self)
        return data

    class Meta:
        verbose_name = _('Ürün Kategori')
        verbose_name_plural = _('Ürün Kategori')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Products(OneTextField):
    type = models.ForeignKey(ProductCategory, related_name='products_type', blank=True, on_delete=models.CASCADE,
                             null=True, verbose_name=_('Ürün Kategori'))
    image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                              verbose_name=_('Ürün Görseli'))
    price = models.DecimalField(verbose_name=_("Fiyat"), help_text=_("Minimum 0.01"), max_digits=19, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))], )

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = _('Ürünler')
        verbose_name_plural = _('Ürünler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
