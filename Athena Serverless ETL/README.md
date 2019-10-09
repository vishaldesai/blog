
Replace parameters, role names and xxxxxxxxxxxxxx with relevant account numbers in all the files.

### Lambda Functions

- add-partition.yaml - SAM file to deploy add-partition.py lambda function
- execute-etl.yaml - SAM file to deploy execute-etl.py lambda function
- get-etl-status.yaml - SAM file to deploy get-etl-status.py function

### Step Function

- StepFunction.json - Step function definition file to orchestrate lambda functions.

### Curated Table and View DDL


- order_items_summary.sql	- DDL to create order_items_summary table.
- order_items_fact.sql - DDL to create denormalized order_items_fact table.
- view_order_items_summary.sql	- View DDL that combines sales total from summary table for historical data and source tables for latest hour partition.

### Reporting test sql

- test.sql - Reporting test sql statements.



