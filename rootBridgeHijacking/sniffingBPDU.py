from scapy.all import sniff

def handle_pkt(pkt):
    if pkt.haslayer("LLC") and pkt["LLC"].dsap == 0x42:
        print("Captured BPDU:")
        pkt.show()   # display full frame

sniff(iface="Ethernet 2", filter="ether dst 01:80:C2:00:00:00", prn=handle_pkt)