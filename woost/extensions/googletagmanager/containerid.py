#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
import re
from cocktail.schema import String


class ContainerId(String):

    id_reg_expr = re.compile("(?P<account>GTM-[A-Z0-9]{7})")

    def normalization(self, value):
        if value:
            match = self.id_reg_expr.search(value)
            if match:
                value = match.group("account")
        return value

