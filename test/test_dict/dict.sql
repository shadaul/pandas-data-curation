-- WITH RankedLogs AS(
--     SELECT
--         order_id,
--         status,
--         log_time,
--         ROW_NUMBER() OVER(
--             PARTITION BY order_id
--             ORDER by log_time DESC
--         ) as row_num
--     FROM order_logs
-- )

-- SELECT 
--     order_id,
--     status
-- FROM RankedLogs
-- WHERE row_num = 1

-- SELECT order_id, status, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY log_time DESC) as sticker_num 
-- FROM order_logs;

-- WITH mytable as(
--     SELECT
--         item_name,
--         purchase_time,
--         client_id,
--         ROW_NUMBER() OVER(
--             PARTITION by client_id ORDER by purchase_time ASC
--         ) as row_num
--     FROM sales
-- )
-- SELECT
--     client_id,
--     item_name
-- FROM mytable
-- WHERE row_num = 1

-- WITH time_machine AS (

--     SELECT 
--         client_id, 
--         visit_date, 
--         LAG(visit_date) OVER (PARTITION by client_id ORDER by visit_date ASC) as prev_visit
--     FROM visits
-- )

-- SELECT 
--     client_id,
--     visit_date,
--     DATEDIFF(day, prev_visit, visit_date) as days_since_last
-- FROM time_machine;

-- SELECT client_id, sum(amount) as total_spent
-- from orders
-- GROUP by client_id
-- HAVING sum(amount) > 600;

-- WITH prev_purchase as (
--     SELECT
--         client_id,
--         purchase_date,
--         LAG(purchase_date) OVER (PARTITION by client_id order by purchase_date ASC) as prev_date
--     from purchases
-- )

-- SELECT DISTINCT client_id
-- from prev_purchase
-- where purchase_date - prev_date = 1

-- SELECT c.name, sum(t.amount)
-- from clients c JOIN transactions t on c.client_id = t.client_id
-- GROUP by c.name
-- HAVING sum(amount) > 5000

-- SELECT DISTINCT amount
-- FROM transfers
-- ORDER BY amount DESC
-- LIMIT 1 OFFSET 1;


-- SELECT transfer_id, amount,
-- CASE 
--     when amount > 10000 then 'high'
--     when amount >= 1000 then 'medium'
--     else 'low'
-- end as risk_level
-- from transfers

-- SELECT d.city_name, sum(f.amount) as total_amount
-- from fact_transactions f JOIN dim_cities d on f.city_id = d.city_id
-- where country_name = 'Switzerland'
-- GROUP by d.city_name
-- order by total_amountamount DESC
-- LIMIT 1


-- WITH cte as (
--     SELECT client_id, amount,
--     dense_rank () OVER (PARTITION by client_id order by amount DESC) as rank
--     from transactions
-- )
-- SELECT client_id, amount, rank
-- from cte
-- where rank <=2


-- SELECT client_id, pay_date, amount,
-- LAG(amount) over (PARTITION by client_id order by pay_date) as prev_amount
-- from payments


SELECT user_id, amount, operation_date
from card_payments
where operation_date like '2026-03-%'

UNION ALL

SELECT user_id, amount, operation_date
from crypto_transfers
where operation_date like '2026-03-%'
