while true
do

	i=$(ip addr show wlan0 | awk '$1 == "inet" {gsub(/\/.*$/, "", $2); print $2}')
	n=${#i}

	echo $n

	if [ $n -ge 7 ]
	then
		echo "OK"
	else
		echo "NOK"
		echo 0 > /sys/bus/usb/devices/2-1/authorized
		echo 1 > /sys/bus/usb/devices/2-1/authorized
	fi

	sleep 60
done
