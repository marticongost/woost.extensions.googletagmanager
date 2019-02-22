#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from cocktail.translations import translations
from woost.admin.sections.settings import Settings
from woost.admin.sections.contentsection import ContentSection

translations.load_bundle("woost.extensions.googletagmanager.admin.sections")


class GoogleTagManagerSettings(Settings):
    icon_uri = (
        "woost.extensions.googletagmanager.admin.ui://"
        "images/sections/google-tag-manager.svg"
    )
    members = [
        "x_googletagmananager_container"
    ]


@when(ContentSection.declared)
def fill(e):
    e.source.append(GoogleTagManagerSettings("google-tag-manager"))

