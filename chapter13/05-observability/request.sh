while :
do
    http get $INGRESS_HOST/api/ism-app | grep "ism-app-"
    sleep 1
    http get $INGRESS_HOST/api/v1/ism-app | grep "ism-app-"
    sleep 1
    http get $INGRESS_HOST/api/v2/ism-app | grep "ism-app-"
    sleep 1
done
