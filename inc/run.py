#!/usr/bin/env python
# coding=utf-8

from inc import output,console
import argparse, sys, time, re, binascii, os
import struct

def hexfile(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("hex.txt", "wb+")
    f2.write(binascii.hexlify(content))
    f2.close()
    print(f"[+] 将{filename}文件转换为16进制TXT成功:导出为hex.txt")
    fr = open("hex.txt",'rb').read()
    data1 = str(fr[22:32])[2:12]
    left = str(bytes.fromhex(data1[2:]).decode('utf-8'))
    data2 = str(fr[46:58])[2:14]
    right = str(bytes.fromhex(data2[2:]).decode('utf-8'))
    data3 = str(fr[58:66])[2:10]
    crc32true = int(data3,16)
    print(f"[+] 获取到左边Hex值为:" + left)
    print(f"[+] 获取到右边Hex值为:" + right)
    print(f"[+] 获取到图片CRC值为:0x" + data3)
    return left,right,crc32true

def baopo(left,right,crc32true):
    left = bytes(left, encoding="ascii")
    right = bytes(right, encoding="ascii")
    for i in range(20000):#一般 20000就够
        wide = struct.pack('>i',i)
        for j in range(20000):
            high = struct.pack('>i',j)
            data = left + wide+ high + right

            crc32 = binascii.crc32(data) & 0xffffffff
            if crc32 == crc32true:
                print('\n[+] 图片宽高爆破成功！！！宽为',i,'高为',j,'CRC值为',crc32)
                #print(type(data))
                return i,j
                exit(0)

def writenew(filename,kuan,gao):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("hexnew.txt", "wb+")
    f2.write(binascii.hexlify(content))
    f2.close()
    print(f"[+] 创建信16进制TXT成功:导出为hexnew.txt")
    fr = open("hexnew.txt",'rb').read()
    data1 = str(fr[32:40])[2:10]
    data2 = str(fr[40:48])[2:10]
    print(f"[+] 原本的宽值为:" + data1)
    print(f"[+] 原本的高值为:" + data2)
    kuan = str(kuan).zfill(8)
    gao = str(gao).zfill(8)
    kuan = bytes(kuan, encoding = 'utf-8')
    gao = bytes(gao, encoding = 'utf-8')
    #data1 = bytes(data1, encoding = 'utf-8')
    #data2 = bytes(data2, encoding = 'utf-8')
    new_content = fr[:32] + kuan + fr[40:]
    new_content = new_content[:40] + gao + new_content[48:]
    with open("hexnew.txt", "wb+") as f:
        f.write(new_content)

def unhex():
    with open("hexnew.txt", 'rb') as f:
        content = f.read()
    f2 = open("unhex.bin", "wb+")
    f2.write(binascii.unhexlify(content))
    f2.close()
    print(f"\n[+] 读取十六进制hexnew.txt文件并导出成功:导出为unhex.bin，请自行修改后缀名")
    sys.exit()

def imager(filename):
    left,right,crc32true = hexfile(filename)
    i,j = baopo(left,right,crc32true)
    kuan = str(hex(i)[2:].lower())
    gao = str(hex(j)[2:].lower())
    print('\n[+] 转换为十六进制成功！！！宽为',kuan,'高为',gao)
    writenew(filename,kuan,gao)
    unhex()
    sys.exit()

def reverse(filename):
    kuan = int(input("请输入需要更改的宽\nUrl >>> "))
    gao = int(input("请输入需要更改的高\nUrl >>> "))
    kuan = str(hex(kuan)[2:].lower())
    gao = str(hex(gao)[2:].lower())
    print('\n[+] 转换为十六进制成功！！！宽为',kuan,'高为',gao)
    writenew(filename,kuan,gao)
    unhex()
    sys.exit()
