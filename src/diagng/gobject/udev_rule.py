#!/usr/bin/env python3

from gi.repository import GObject


class UDevRule(GObject.Object):
    rule_file_name = GObject.Property(type=str)
    rule_text = GObject.Property(type=str)
