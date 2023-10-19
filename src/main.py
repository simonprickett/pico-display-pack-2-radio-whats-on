import gc
import network
import secrets
import time
import urequests

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
from pimoroni import Button, RGBLED

# Initialize the LED and create a display object for pico graphics.
led = RGBLED(6, 7, 8)
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB332, rotate=0)

SPINNER_CHARS = [ "\\", "|", "/", "-" ]

# How often to refresh the data (seconds).
REFRESH_INTERVAL = 30

# Which radio station to show at startup (from STATION_MAP)
DEFAULT_STATION = "b"

# Details required for the four stations to associate with
# the A, B, X, Y buttons on the device.
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

current_station = DEFAULT_STATION

# Clear the screen.
def clear_screen():
    display.set_pen(BLACK_PEN)
    display.clear()

# Retrieve current / last played song information for a given BBC radio station.
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

# Attempt to connect to the network (config in secrets.py).
led.set_rgb(128, 0, 0) 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

n = 0
led.set_rgb(61, 21, 15)

while not wlan.isconnected() and wlan.status() >= 0:
    clear_screen()
    display.set_pen(WHITE_PEN)
    display.text(f"CONNECTING {SPINNER_CHARS[n]}", 1, 115, scale = 5)
    display.update()
    
    n = n + 1 if n < len(SPINNER_CHARS) - 1 else 0
    time.sleep(0.2)

clear_screen()
display.set_pen(WHITE_PEN)

# Display the current WIFI status.
if wlan.status() == network.STAT_GOT_IP:
    display.text(f"CONNECTED: UPDATING", 3, 115, scale = 3)
elif wlan.status() == network.STAT_WRONG_PASSWORD:
    display.text("BAD WIFI PASSWORD", 20, 115, scale =  3)
elif wlan.status() == network.STAT_NO_AP_FOUND:
    display.text("BAD WIFI SSID", 60, 115, scale =  3)
else:
    display.text("UNKNOWN WIFI ERROR", 15, 115, scale =  3)

display.update()

if (wlan.status() != network.STAT_GOT_IP):
    # Set the LED to red and go no further.
    led.set_rgb(32, 0, 0)
    
    while True:
        time.sleep(1)

# Got wifi, so perform initial data load from BBC API.
last_updated = time.ticks_ms()
led.set_rgb(61, 21, 15)
status, artist, song = get_song_data(STATION_MAP[current_station]["id"])
led.set_rgb(0, 32, 0)

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

show_artist = True
last_refreshed = time.ticks_ms()

while True:
    ticks_now = time.ticks_ms()
    
    if time.ticks_diff(ticks_now, last_refreshed) > 3000:
        # Update the display with the current information.
        clear_screen()
        
        h_offset = 0

        # Draw the coloured circle for the station identity background, with
        # an outline if needed (e.g. when the station's colour is indistinguishable
        # from the black background).
        if "outline" in STATION_MAP[current_station]:
            display.set_pen(STATION_MAP[current_station]["outline"])
            display.circle(245, 85, 62)
            h_offset = 2
            
        display.set_pen(STATION_MAP[current_station]["pen"])
        display.circle(245, 85, 60)
        display.set_pen(WHITE_PEN)
        display.set_font("bitmap8")
        display.text(STATION_MAP[current_station]["display"], 228 + h_offset, 50, scale = 10)    

        display.set_font("bitmap6")
        
        # Alternate between showing the artist name and song title.
        if show_artist:
            text = artist
        else:
            text = song
        
        display.text(text, 10, 180, 300, scale = 3)
        display.text(status, 10, 60, 200, scale = 4)
    
        show_artist = not show_artist
    
        display.update()
        last_refreshed = time.ticks_ms()

    # Check if any of the buttons were pressed and change station if so.
    # Reset the last updated time to force an immediate update.
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
            
    # Periodic update - get fresh information from the BBC.
    if time.ticks_diff(ticks_now, last_updated) > REFRESH_INTERVAL * 1000:
        # Clear the part of the screen that shows the artist/song information.
        display.set_pen(BLACK_PEN)
        display.rectangle(0, 160, 320, 240)
        display.update()
        
        display.set_pen(WHITE_PEN)
        display.text("Updating...", 10, 180, 300, scale = 3)
        display.update()
        led.set_rgb(61, 21, 15)   
        status, artist, song = get_song_data(STATION_MAP[current_station]["id"])

        last_updated = time.ticks_ms()
        led.set_rgb(0, 32, 0)
    
    # Sleep a little to avoid a tight loop.
    time.sleep(0.1)
