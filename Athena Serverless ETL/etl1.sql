insert into
   order_items_fact 
   select
      a.order_id,
      a.line_item_id,
      a.product_id,
      b.product_name,
      a.unit_price,
      a.quantity,
      a.year,
      a.month,
      a.day,
      a.hour 
   from
      order_items a,
      product b 
   where
      a.product_id = b.product_id 
      and a.year = '{pyear}' 
      and a.month = '{pmonth}' 
      and a.day = '{pday}' 
      and a.hour = '{phour}'