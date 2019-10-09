CREATE OR REPLACE VIEW view_order_items_summary AS 
SELECT
  "product_name"
, "sum"("totalsale") "totalsale"
FROM
  (
   SELECT
     "product_name"
   , "totalsale"
   FROM
     default.order_items_summary
UNION ALL    SELECT
     "b"."product_name" "product_name"
   , "sum"(("a"."unit_price" * "a"."quantity")) "totalsale"
   FROM
     order_items a
   , product b
   WHERE ((((("a"."product_id" = "b"."product_id") AND ("a"."year" = CAST("year"(current_timestamp) AS varchar))) AND ("a"."month" = "lpad"(CAST("month"(current_timestamp) AS varchar), 2, '0'))) AND ("a"."day" = "lpad"(CAST("day"(current_timestamp) AS varchar), 2, '0'))) AND ("a"."hour" = "lpad"(CAST("hour"(current_timestamp) AS varchar), 2, '0')))
   GROUP BY "b"."product_name"
) 
GROUP BY "product_name"
