# -*- coding: utf-8 -*-
# @Author: Lorenzo
# @Date:   2018-04-04 16:22:43
# @Last Modified by:   Lorenzo
# @Last Modified time: 2018-04-17 09:35:10

"""
.. module:: diabloserial

*******************************************
4DSystems Diablo16 Serial Interface Library
*******************************************

    """

# 8.3 format for file names!

@native_c('difc_diablodemo',['csrc/*'])
def diablodemo():
    pass

@native_c('difc_openComm', ['csrc/*'])
def openComm(serdrv, serbaud):
    pass

@native_c('difc_media_Init', ['csrc/*'])
def media_Init():
    pass

@native_c('difc_file_Mount', ['csrc/*'])
def file_Mount():
    pass

@native_c('difc_file_Open', ['csrc/*'])
def file_Open(filename, mode):
    pass

@native_c('difc_file_LoadImageControl', ['csrc/*'])
def file_LoadImageControl(datfile, gcifile, mode):
    pass

@native_c('difc_img_Show', ['csrc/*'])
def img_Show(image_handle, index):
    pass

@native_c('difc_img_Enable', ['csrc/*'])
def img_Enable(image_handle, index):
    pass

@native_c('difc_img_Disable', ['csrc/*'])
def img_Disable(image_handle, index):
    pass

@native_c('difc_gfx_Cls', ['csrc/*'])
def gfx_Cls():
    pass


gfx = None
file = None
def init(serdrv, serbaud):
    """
.. function:: init(serdrv, serbaud)

    :param serdrv: serial interface the chip is connected to (e.g., SERIAL0, SERIAL1, ...)
    :param serbaud: serial communication baud

    Initialize serial communication with Diablo16 chip.
    This function also instantiates the following module objects:

        *:samp:`gfx`
        *:samp:`file`

    """
    global gfx, file
    openComm(serdrv, serbaud)
    gfx = GFX()
    file = File()


def _load_image_control(*args):
    if len(args) == 2:
        datfile = args[0] + '.dat'
        gcifile = args[0] + '.gci'
        mode = args[1]
    else:
        datfile = args[0]
        gcifile = args[1]
        mode = args[2]
    return image(file_LoadImageControl(datfile, gcifile, mode))

class File:
    """
=================
File class
=================

.. class:: File()   

    
    """
    def __init__(self):
        pass

    def mount(self):
        return file_Mount()

    def load_image_control(self, *args):
        """
.. method:: load_image_control(*args)

        This method can be called passing:

            * tuples with two or three elements (see next point)
            * two strings for dat and gci filenames and an integer for load mode or a single string for a common dat and gci filenames prefix and an integer for the mode

        Example::

            img1, img2 = fourserial.file.load_image_control(("img1",1), ("img2",1))
            img1, img2 = fourserial.file.load_image_control(("img1.dat", "img1.gci",1), ("img2.dat", "img2.gci",1))
            img1 = fourserial.file.load_image_control("img1",1)
            img1 = fourserial.file.load_image_control("img1.dat", "img1.gci", 1)

        """
        if len(args) > 1 and type(args[0]) == PTUPLE or type(args[0]) == PLIST:
            res = [None]*len(args)
            for i, dat_gci_mode in enumerate(args):
                res[i] = _load_image_control(*dat_gci_mode)
            return res
        elif len(args) == 2 or len(args) == 3:
            return _load_image_control(*args)
        raise TypeError

class image:

    def __init__(self, handle):
        self.handle = handle

    def enable(self, index):
        return img_Enable(self.handle, index)

    def disable(self, index):
        return img_Disable(self.handle, index)

    def show(self, index):
        return img_Show(self.handle, index)

class GFX:

    def __init__(self):
        pass

    def cls(self):
        gfx_Cls()