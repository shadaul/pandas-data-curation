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

SELECT order_id, status, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY log_time DESC) as sticker_num 
FROM order_logs;