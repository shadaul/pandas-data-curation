SELECT name 
FROM customers LEFT JOIN orders on customers.id = orders.customer_id
where orders.order_id is NULL