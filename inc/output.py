#!/usr/bin/env python
# coding=utf-8

import random, time, os, sys

def logo():
    logo0 = r'''
                   ____       ____                              __               
                  / __ \___  / __/___  _________ ___  ___  ____/ /               
                 / / / / _ \/ /_/ __ \/ ___/ __ `__ \/ _ \/ __  /                
                / /_/ /  __/ __/ /_/ / /  / / / / / /  __/ /_/ /                 
    ____       /_____/\___/_/  \____/_/  /_/_/_/ /_/\___/\__,_/                  
   /  _/___ ___  ____ _____ ____        / __ \___  _____/ /_____  ________  _____
   / // __ `__ \/ __ `/ __ `/ _ \______/ /_/ / _ \/ ___/ __/ __ \/ ___/ _ \/ ___/
 _/ // / / / / / /_/ / /_/ /  __/_____/ _, _/  __(__  ) /_/ /_/ / /  /  __/ /    
/___/_/ /_/ /_/\__,_/\__, /\___/     /_/ |_|\___/____/\__/\____/_/   \___/_/     
                    /____/                                                       
                                Version: 1.02                                    
                          Author:  曾哥（@AabyssZG）                             
                     Whoami:  https://github.com/AabyssZG                        

'''
    print(logo0)

def usage():
    print('''
用法:
        自动爆破图片宽高并修复PNG图片:   python3 Deformed-Image-Restorer.py -i demo.png
        使用指定宽高修复导出PNG图片:     python3 Deformed-Image-Restorer.py -r demo.png

参数:
        -i  --image    自动爆破图片宽高并导出修复后的PNG图片
        -r  --reverse  使用指定宽高导出修复后的PNG图片
        ''', end='')
