
# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import the SDK
import time
import datetime
from datetime import timedelta
import boto3
import os

def run_sql(sql_statement, database, s3_output):
    
    athena = boto3.client('athena')
    sql = athena.start_query_execution(
        QueryString=sql_statement,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': s3_output,
        }
    )


    return sql['QueryExecutionId']


def lambda_handler(event, context):
    #Derive year, month, day and hour. Athena here will process source table partitions from previous hour
    pnow = datetime.datetime.utcnow() - timedelta(hours=1)
    pyear = str(pnow.year)
    pmonth = str("{0:02d}".format(pnow.month))
    pday = str("{0:02d}".format(pnow.day))
    phour = str("{0:02d}".format(pnow.hour))

    #Loop through all the ETL statements
    try:
        sql_statement_ids={}
        s3 = boto3.client('s3')
        s3resource = boto3.resource('s3')
        resp = s3.list_objects_v2(Bucket=os.environ["etlcodebucket"])
        i = 1
        for objlist in resp['Contents']:
            
            obj = s3resource.Object(os.environ["etlcodebucket"], objlist['Key'])
            sql_statement = obj.get()['Body'].read().decode('utf-8').format(pyear=pyear, pmonth=pmonth, pday=pday, phour=phour)
            print("Executing statement:" + sql_statement)
            sql_statement_id = run_sql(sql_statement, os.environ["database"], os.environ["s3output"])
            sql_statement_ids.update({'id' + str(i) : sql_statement_id})
            i = i + 1
    except:
        raise Exception('Error submitting ETL Statements')
    

    return sql_statement_ids
