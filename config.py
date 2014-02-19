# -*- coding: utf-8 -*-
from livesettings import config_register, ConfigurationGroup, PositiveIntegerValue, PercentValue, StringValue
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
MYAPP_GROUP = ConfigurationGroup(
    'MyApp',               # key: internal name of the group to be created
    u'Настройки сайта',  # name: verbose name which can be automatically translated
    ordering=0             # ordering: order of group in the list (default is 1)
    )



config_register(StringValue(
                            MYAPP_GROUP,
        'EMAIL', 
        description = u'Email администратора',
        help_text = u"Почта, куда будут приходить заявки.",
        default = 'annkpx@gmail.com'
    ))


config_register(StringValue(
                            MYAPP_GROUP,
        'field_1', 
        description = u'доставлен груз до пункта назначения',
        default = '236'
    ))

config_register(StringValue(
                            MYAPP_GROUP,
        'field_2', 
        description = u'довольных клиентов',
        default = '569'
    ))

config_register(StringValue(
                            MYAPP_GROUP,
        'field_3', 
        description = u'звонка в день',
        default = '52'
    ))

config_register(StringValue(
                            MYAPP_GROUP,
        'field_4', 
        description = u'процента закупок за рубежом',
        default = '2,53'
    ))