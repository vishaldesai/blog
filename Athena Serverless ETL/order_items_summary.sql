CREATE EXTERNAL TABLE `order_items_summary`(
  `product_name` string, 
  `totalsale` bigint)
PARTITIONED BY ( 
  `year` string, 
  `month` string, 
  `day` string, 
  `hour` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://vishal-blog-athena/order_items_summary'
TBLPROPERTIES (
  'has_encrypted_data'='false',
)