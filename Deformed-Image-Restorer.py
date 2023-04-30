#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, console, run
import re, binascii, argparse, sys, time

def get_parser():
    parser = argparse.ArgumentParser(usage='python3 Deformed-Image-Restorer.py',description='Deformed-Image-Restorer: 自动爆破图片宽高并一键修复工具',)
    p = parser.add_argument_group('FileReverse-Tools 的参数')
    p.add_argument("-i", "--imager", type=str, help="自动爆破图片宽高并修复图片")
    p.add_argument("-r", "--reverse", type=str, help="使用指定宽高修复导出图片")
    args = parser.parse_args()
    return args

def main():
    output.logo()
    args = get_parser()
    console.Image_Restorer_console(args)

if __name__ == '__main__':
    main()
