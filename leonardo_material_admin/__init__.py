
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_material_admin.Config'

LEONARDO_ORDERING = 100

LEONARDO_APPS = [
    'material',
    'material.admin',
    'leonardo_admin',
]


class Config(AppConfig):
    name = 'leonardo_material_admin'
    verbose_name = _("Admin Material Theme")
