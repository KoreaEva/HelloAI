#!/bin/bash

# 리소스 그룹, 가상 머신, VNet, 서브넷, 네트워크 인터페이스 및 공용 IP에 대한 정보를 설정합니다.
resource_group_name="RG"
vm_prefix="myvm"
vnet_name="myvnet"
subnet_name="default"
vm_size="Standard_B1ls"
admin_username="tony"
admin_password="Pa55w.rd1234"
location="koreacentral"
publisher="Canonical"
offer="UbuntuServer"
sku="18.04-LTS"
version="latest"
subnet_address_prefix="10.0.0.0/24"
vnet_address_prefix="10.0.0.0/16"
vm_count=2
public_ip_allocation_method="Static"
public_ip_sku="Standard"
public_ip_dns_name_prefix="mydnsprefix"
default_resource_group="1"

# 리소스 그룹을 생성합니다.
#echo "Create Resource Group -------------------- $resource_group_name "
#az group create --name $resource_group_name --location $location --output none 

# VNet과 서브넷을 생성합니다.
echo "Create Virtual Network -------------------- $vnet_name "
az network vnet create --resource-group $resource_group_name$default_resource_group --name $vnet_name --address-prefixes $vnet_address_prefix --subnet-name $subnet_name --subnet-prefix $subnet_address_prefix --output none

# 가상 머신, 네트워크 인터페이스 및 공용 IP를 생성하고 VNet과 서브넷에 연결합니다.
for i in $(seq 1 $vm_count)
do
    vm_name="$vm_prefix$i"
    nic_name="$vm_name-nic"
    public_ip_name="$vm_name-ip"

    echo "Create Virtual Machine -------------------- $vm_name "

    # 공용 IP 주소를 생성합니다.
    echo "Create IP Address"

    az network public-ip create \
        --resource-group $resource_group_name$i \
        --name $public_ip_name \
        --sku $public_ip_sku \
        --allocation-method $public_ip_allocation_method \
        --dns-name $public_ip_dns_name_prefix$i \
        --output none

        # 네트워크 인터페이스를 생성하고 공용 IP 주소를 연결합니다.
    echo "Create Network Interface"

    az network nic create \
        --resource-group $resource_group_name$i \
        --name $nic_name \
        --vnet-name $vnet_name \
        --subnet $subnet_name \
        --public-ip-address $public_ip_name \
        --output none

    echo "Create VM"

    # 가상 머신을 생성합니다.
    az vm create \
        --resource-group $resource_group_name$i \
        --name $vm_name \
        --location $location \
        --image $publisher:$offer:$sku:$version \
        --size $vm_size \
        --admin-username $admin_username \
        --admin-password $admin_password \
        --nics $nic_name \
        --output none \
        #--public-ip-sku Standard \
    
    #Port를 연다. 
    echo "Open the port 22, 80"
    #az vm open-port --port 80 --resource-group $resource_group_name$i --name $vm_name
    #az vm open-port --port 22 --resource-group $resource_group_name$i --name $vm_name


    # az vm create \
    #     --resource-group $resource_group_name \
    #     --name $vm_name \
    #     --location $location \
    #     --size $vm_size \
    #     --image $publisher:$offer:$sku:$version \
    #     --admin-username $admin_username \
    #     --admin-password $admin_password \
    #     --nics $nic_name \
    #     --output none \

    az network nsg rule create \
        --resource-group $resource_group_name$i \
        --nsg-name ${vm_name}-nsg \
        --name allow-ssh-http \
        --priority 80 \
        --destination-port-ranges 22 100 \
        --access Allow \
        --output none \
    
    # az network nsg rule create \
    #     --resource-group $resource_group_name \
    #     --nsg-name ${vm_name}-nsg \
    #     --name allow-ssh-http \
    #     --priority 100 \
    #     --destination-port-ranges 80 \
    #     --access Allow \
    #     --output none \

done