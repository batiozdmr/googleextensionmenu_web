from decimal import Decimal

from django.contrib.auth.models import AbstractUser, User, Group
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.fileUpload.userPath import userDirectoryPath
from apps.common.oneTextField import OneTextField
from apps.parameter.models import Colors, Icon


def size_format(b):
    if b < 1000:
        return '%i' % b + ' B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b / 1000) + ' KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b / 1000000) + ' MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b / 1000000000) + ' GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b / 1000000000000) + ' TB'


class TopFileTypes(OneTextField):
    color = models.ForeignKey(Colors, related_name='top_files_types_color', blank=True, on_delete=models.CASCADE,
                              null=True, verbose_name=_('Renk'))
    icon = models.ForeignKey(Icon, related_name='top_files_types_icon', blank=True, on_delete=models.CASCADE,
                             null=True, verbose_name=_('İcon'))

    def __str__(self):
        return str(self.text)

    def size_count(self):
        count = 0
        type = FileTypes.objects.filter(type=self)
        for item in type:
            files = Files.objects.filter(type=item)
            for file_item in files:
                count = Decimal(count) + Decimal(file_item.kb_size)
        count = size_format(count)
        return count

    class Meta:
        verbose_name = _('Üst Dosya Tipi')
        verbose_name_plural = _('Üst Dosya Tipi')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class FileTypes(OneTextField):
    type = models.ForeignKey(TopFileTypes, related_name='files_type_type', blank=True, on_delete=models.CASCADE,
                             null=True, verbose_name=_('Üst Dosya Tipi'))

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = _('Dosya Tipi')
        verbose_name_plural = _('Dosya Tipi')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Files(OneTextField):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name="files_user",
                             verbose_name=_('Kullanıcı'))
    slug = models.SlugField(unique=True, max_length=255, null=True, editable=False, verbose_name=_('Slug'))
    file = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('Dosya'))
    type = models.ForeignKey(FileTypes, related_name='files_type', blank=True, on_delete=models.CASCADE,
                             null=True, verbose_name=_('Dosya Tipi'))
    size = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Boyut'))
    kb_size = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('KB Boyut'))

    def __str__(self):
        return str(self.text)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:250])

        super(Files, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Dosyalar'
        verbose_name_plural = 'Dosyalar'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
