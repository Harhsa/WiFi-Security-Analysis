from scapy.all import *
packet = RadioTap()/Dot11(type=0, subtype=8)/Dot11Beacon()
wrpcap("wifi_test.pcap", packet)
print("Test packet created!")
