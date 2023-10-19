# BBC Radio "What's On" Display for Pimoroni Pico Display Pack 2
![Demo of the code running on the Display Pack 2.0](readme_images/radio_2_demo.gif)

# Introduction

TODO

# Shopping List

You'll need the following to build and run this project... no soldering required!

## Hardware

All links go to the Pimoroni shop in the UK -- they ship worldwide!

* Raspberry Pi Pico W (I recommend the version with the headers pre-soldered, if you want to do some soldering then pick up a Pico W without headers, get a set of headers and solder them on!)
* Pimoroni Pico Display Pack 2.0.  A spacious 320 x 240 pixel LCD display for Raspberry Pi Pico, with four buttons and an RGB LED.  This project uses all of these features.
* A USB to micro USB data cable (to provide power to the project and install code on the Pico W).
* A USB plug if you want to plug the project into a wall socket and power it from there.

## Software

This stuff's free! (but if you enjoy Thonny, please check out their "Support Ukraine" initiative [here](https://github.com/thonny/thonny/wiki/Support-Ukraine)).

* Pimoroni MicroPython latest build for the Raspberry Pi Pico W.  This contains the MicroPython runtime plus pre-installed libraries for Pimoroni products that the code depends on.
* Thonny IDE - a simple code editor that connects to the Raspberry Pi Pico W to install, run and debug code.  Alternative IDEs (for example Visual Studio Code with appropriate extensions) are available - if you're comfortable using one of those with the Raspberry Pi Pico W then go for it!

# Try it!

TODO

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

TODO

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