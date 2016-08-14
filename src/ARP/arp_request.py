#!/usr/bin/env python3
from scapy.all import *

ip = '192.168.11.2'
mac = 'ff:ff:ff:ff:ff:ff'
dummy_mac = 'ff:ff:ff:ff:ff:ee'

ans,unans = srp(Ether(dst=mac)/ARP(pdst=ip),timeout=2)
#普通のマシンはmacアドレスを返す。
dans,dunans = srp(Ether(dst=dummy_mac)/ARP(pdst=ip),timeout=2)
#普通のマシンは何も返さないが,プロミスキャスモードを使っているマシンはmacアドレスを返す。

print ans,dans
