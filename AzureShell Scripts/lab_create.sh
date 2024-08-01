TOTAL_USERS=101
USER_PASSWORD="!Seoul2024"

#TENANT="msaischool.onmicrosoft.com"
#TENANT="daeguailab.onmicrosoft.com"
#TENANT="kisedkoss.onmicrosoft.com"
#TENANT="helloaicloud.onmicrosoft.com"
#TENANT="link21ailab.onmicrosoft.com"
TENANT="snuailab.onmicrosoft.com"
#USER_NAME="danuser"
USER_NAME="labuser"
#RESOURCE_GROUP="RGDAN"
RESOURCE_GROUP="RG"

# Ceate Group 
#az ad group create --display-name "Lab"  --mail-nickname "Lab"

i=1
member_id=""

while [ $i -lt $TOTAL_USERS ]
do
  echo "$i ----------------------------------------------user development eviroment setting.. "

  # Create User
  az ad user create --display-name "$USER_NAME$i" --password "$USER_PASSWORD" --user-principal-name "$USER_NAME$i@$TENANT" | jq '.id' > tmp.txt
  cat tmp.txt | read member_id 
  member_id=$(<tmp.txt)

  #앞뒤의 ""를 제거해 준다. 
  oldstr="\""
  newstr=""
  member_id=$(echo $member_id | sed "s/$oldstr/$newstr/") 
  member_id=$(echo $member_id | sed "s/$oldstr/$newstr/") 

  # Lab 그룹에 추가한다. 
  az ad group member add --group Lab --member-id $member_id

  #echo "Create Resource Group and Resoure Group Onwer role.------------------------------------"
  az group create --name "$RESOURCE_GROUP$i" --location koreacentral
  az role assignment create --assignee $USER_NAME$i@$TENANT --role Contributor -g $RESOURCE_GROUP$i &
  
  rm tmp.txt
  ((i+=1))
done