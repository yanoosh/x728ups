# X728 UPS Service

This project replaces much of the standard Geekworm software provided for the X728 UPS, which is a small UPS for the Raspberry Pi.

I wrote this because I found the original software unreliable and difficult to configure. It also didn't provide a
satisfactory mechanism for shutting down the Raspberry Pi in the event of an extended power outage.

This service runs as a systemd unit and manages both shutdown requests from the UPS itself, as well as monitoring PLD
and battery voltage to ensure the RPi shuts down in a timely manner should an extended power outage occur.

This software requires I2C to be enabled on the Raspberry Pi (part of the standard software installation process).

## Lack of Any Kind of Warranty

I share this purely out of the goodness of my own heart and I don't support or endorse it in any way.

_If you choose to use this software you do this at your own risk. I am not responsible for anything that happens to you,
your Raspberry Pi, your UPS or anything else related to your situation._

## Installation

Rough guide:

 * Install 

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get -y install i2c-tools python3-smbus python3-venv

 * Clone this repository in, say, `/home/pi/x728ups`.
 * Copy the `x728ups.service` file into `/etc/systemd/system` or use `systemctl link` to use it in-situ.
 * Modify the path in `/etc/systemd/system/x728ups.service` if you cloned elsewhere.
 * I like to use Python virtualenvs so I created one in the clone directory with `python -m venv venv` - you'll note that the systemd unit uses this virtualenv directly.
 * Setup virtual env `source venv/bin/activate` for bash or `source venv/bin/activate.fish` for fish
 * Install dependenicis `pip install -r requirements.txt`
 * Copy secret file `configurationExample.py` na rename to `configuration.py`

You can customise the shutdown duration after power-loss detection and minimum battery voltage thresholds by editing
the `configuration.py`.

This service also supports publishing voltage/capacity updates and event descriptions to a nearby MQTT server. If you have
one you can modify the script to make use of it. It publishes to the `ups/event`, `ups/voltage` and `ups/capacity` topics.

## License

This software is released under the standard MIT license. See `LICENSE` file for details.




