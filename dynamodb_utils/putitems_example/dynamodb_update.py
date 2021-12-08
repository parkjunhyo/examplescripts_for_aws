#! /usr/bin/env python3

import re, boto3

# DynamoDB information
use_default_key = True # if you want to use indivisual key, change False
info_tablename = '---------------'
info_access_keyid = '----------------'
info_access_key = '----------------'

# String Pattern for contact
correct_contact_endmark = ";"
wrong_contact_endmark = re.compile(";\s*")

# Connect Dynamodb
if use_default_key :
    client = boto3.client("dynamodb")
else:
    client = boto3.client("dynamodb",aws_access_key_id=info_access_keyid,aws_secret_access_key=info_access_key)

# insert the item from data_sample.txt
with open('data_sample.txt','r') as read_contents:
    for content in read_contents.readlines():
        content = wrong_contact_endmark.sub(correct_contact_endmark, content)
        splited_content = content.strip().split()
        reformed_json = {
            "uuid" : { "S" : splited_content[0] },
            "csp" : { "S" : splited_content[1] },
            "org_directory_id" : { "S" : splited_content[2] },
            "default_account_subscription_no" : { "S" : splited_content[3] },
            "child_account_subscription_no" : { "S" : splited_content[4] },
            "subnet_category" : { "S" : splited_content[5] },	
            "assigned_region" : { "S" : splited_content[6] },
            "assigned_status" : { "S" : splited_content[7] },
            "assigned_subnet" : { "S" : splited_content[8] },
            "assigned_subnet_size" : { "S" : splited_content[9] },
            "class_c_cidr" : { "S" : splited_content[10] },
            "attachment_status_gateway" : { "S" : splited_content[11] },
            "attachment_gateway_account_subscription_no" : { "S" : splited_content[12] },
            "attachment_gateway_resource_nameid" : { "S" : splited_content[13] },
            "assigned_virtualnet_nameid" : { "S" : splited_content[14] },
            "assigned_virtualnet_usage" : { "S" : splited_content[15] },
            "security_system_account_subscription_no" : { "S" : splited_content[16] },
            "security_system_version" : { "S" : splited_content[17] },
            "security_system_connected_status" : { "S" : splited_content[18] },
            "start_date" : { "S" : splited_content[19] },
            "end_date" : { "S" : splited_content[20] },
            "comments" : { "S" : splited_content[21] },
            "contacts" : { "S" : splited_content[22] }
        }
        response = client.put_item(
                TableName = info_tablename,
                Item = reformed_json
                )
        # un-comment to display response as the result
        print(response)



