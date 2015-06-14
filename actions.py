#!/usr/bin/python


from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--enable-pinentry-gtk2")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    
