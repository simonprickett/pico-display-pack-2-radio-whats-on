import gc
import network
import secrets
import time
import urequests

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

print(gc.mem_free())

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)

BLACK_PEN = display.create_pen(0, 0, 0)
ORANGE_PEN = display.create_pen(250, 100, 0)
WHITE_PEN = display.create_pen(255, 255, 255)

display.set_pen(BLACK_PEN)
display.clear()

# TODO some sort of loading message...
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while not wlan.isconnected() and wlan.status() >= 0:
    print("connecting")
    time.sleep(0.2)

show_artist = True

display = None
gc.collect()

now_playing = urequests.get("https://rms.api.bbc.co.uk/v2/services/bbc_radio_two/segments/latest?experience=domestic&offset=0&limit=1", headers= {"User-Agent": "PicoW"}).json()
status = now_playing["data"][0]["offset"]["label"]
artist = now_playing["data"][0]["titles"]["primary"]
song = now_playing["data"][0]["titles"]["secondary"]
# TODO Sanitize to be A-Z 0-9 and replace anything else with a space.
now_playing = None
gc.collect()

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)

while True:
    display.set_pen(ORANGE_PEN)
    display.circle(245, 85, 60)
    display.set_pen(WHITE_PEN)
    display.set_font("bitmap8")
    display.text("2", 228, 50, scale = 10)    

    display.update()
    display.set_font("bitmap6")
        
    if show_artist:
        text = artist
    else:
        text = song
        
    display.text(text, 10, 180, 300, scale = 3)
    display.text(status, 10, 60, 200, scale = 4)
        
    show_artist = not show_artist
    display.update()
    
    time.sleep(3)
    
    display.set_pen(BLACK_PEN)
    display.rectangle(0, 160, 320, 240)
    display.update()
