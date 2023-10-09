import gc
import network
import secrets # TODO rename to config or something
import time
import urequests

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
from pimoroni import Button, RGBLED

def create_display():
    return PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB332, rotate=0)

def get_song_data(radio_station):
    now_playing = urequests.get(f"https://rms.api.bbc.co.uk/v2/services/{radio_station}/segments/latest?experience=domestic&offset=0&limit=1", headers= {"User-Agent": "PicoW"}).json()
    if len(now_playing["data"]) > 0:
        status = now_playing["data"][0]["offset"]["label"]
        artist = now_playing["data"][0]["titles"]["primary"]
        song = now_playing["data"][0]["titles"]["secondary"]
    else:
        status = "NO DATA"
        artist = "NO DATA"
        song = "NO DATA"
        
    # TODO sanitize special characters out of these values...
    return status, artist, song

led = RGBLED(6, 7, 8)
display = create_display()

# TODO move this out into config...
STATION_MAP = {
    "a": {
        "id": "bbc_radio_one",
        "display": "1",
        "pen": display.create_pen(0, 0, 0),
        "outline": display.create_pen(128, 128, 128)
    },
    "b": {
        "id": "bbc_radio_two",
        "display": "2",
        "pen": display.create_pen(250, 100, 0)
    },
    "x": {
        "id": "bbc_6music",
        "display": "6",
        "pen": display.create_pen(1, 95, 13)
    },
    "y": {
        "id": "bbc_radio_nottingham",
        "display": "N",
        "pen": display.create_pen(32, 14, 51)
    }
}

BLACK_PEN = display.create_pen(0, 0, 0)
WHITE_PEN = display.create_pen(255, 255, 255)

display.set_pen(BLACK_PEN)
display.clear()

current_station = secrets.DEFAULT_STATION

# TODO some sort of loading message...
led.set_rgb(128, 0, 0) 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while not wlan.isconnected() and wlan.status() >= 0:
    led.set_rgb(61, 21, 15) 
    time.sleep(0.2)

led.set_rgb(0, 32, 0)

display = None
gc.collect()

last_updated = time.ticks_ms()
led.set_rgb(61, 21, 15)  
status, artist, song = get_song_data(STATION_MAP[current_station]["id"])
led.set_rgb(0, 32, 0)
gc.collect()
display = create_display()

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

show_artist = True
last_refreshed = time.ticks_ms()

while True:
    gc.collect()
    
    ticks_now = time.ticks_ms()
    
    if time.ticks_diff(ticks_now, last_refreshed) > 3000:
        display.set_pen(BLACK_PEN)
        display.rectangle(0, 160, 320, 240)
        display.update()
        
        h_offset = 0

        if "outline" in STATION_MAP[current_station]:
            display.set_pen(STATION_MAP[current_station]["outline"])
            display.circle(245, 85, 62)
            h_offset = 2
            
        display.set_pen(STATION_MAP[current_station]["pen"])
        display.circle(245, 85, 60)
        display.set_pen(WHITE_PEN)
        display.set_font("bitmap8")
        display.text(STATION_MAP[current_station]["display"], 228 + h_offset, 50, scale = 10)    

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
        last_refreshed = time.ticks_ms()
    
    if button_a.read():
        current_station = "a"
        last_updated = 0
    elif button_b.read():
        current_station = "b"
        last_updated = 0
    elif button_x.read():
        current_station = "x"
        last_updated = 0
    elif button_y.read():
        current_station = "y"
        last_updated = 0
            
    if time.ticks_diff(ticks_now, last_updated) > secrets.REFRESH_INTERVAL * 1000:
        display.set_pen(BLACK_PEN)
        display.rectangle(0, 160, 320, 240)
        display.update()
        
        display.set_pen(WHITE_PEN)
        display.text("Updating...", 10, 180, 300, scale = 3)
        display.update()
        led.set_rgb(61, 21, 15)   
        display = None
        gc.collect()
        status, artist, song = get_song_data(STATION_MAP[current_station]["id"])
        gc.collect()    
        display = create_display()
        last_updated = time.ticks_ms()
        led.set_rgb(0, 32, 0)
    
    time.sleep(0.1)

