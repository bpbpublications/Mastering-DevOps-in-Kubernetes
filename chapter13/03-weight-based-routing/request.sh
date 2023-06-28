while :
do
    http get $INGRESS_HOST | grep "ism-app-"
    sleep 1
done
