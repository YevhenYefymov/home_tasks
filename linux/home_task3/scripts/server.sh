#! /bin/ash

touch /mnt/host/savedip

MY_IP=$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)
echo $MY_IP > /mnt/host/savedip

nc -vlkp 8080
