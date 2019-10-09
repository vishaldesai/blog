insert into
   order_items_summary 
   select
      b.product_name,
      sum(a.unit_price*a.quantity),
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
   group by
      b.product_name,
      a.year,
      a.month,
      a.day,
      a.hour

