import badge
import ugfx
import network

def show(text):
	ugfx.clear()
	ugfx.string(10, 10, text, 'Roboto_Regular18', ugfx.BLACK)
	ugfx.flush()

# from https://radius.sha2017.org/probe/bssid_list
locations = {
	'34:FC:B9:19:69:51': 'workshop-tau_AP277',
	# TODO
}

#nickname = badge.nvs_get_str("owner", "name", "noname")

wlan = network.WLAN(network.STA_IF)
wlan.active("up")
scan_results = wlan.scan()
# Each result is a tuple: (ssid, bssid, channel, RSSI, authmode, hidden)

strongest_ap = max(scan_results, key=lambda ap: ap[3])
bssid = strongest_ap[1]
ssid = strongest_ap[0]
macaddress = ":".join(list(map(lambda x: hex(ord(x))[2:], s))) # FIXME
location = locations.get(bssid)

if location:
	show(location)
else:
	#show('no idea!') 
	show(macaddress)

# networking docs:
# https://github.com/micropython/micropython-esp32/blob/046d15f074398cc2968fc66ae2fd25dc31100109/docs/library/network.rst
# https://github.com/micropython/micropython-esp32/blob/ec9c2778867fbb4d0ef1ebf5ace6433b01589d05/docs/esp8266/tutorial/network_basics.rst
