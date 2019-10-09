select product_name,sum(totalsale) as "totalsales"
from "default"."order_items_summary" 
group by product_name order by 2 desc;


select product_name,sum(unit_price*quantity) as "totalsales"
from "default"."order_items_fact" 
group by product_name order by 2 desc;


select b.product_name,sum(a.unit_price*a.quantity) as "totalsales"
from "default"."order_items" a , "default"."product" b
where a.product_id = b.product_id
and NOT (year='2019'and month='09' and day='27' and hour='12')
group by product_name order by 2 desc;

SELECT * FROM "default"."view_order_items_summary"
order by 2 desc;

select b.product_name,sum(a.unit_price*a.quantity) as "totalsales"
from "default"."order_items" a , "default"."product" b
where a.product_id = b.product_id
group by product_name order by 2 desc;

