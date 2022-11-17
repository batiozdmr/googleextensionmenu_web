from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.oneTextField import OneTextField


class ProductCategory(OneTextField):

    def __str__(self):
        return str(self.text)

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
