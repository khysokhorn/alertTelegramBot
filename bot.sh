#!/bin/bash

token='5476532482:AAFBrQgyMQXDN6bc27nuKYBfoYyAoz636bI'
tele_url="https://api.telegram.org/bot${token}";
# curl -s "${tele_url}/getUpdates" | json_pp

# chat_id=$(curl -s "${tele_url}/getUpdates" | jq -r ".result[-1].update_id")
echo $chat_id
# curl -s "${tele_url}/sendMessage?chat_id=${chat_id}" \
#   --data-urlencode "text=$1" | json_pp

curl https://api.telegram.org/bot$token/sendMessage\?chat_id\=-1001508760330\&text\="$1"