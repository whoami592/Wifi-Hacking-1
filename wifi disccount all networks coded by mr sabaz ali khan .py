import wmi

# Initialize the WMI object
wmi_obj = wmi.WMI()

# Get a list of all network adapters
network_adapters = wmi_obj.Win32_NetworkAdapter(NetConnectionStatus=2)  # 2 means connected

# Iterate over the list of network adapters
for adapter in network_adapters:
    # Disconnect the network adapter
    adapter.Disable()

print("All WiFi networks have been disconnected.")