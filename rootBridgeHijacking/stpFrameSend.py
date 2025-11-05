from scapy.all import *
from scapy.contrib.lldp import LLDPDU
from scapy.layers.l2 import Ether

bpdu = (
    b"\x00\x00"      # Protocol ID
    b"\x00"          # Version
    b"\x00"          # BPDU Type (Config BPDU)
    b"\x01"          # Flags
    b"\x80\x00\x00\x00\x00\x00\x00\x01"  # Root ID
    b"\x00\x00\x00\x10"                  # Root Path Cost
    b"\x80\x00\x00\x00\x00\x00\x00\x02"  # Bridge ID
    b"\x80\x01"      # Port ID
    b"\x00\x01"      # Message Age
    b"\x00\x14"      # Max Age
    b"\x00\x02"      # Hello Time
    b"\x00\x15"      # Forward Delay
)

frame = (
    Ether(dst="01:80:C2:00:00:00", src="02:00:00:00:00:01") /
    LLDPDU(dsap=0x42, ssap=0x42, ctrl=0x03) /
    Raw(load=bpdu)
)

# Send continuously like a real switch does (every 2s)
sendp(frame, iface="eth0", loop=1, inter=2)