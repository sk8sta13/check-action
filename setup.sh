#!/bin/bash

CONFIGFILE=./config.json
if [ ! -f "$CONFIGFILE" ]; then
    echo "{
    \"token_api\": \"\",
    \"email\": {
        \"server\": \"\",
        \"port\": null,
        \"username\": \"\",
        \"password\": \"\"
    },
    \"users\": [
        {
            \"first_name\": \"\",
            \"last_name\": \"\",
            \"email\": \"\",
            \"actions\": [
                {
                    \"label\": \"\",
                    \"purchase\": null,
                    \"sell\": null
                }
            ]
        }
    ]
}" >> ./config.json
fi

myfilesize=$(wc -c "./config.json" | awk '{print $1}')
if [ "$myfilesize" -le 442 ]; then
    echo "You need set configurations in file config.json."
else
    chmod +x check_action.py
    systemlocal=$(pwd)
    sed -i -e "s|#WD|$systemlocal|g" check_action.service
    cp check_action.service /etc/systemd/system/check_action.service
    systemctl enable check_action

    echo "Finished installation."
fi
