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
            database_values={
                    "dbname" : g_database_name,
                    }
            # create database
            query_msg_string = "create database {dbname}".format_map(database_values)

            # drop database
            #query_msg_string = "drop database {dbname}".format_map(database_values)
            
            # run command
            cur.execute(query_msg_string)
            cur.close()


            print(sys_argv)
        else:
            # error.1
            print("[error.1] need more parameters as the table name")
            sys.exit()


if __name__ == "__main__":

    main_feature = Main_Class()
    main_feature.run(sys.argv[1:])
