#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#   LightDM GTK Greeter Settings
#   Copyright (C) 2014 Andrew P. <pan.pav.7c5@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License version 3, as published
#   by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranties of
#   MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.


def main():
    from gi.repository import Gtk
    from lightdm_gtk_greeter_settings import helpers
    from lightdm_gtk_greeter_settings import GtkGreeterSettingsWindow
    from lightdm_gtk_greeter_settings.GtkGreeterSettingsWindow import WindowMode

    import argparse
    import locale
    locale.textdomain('lightdm-gtk-greeter-settings')

    parser = argparse.ArgumentParser(description='LightDM Gtk+ Greeter settings editor')
    parser.add_argument('-s', '--socket-id', action='store', help='Settings manager socket')
    parser.add_argument('--use-gtk-header', action='store_const', const=True,
                        help='Use GtkHeaderBar')
    args = parser.parse_args()

    try:
        socket_id = int(args.socket_id or '')
    except ValueError:
        socket_id = None

    if socket_id:
        window = GtkGreeterSettingsWindow.GtkGreeterSettingsWindow(WindowMode.Embedded)
        plug = Gtk.Plug.new(socket_id)
        plug.connect('delete-event', Gtk.main_quit)
        plug.show()
        content = window.builder.get_object('content_box')
        content.reparent(plug)
        Gtk.main()
    else:
        if args.use_gtk_header:
            window = GtkGreeterSettingsWindow.GtkGreeterSettingsWindow(mode=WindowMode.GtkHeader)
        else:
            window = GtkGreeterSettingsWindow.GtkGreeterSettingsWindow()
        window.show()
        Gtk.main()


if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    main()
