# MQTT
MQTT_SERVER_ADDRESS = "localhost"
MQTT_SERVER_PORT = 1883
MQTT_SERVER_USER = "user"
MQTT_SERVER_PASSWORD = "password"
MQTT_ROOT = "ups"

# Shut down the pi if any of these thresholds are met
SHUTDOWN_BATTERY_CAPACITY = 50  # capacity falls below this percentage
SHUTDOWN_BATTERY_VOLTAGE = 3.6  # voltage falls below this value
SHUTDOWN_SECONDS = 20  # power-fail for longer than this duration

# x728 I2C bus info
I2C_BUS_ID = 1
I2C_ADDRESS = 0x36

GPIO_X728_SHUTDOWN = 5   # high for a duration if UPS requests reboot or shutdown
GPIO_X728_PLD = 6        # high if power loss detected
GPIO_X728_BOOT_OK = 12   # high if RPi is booted, UPS powers off when set low after shutdown request
GPIO_X728_SYSTEM = 13    # hold high to initiate system (UPS & RPi) reboot or shutdown


DATA_SEND_PERIOD = 60  # seconds between publishing battery data
MQTT_RETRY_PERIOD = 600  # seconds between retrying MQTT connection

SYSTEM_SHUTDOWN_REQUEST_DURATION = 4  # duration of GPIO 13 pulse, in seconds, to initiate system shutdown

REBOOT_PULSE_MINIMUM = 200  # milliseconds
REBOOT_PULSE_MAXIMUM = 600  # milliseconds