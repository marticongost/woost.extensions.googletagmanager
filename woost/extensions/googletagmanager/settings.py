#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.translations import translations
from woost.models import add_setting
from .containerid import ContainerId

translations.load_bundle("woost.extensions.googletagmanager.settings")

add_setting(
    ContainerId(
        "x_googletagmananager_container",
        text_search = False,
    )
)

