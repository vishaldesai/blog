CREATE EXTERNAL TABLE `order_items_fact`(
  `order_id` bigint, 
  `line_item_id` bigint, 
  `product_id` bigint, 
  `product_name` string, 
  `unit_price` bigint, 
  `quantity` bigint)
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
  's3://vishal-blog-athena/order_items_deno'
TBLPROPERTIES (
  'has_encrypted_data'='false'
)