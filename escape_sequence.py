#!/usr/bin/env python
# -*- coding: utf-8 -*-

def em(text):
    return '\033[%dm%s\033[%dm' % (1,text,0)

def under_line(text):
    return '\033[%dm%s\033[%dm' % (4,text,0)


def __change_forward_color(text,color_no):
    return '\033[%dm%s\033[%dm' % (color_no,text,39)

def black(text):
    return __change_forward_color(text,30)

def red(text):
    return __change_forward_color(text,31)

def green(text):
    return __change_forward_color(text,32)

def yellow(text):
    return __change_forward_color(text,33)

def blue(text):
    return __change_forward_color(text,34)

def magenta(text):
    return __change_forward_color(text,35)

def cyan(text):
    return __change_forward_color(text,36)

def white(text):
    return __change_forward_color(text,37)


def __change_back_color(text,color_no):
    return '\033[%dm%s\033[%dm' % (color_no,text,49)

def back_red(text):
    return __change_back_color(text,41)

def back_green(text):
    return __change_back_color(text,42)

def back_yellow(text):
    return __change_back_color(text,43)

def back_blue(text):
    return __change_back_color(text,44)

def back_magenta(text):
    return __change_back_color(text,45)

def back_cyan(text):
    return __change_back_color(text,46)

def back_white(text):
    return __change_back_color(text,47)


if __name__ == '__main__':
    print('Test : ')
    out1 = red('Red')+green('Green')+yellow('Yellow')+ \
          blue('Blue')+magenta('Magenta')+cyan('Cyan')+white('White')
    out2 = back_red('Red')+back_green('Green')+back_yellow('Yellow')+ \
          back_blue('Blue')+back_magenta('Magenta')+back_cyan('Cyan')+back_white('White')

    print(out1)
    print(out2)
    print(em('Emphasize'))
    print(under_line('UnderLine'))
