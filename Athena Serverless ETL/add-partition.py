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


    while 2>1:
        sql_response = athena.get_query_execution(
            QueryExecutionId=sql['QueryExecutionId']
        )
 
        if sql_response['QueryExecution']['Status']['State'] == "SUCCEEDED":
            break
        elif sql_response['QueryExecution']['Status']['State'] == "FAILED":
            raise Exception('Error executing ' + sql['QueryExecutionId'])
        
    print('Execution ID: ' + sql['QueryExecutionId'] + ' has ' +
          sql_response['QueryExecution']['Status']['State'])
    return sql_response['QueryExecution']['Status']['State']

def lambda_handler(event, context):
    
    cnow = datetime.datetime.utcnow()
    cyear = str(cnow.year)
    cmonth = str("{0:02d}".format(cnow.month))
    cday = str("{0:02d}".format(cnow.day))
    chour = str("{0:02d}".format(cnow.hour))
    tablelist = os.environ["tablename"].split(",")
    
    ## Temporary code to simulate data ingestion
    s3 = boto3.resource('s3')
    #chour = str(int(chour)-13)
    source_key = 'ORDER_ITEMS_' + chour + '.csv'
    print(source_key)
    copy_source = {
        'Bucket': 'vishal-blog-staging1',
        'Key': source_key
    }
    bucket = s3.Bucket('vishal-blog-athena')
    target_key = 'order_items' + '/' + cyear + '/' + cmonth + '/' + cday + \
        '/' + chour + '/' + 'ORDER_ITEMS_' + chour + '.csv'
    bucket.copy(copy_source, target_key)
    
    
    for i in tablelist:
        print("Adding partition for " + i)

        sql_statement = "ALTER TABLE " + i + " ADD PARTITION (year='" + cyear + "',month='" + cmonth + "',day='" + cday + "',hour='" + chour + "') location  's3://" + os.environ["bucket"] + "/" + i + "/" + cyear + "/" + cmonth + "/" + cday + "/" + chour + "/'"
        print(sql_statement)
        SqlStatus=run_sql(sql_statement, os.environ["database"], os.environ["s3output"])
        
    return SqlStatus
       
