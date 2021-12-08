#! /usr/bin/env python3

import mariadb
import sys


import sys

# DB Parameters
g_mariadb_user = ""
g_mariadb_password = ""
g_mariadb_host = "mariadb.aws.remote-target.site"
g_mariadb_port = 3306
g_database_name = "sktcloud_ip_management"
g_table_name = "sktcloud_azure_ipms_a"

# parameter
database_values={
        "dbname" : g_database_name,
        "tbname": g_table_name
        }

class Main_Class:

    def run(self, sys_argv):
        sys_argv_len = len(sys_argv)
        if not sys_argv_len:
            conn = mariadb.connect(
                    user = g_mariadb_user,
                    password = g_mariadb_password,
                    host = g_mariadb_host,
                    port = g_mariadb_port
                    )
            cur = conn.cursor()
            
            # query strings
            query_msg_string = '''create table {dbname}.{tbname} (
            uuid VARCHAR(300) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            cloud_service_provider VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            organizagion_directory_id VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            account_subscription_id VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            inherited_account_subscription_id VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_subnet_category VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_region VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_status VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_subnet VARCHAR(300) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_subnetmask_size VARCHAR(300) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            classified_by_class_c_block VARCHAR(300) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            gateway_attachment_status VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            account_subscription_id_for_gateway VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            gateway_nameid VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_virtualnet_nameid VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            assigned_virtualnet_usage VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            account_subscription_id_for_access_management VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            access_management_info  VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            access_management_connected_status VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            begin_date VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            due_date VARCHAR(150) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            comments VARCHAR(600) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            contacts VARCHAR(600) charset 'utf8mb4' collate 'utf8mb4_general_ci',
            PRIMARY KEY (`uuid`)
            )
            '''.format_map(database_values).strip()

            # drop table
            #query_msg_string = "drop table {dbname}.{tbname}".format_map(database_values)

            # run command
            cur.execute(query_msg_string)
            cur.close()


        else:
            # error.1
            print("[error.1] need more parameters as the table name")
            sys.exit()


if __name__ == "__main__":

    main_feature = Main_Class()
    main_feature.run(sys.argv[1:])


