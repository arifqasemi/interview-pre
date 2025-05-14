select AVG(order_count)
from(select name,COUNT(*) as order_count from product)