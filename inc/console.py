#!/usr/bin/env python
# coding=utf-8

from inc import output,run
import sys

# 控制台-参数处理和程序调用
def Image_Restorer_console(args):
    if args.imager:
        run.imager(args.imager)
    if args.reverse:
        run.reverse(args.reverse)
    else:
        output.usage()
        sys.exit()
