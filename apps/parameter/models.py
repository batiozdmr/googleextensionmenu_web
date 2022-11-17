from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel

from ..common.mixins.audit import AuditMixin
from ..common.oneTextField import OneTextField
from ..common.seo.seo import SeoModel


class SiteSettings(AuditMixin, SeoModel):
    site = models.OneToOneField(Site, related_name="settings", on_delete=models.CASCADE, verbose_name='Site')

    text = models.CharField(max_length=400, verbose_name=_('Firma Adı'), blank=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# color
class Colors(OneTextField):
    class Meta:
        ordering = ('text',)
        verbose_name = _('Renkler')
        verbose_name_plural = _('Renkler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Icon(OneTextField):

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'İcon'
        verbose_name_plural = 'İcon'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
