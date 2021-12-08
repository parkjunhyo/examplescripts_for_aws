#! /usr/bin/env python3

import mariadb
import sys
import re
import boto3

# dynamodb
access_keyid = ""
access_secret = ""
access_dynamodb_table = ""
# mariadb

# DB Parameters
g_mariadb_user = ""
g_mariadb_password = ""
g_mariadb_host = "mariadb.aws.remote-target.site"
g_mariadb_port = 3306
g_database_name = "sktcloud_ip_management"
g_table_name = "sktcloud_aws_ipms_a"

# parameter
database_values={
        "dbname" : g_database_name,
        "tbname": g_table_name
        }

# access database
conn = mariadb.connect(
        user = g_mariadb_user,
        password = g_mariadb_password,
        host = g_mariadb_host,
        port = g_mariadb_port
        )
cur = conn.cursor()

# open dynamodb
client = boto3.client("dynamodb",
        aws_access_key_id = access_keyid,
        aws_secret_access_key = access_secret
        )

response = client.scan(
        TableName = access_dynamodb_table,
        )

# compiled pattern for compare
compre_assgine_sbunet = re.compile("not\-assigned")
compre_attachment = re.compile("attached")
compre_subnet_cloud = re.compile("100\.64")
compre_subnet_private = re.compile("192\.168")

for content in response['Items']:
    # default 
    exp_directory_value = "none"
    exp_security_status = "none"
    exp_security_id = "none"
    exp_security_version = "none"
    exp_gateway_account = "none"
    exp_gateway_id = "none"
    exp_assgined_region = "none"
    exp_subnet_category = "none"
    #
    if compre_assgine_sbunet.match(content['assigned_status']['S']):
        pass
    else:
        if compre_attachment.match(content['dx_er_attachment_status']['S']):
            exp_directory_value = "o-
            exp_security_status = "connected"
            exp_security_id = "#"
            exp_security_version = "f8"
            exp_gateway_account = "#"
            exp_gateway_id = "tgw-"
            exp_assgined_region = content['assigned_region']['S']
            if compre_subnet_cloud.search(content['assigned_subnet']['S']):
                exp_subnet_category = "-cloud-subnet"
            elif compre_subnet_private.search(content['assigned_subnet']['S']):
                exp_subnet_category = "-private-subnet"
    #
    info_to_insert = {
            "uuid" : content['uuid']['S'],
            "cloud_service_provider" : content['csp']['S'],
            "organizagion_directory_id" : exp_directory_value,
            "account_subscription_id" : content['default_account_subscription_no']['S'],
            "inherited_account_subscription_id" : content['shared_account_subscription_no']['S'],
            "assigned_subnet_category" : exp_subnet_category,
            "assigned_region" : exp_assgined_region,
            "assigned_status" : content['assigned_status']['S'],
            "assigned_subnet" : content['assigned_subnet']['S'],
            "assigned_subnetmask_size" : content['assigned_subnet_size']['S'],
            "classified_by_class_c_block" : content['class_c_cidr']['S'],
            "gateway_attachment_status" : content['dx_er_attachment_status']['S'],
            "account_subscription_id_for_gateway" : exp_gateway_account,
            "gateway_nameid" : exp_gateway_id,
            "assigned_virtualnet_nameid" : content['virtualnetwork_name']['S'],
            "assigned_virtualnet_usage" : content['virtualnetwork_usage']['S'],
            "account_subscription_id_for_access_management" : exp_security_id,
            "access_management" : exp_security_version,
            "access_management_connected_status" : exp_security_status,
            "begin_date" : content['start_date']['S'],
            "due_date" : content['end_date']['S'],
            "comments" : content['comments']['S'],
            "contacts" : content['contacts']['S']
            }
    info_to_insert.update(database_values)
    query_msg_string = '''insert into {dbname}.{tbname} (
            uuid,
            cloud_service_provider,
            organizagion_directory_id,
            account_subscription_id,
            inherited_account_subscription_id,
            assigned_subnet_category,
            assigned_region,
            assigned_status,
            assigned_subnet,
            assigned_subnetmask_size,
            classified_by_class_c_block,
            gateway_attachment_status,
            account_subscription_id_for_gateway,
            gateway_nameid,
            assigned_virtualnet_nameid,
            assigned_virtualnet_usage,
            account_subscription_id_for_access_management,
            access_management_info,
            access_management_connected_status,
            begin_date,
            due_date,
            comments,
            contacts
            ) values (
            "{uuid}",
            "{cloud_service_provider}",
            "{organizagion_directory_id}",
            "{account_subscription_id}",
            "{inherited_account_subscription_id}",
            "{assigned_subnet_category}",
            "{assigned_region}",
            "{assigned_status}",
            "{assigned_subnet}",
            "{assigned_subnetmask_size}",
            "{classified_by_class_c_block}",
            "{gateway_attachment_status}",
            "{account_subscription_id_for_gateway}",
            "{gateway_nameid}",
            "{assigned_virtualnet_nameid}",
            "{assigned_virtualnet_usage}",
            "{account_subscription_id_for_access_management}",
            "{access_management}",
            "{access_management_connected_status}",
            "{begin_date}",
            "{due_date}",
            "{comments}",
            "{contacts}"
            )
        '''.format_map(info_to_insert).strip()
    cur.execute(query_msg_string)

# run execute query
conn.commit()
conn.close()
