import network

SSID = 'USP_OFFICE_B'
PASSWORD = 'uspuspusp1234'

wlan_if = network.WLAN(network.STA_IF)
wlan_if.active(True)
wlan_if.connect(SSID, PASSWORD)
