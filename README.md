# Stock market stock monitoring service

Receive an email when the value of the monitored action reaches the value configured to buy or sell.

## Install

Clone this repository, enter the project folder, add execute permission in the setup.sh file and run it. See the step by step below:

```bash
git clone https://github.com/sk8sta13/check-action.git
cd check-action
chmod +x setup.sh
sudo ./setup.sh
```

When you run setup for the first time, the configuration file will be created, you need to configure the settings, and then run setup.sh again.

When the installation is finished, the check-action becomes a service on linux enabled, so it is started along with the computer, you can change this behavior just by disabling:

```bash
systemctl enable check-action
```

It is also possible to stop the service, start it and or restart it:

```bash
systemctl check-action stop
systemctl check-action start
systemctl check-action restart
```

## Configuration

This is the configuration file:

```bash
{
    "token_api": "",
    "email": {
        "server": "",
        "port": null,
        "username": "",
        "password": ""
    },
    "users": [
        {
            "first_name": "",
            "last_name": "",
            "email": "",
            "actions": [
                {
                    "label": "",
                    "purchase": null,
                    "sell": null
                }
            ]
        }
    ]
}
```

See that it is a file in JSON format, the token_api you can get here: https://www.alphavantage.co/, using the free option it is now possible to obtain a token. The settings are very intuitive, I believe that the only one that needs an explanation is the "actions" section, in the label is the "trading code" of the action, it is used to be searched in the api, so pay attention to write it correctly, in purchase you must put the value at which you intend to pay the share, and sell the value at which you intend to sell the share. An important point is that we can have several actions, as well as we can have several users.