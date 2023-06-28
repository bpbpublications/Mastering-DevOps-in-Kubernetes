while :
do
    http get $INGRESS_HOST/api/ism-app-backend | grep "ism-app-"
    sleep 1
done
