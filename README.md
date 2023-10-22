# BBC Radio "What's On" Display for Pimoroni Pico Display Pack 2

![Demo of the code running on the Display Pack 2.0](readme_images/radio_2_demo.gif)

# Introduction

This is a small scale project that I made to solve a problem I had with our Amazon Echo Show device.

When using the [BBC Sounds skill](https://www.bbc.co.uk/sounds/help/questions/listening-on-a-smart-speaker/alexa) to play various BBC Radio stations I noticed that the current song and artist information isn't displayed.  The BBC has the data for this as it appears on the [web version of BBC Sounds](https://www.bbc.co.uk/sounds).

I decided to see how the website works, found the JSON feed with the information I needed and made my own companion display for the Echo Show...

![Solving a problem with the Amazon Echo Show device](readme_images/pico_display_pack_2_with_echo_show.png)

If you're reading this and you're responsible for the BBC Sounds skill on Alexa I'd love to hear why you don't show this basic information (feel free to [get in touch](https://simonprickett.dev/contact/))... other skills can do it... here's Absolute Radio for example:

![Absolute Radio can show artist and song information](readme_images/absolute_radio.jpg)

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

If you bought a Pi Pico W with the headers pre-soldered, then attaching the Display Pack is simply a matter of aligning the male headers on the Pico with the corresponding female ones on the Display pack and pushing the two together.

Pimoroni even print an image of the Pico on the underside of the Display Pack for you so that it's easy to see how to orient the Pico so that the micro USB port is at the right end of the Display Pack...

![Assembling the hardware](readme_images/assembly.png)

If you bought a Pico W without pre-soldered headers, you'll need to solder the headers on first.  If you need help with this I recommend watching [this video](https://www.youtube.com/watch?v=R11QanPDccs) on the "Learn Embedded Systems" channel on YouTube.

## Install Pimoroni MicroPython on the Raspberry Pi Pico W

The Raspberry Pi Pico W doesn't come with a MicroPython runtime installed by default.  Earlier, you downloaded the latest version of the Pi Pico W MicroPython image from Pimoroni.  You'll sometimes see this referred to as "Pirate Brand MicroPython".

We're using Pimoroni's distribution as it contains drivers for many of their products including the Display Pack 2 that we need for this project.

Install the MicroPython runtime by:

1. Holding down the BOOTSEL button on the back of the Pi Pico W whilst connecting it to your machine using the USB->Micro USB cable.
1. Dragging and dropping the `.uf2` file that you downloaded onto the removable drive named "RPI-RP2" that appears on your machine.
1. When the file copy has finished, the removable drive "RPI-RP2" should disappear, and you've now got a Pi Pico W running MicroPython.

If you get stuck or need a more detailed description of how to do this, check out Pimoroni's guide [here](https://learn.pimoroni.com/article/getting-started-with-pico#installing-the-custom-firmware).

## Get the Code

Grab a copy of the code by cloning it or downloading a zip of it from the GitHub repository ([here](https://github.com/simonprickett/pico-display-pack-2-radio-whats-on)).

If you have the `git` command line tools installed, clone the repository like this:

```
git clone https://github.com/simonprickett/pico-display-pack-2-radio-whats-on.git
```

This creates a folder named `pico-display-pack-2-radio-whats-on` wherever you ran the git clone command.  If you chose to download a zip file from GitHub insteead, unzip the file and you'll get the same folder.

Use Thonny or your own choice of IDE to open this folder.  

The next step is to configure the code to connect to your WiFi network.

## Network Configuration

You will need to add your WiFi SSID (network name) and password to the `secrets.py` file.  Edit `secrets.py` and replace the template content with the correct values for your network:

```python
WIFI_SSID = "Your wifi network name..."
WIFI_PASSWORD = "Your wifi password..."
```

Save your changes.

## Optional: Radio Station Configuration

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

The above is a Python dictionary which has top level keys "a", "b", "x", "y" - these are used to configure each button on the display.  Each button's key contains another dictionary that has keys as follows:

* `id` (required): The ID of the Radio station to get data for. 
* `display` (required): A single character to display as the station's logo (it will go in the centre of a circle on the display).  This will be rendered in white.
* `pen` (required): A [Pimoroni Pico Graphics](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/picographics) pen used to draw and colour in the circular area on the screen.  Change the three numeric values (R, G, B) to represent the colour of your choice.  Here's an [RGB colour picker](https://www.rapidtables.com/web/color/RGB_Color.html) you can use.  In the example data, I've set the colours to match those used by the BBC for the respective radio stations.
* `outline` (optional): Another Pico Graphics pen.  This is optional and only needed when the colour you choose for `pen` can't easily be distinguished from the black background on the display.  If this value is present, the code will use this pen to draw an outline around the circle.  In the sample data set this is needed for Radio 1 as their brand colour is back.

If you chose to change the button configurations, save your changes to `main.py`.

## Copying the Code to the Raspberry Pi Pico W

TODO

## Running the Code

TODO

# How Does it Work?

TODO - information on the JSON feed, working with PicoGraphics, could I show the presenter info and the current song image etc.  

# Have Fun!

Hopefully you find this a useful little project and a good demonstration of how to get some data from a JSON endpoint on the internet, display it on the Display Pack 2 and react to button presses on the device.  If you get this running or use it as a start point for your own project I'd love to hear from you.  Reach out to me using one of the methods on my website's [contact me](https://simonprickett.dev/contact/) page.

# Problems?

If you've found a bug or are having trouble getting started, please raise a [GitHub issue](https://github.com/simonprickett/pico-display-pack-2-radio-whats-on/issues) in this repository and I'll try and get back to you.  Have you improved on this project?  Feel free to submit a [pull request](https://github.com/simonprickett/pico-display-pack-2-radio-whats-on/pulls).