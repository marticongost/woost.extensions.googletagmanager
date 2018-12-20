#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from woost.controllers.cmscontroller import CMSController
from woost.models import get_setting

@when(CMSController.producing_output)
def handle_producing_output(e):
    html = e.output.get("body_beginning_html", "")
    if html:
        html += " "
    html += get_markup()
    e.output["body_beginning_html"] = html

def get_markup():

    container_id = get_setting("x_googletagmananager_container")

    if not container_id:
        return ""
    else:
        return """
            <!-- Google Tag Manager -->
            <noscript><iframe src="//www.googletagmanager.com/ns.html?id=%(container_id)s"
            height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
            <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
            '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','%(container_id)s');</script>
            <!-- End Google Tag Manager -->
            """ % {"container_id": container_id}

