from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    messages = models.TextField(verbose_name=_('messages'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
