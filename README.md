# BBC Radio "What's On" Display for Pimoroni Pico Display Pack 2
![Demo of the code running on the Display Pack 2.0](readme_images/radio_2_demo.gif)

# Introduction

TODO

# Shopping List

You'll need the following to build and run this project... no soldering required!

## Hardware

Most of these links go to the Pimoroni shop in the UK (they also ship worldwide!).

* [Raspberry Pi Pico W](https://shop.pimoroni.com/products/raspberry-pi-pico-w?variant=40059369652307) (I recommend the version with the headers pre-soldered, if you want to do some soldering then pick up a Pico W without headers, get a set of headers and solder them on!)
* [Pimoroni Pico Display Pack 2.0](https://shop.pimoroni.com/products/pico-display-pack-2-0?variant=39374122582099).  A 320 x 240 pixel LCD display for Raspberry Pi Pico, with four buttons and an RGB LED.  This project uses all of these features.
* A [USB to micro USB data cable](https://shop.pimoroni.com/products/usb-a-to-microb-cable-red?variant=32065140746) (to provide power to the project and install code on the Pico W).  I like red cables but any colour and length will do so long as it provides both charging and data.
* A [USB plug](https://www.amazon.co.uk/TECHNOPLAY-Charger-Adapter-1000mAh-Compatible-White/dp/B09HDRYG7J/?th=1) if you want to power the project from a wall socket.  If you have one from a phone that you already own, that'll work fine.

## Software

This stuff's free! (but if you enjoy Thonny, please check out their "Support Ukraine" initiative [here](https://github.com/thonny/thonny/wiki/Support-Ukraine)).

* Pimoroni MicroPython runtime.  You'll want the latest build for the Raspberry Pi Pico W.  This contains the MicroPython runtime plus pre-installed libraries for Pimoroni products that the code depends on.  Download the latest `.uf2` file for the Pi Pico W from GitHub [here](https://github.com/pimoroni/pimoroni-pico/releases) (it will be named something like `pimoroni-picow-vX.XX.X-micropython.uf2`).  
* [Thonny IDE](https://thonny.org/) - a simple code editor that connects to the Raspberry Pi Pico W to install, run and debug code.  Alternative IDEs (for example Visual Studio Code with appropriate extensions) are available - if you're comfortable using one of those with the Raspberry Pi Pico W then go for it!

# Try it!

There's a few steps to complete before you can have this running on your hardware... they're not hard, let's take them one at a time...

## Assemble the Hardware

TODO

## Install Pimoroni MicroPython on the Raspberry Pi Pico W

TODO

## Get the Code

TODO

## Network Configuration

You will need to add your wifi SSID and password to the `secrets.py` file.  Edit `secrets.py` and replace the template content with the correct values for your network:

```python
WIFI_SSID = "Your wifi network name..."
WIFI_PASSWORD = "Your wifi password..."
```

Save your changes.

## Radio Station Configuration

This project displays "what's on" data for four BBC radio stations.  You change the current station displayed on the screen using the four buttons.  These are labelled A, B, X and Y.

The default configuration is as follows:

| Button | Station          |
|--------|------------------|
| A      | Radio 1          |
| B      | Radio 2          |
| X      | Radio 6 Music    |
| Y      | Radio Nottingham |

If you're just trying this out and are happy with these stations, skip the rest of this section.  If you'd like to change them for your own choices read on...

Here are some `id` values for a selection of national and local BBC radio stations.  

| Station                  | `id`                       |
|--------------------------|----------------------------|
| Radio 1                  | `bbc_radio_one`            |
| Radio 2                  | `bbc_radio_two`            |
| Radio 3                  | `bbc_radio_three`          |
| Radio 4                  | `bbc_radio_fourfm`         |
| Radio 5 Live             | `bbc_radio_five_live`      |
| Radio 6 Music            | `bbc_6music`               |
| Radio 1Xtra              | `bbc_1xtra`                |
| Asian Network            | `bbc_asian_network`        |
| World Service            | `bbc_world_service`        |
| Radio Scotland           | `bbc_radio_scotland_fm`    |
| Radio Wales              | `bbc_radio_wales_fm`       |
| Radio Ulster             | `bbc_radio_ulster`         |
| Radio Derby              | `bbc_radio_derby`          |
| Radio Leeds              | `bbc_radio_leeds`          |
| Radio Leicester          | `bbc_radio_leicester`      |
| Radio London             | `bbc_london`               |
| Radio Manchester         | `bbc_radio_manchester`     |
| Radio Merseyside         | `bbc_radio_merseyside`     |
| Radio Newcastle          | `bbc_radio_newcastle`      |
| Radio Nottingham         | `bbc_radio_nottingham`     |
| Radio Sheffield          | `bbc_radio_sheffield`      |
| Radio WM                 | `bbc_wm`                   |
| BBC Three Counties Radio | `bbc_three_counties_radio` |

If you don't see one that you're looking for here, it's easy to figure out the value you need.  Begin [here](https://www.bbc.co.uk/sounds/stations) at the BBC Sounds list of stations.  

Now click on the station that you want to get an ID for.  The value you need is the last part of the URL that your browser takes you to. 

For example if you wanted to add BBC Hereford and Worcester, the ID is `bbc_radio_hereford_worcester` taken from the URL `https://www.bbc.co.uk/sounds/play/live:bbc_radio_hereford_worcester`.

I'll leave the choice of pen colour and character to display for each station up to you.

Once you've chosen the stations that you want to assign to each button, edit `main.py`, changing the values here:

```python
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
```

TODO explain the values in the dictionary above.

Save your changes to `main.py`.

## Copying the Code to the Raspberry Pi Pico W

TODO

## Running the Code

TODO

# How Does it Work?

TODO

# Have Fun!

Hopefully you find this a useful little project and a good demonstration of how to get some data from a JSON endpoint on the internet, display it on the Display Pack 2 and react to button presses on the device.  If you get this running or use it as a start point for your own project I'd love to hear from you.  Reach out to me using one of the methods on my website's [contact me](https://simonprickett.dev/contact/) page.

# Problems?

If you've found a bug or are having trouble getting started, please raise a [GitHub issue](https://github.com/simonprickett/pico-display-pack-2-radio-whats-on/issues) in this repository and I'll try and get back to you.  Have you improved on this project?  Feel free to submit a [pull request](https://github.com/simonprickett/pico-display-pack-2-radio-whats-on/pulls).