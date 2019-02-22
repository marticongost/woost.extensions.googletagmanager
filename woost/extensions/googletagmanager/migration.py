#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.persistence import migration_step

@migration_step
def import_old_settings(e):

    from woost.models import Configuration, Website

    for obj in (list(Configuration.select()) + list(Website.select())):
        try:
            value = obj._google_tag_manager_account
        except AttributeError:
            pass
        else:
            del obj._google_tag_manager_account
            obj.x_googletagmananager_container = value

