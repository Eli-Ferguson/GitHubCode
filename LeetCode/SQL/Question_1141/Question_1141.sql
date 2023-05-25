# Write your MySQL query statement below

SELECT activity_date day, count( distinct( user_id ) ) active_users
FROM Activity
WHERE activity_date between '2019-06-28' and '2019-07-27'
GROUP BY day

-- Runtime better than 89.92%, 760ms