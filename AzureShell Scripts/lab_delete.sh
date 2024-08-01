TOTAL_USERS=101
TENANT="snuailab.onmicrosoft.com"
#TENANT="link21ailab.onmicrosoft.com"
#TENANT="msaischool.onmicrosoft.com"
#TENANT="kisedkoss.onmicrosoft.com"
#TENANT="helloaicloud.onmicrosoft.com"
#TENANT="daeguailab.onmicrosoft.com"
#TENANT="aiakor.onmicrosoft.com"
#USER_NAME="danuser"
USER_NAME="labuser"
#RESOURCE_GROUP="RGDAN"
RESOURCE_GROUP="RG"

# Ceate Group 
#az ad group delete --display-name "Lab"  --mail-nickname "Lab"

사용자 삭제
i=1
while [ $i -lt $TOTAL_USERS ]
do
  az ad user delete --id "$USER_NAME$i@$TENANT"
  echo "USER $USER_NAME$i@$TENANT DELETED." 
  #az group delete --name "$RESOURCE_GROUP$i" --yes &
  ((i+=1))
done

#리소스 그룹 삭제
az group list | grep name > tmp.txt

while read line; 
  do 
  #echo $line; 
  oldstr="\"name\":"
  oldstr2="\""
  oldstr3=","
  newstr=""
  group_name=$(echo $line | sed "s/$oldstr/$newstr/") 
  #group_name=$(echo $line | sed "s/$oldstr/$newstr/")
  group_name=$(echo $group_name | sed "s/$oldstr2/$newstr/") 
  group_name=$(echo $group_name | sed "s/$oldstr2/$newstr/")   
  group_name=$(echo $group_name | sed "s/$oldstr3/$newstr/")   
  #echo $group_name

  if [ $group_name = "Teacher-0" ]
  then
    echo "<PASS>"
  else
    echo "------------$group_name DELETE" 
    az group delete --name "$group_name" --yes &
  fi
done < tmp.txt

rm tmp.txt