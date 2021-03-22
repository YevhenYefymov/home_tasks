#! /bin/ash


#MY_IP=$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)
IP_TO_CONNECT=$(cat /mnt/host/savedip)
nc $IP_TO_CONNECT 8080
#"This is a message to a client!"
#"And another one!"
