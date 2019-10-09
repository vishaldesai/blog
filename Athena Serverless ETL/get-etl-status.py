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
import json
import boto3

def get_status(QueryExecutionId):
    
    athena = boto3.client('athena')

    sql_response = athena.get_query_execution(
        QueryExecutionId=QueryExecutionId
    )

    print('Execution ID: ' + QueryExecutionId + ' has ' +
          sql_response['QueryExecution']['Status']['State'])
    return sql_response['QueryExecution']['Status']['State']

def lambda_handler(event, context):
    print(event)
    status={}
    for key,value in event.items():
        if 'id' in key:
            status.update({key: get_status(value)})
       
        
    print(status)
    for key,value in status.items():
        if 'FAILED' in value:
            return 'FAILED'
        elif 'RUNNING' in value:
            return 'RUNNING'
        elif 'SUCCEEDED' in value:
            return 'SUCCEEDED'
        
    
