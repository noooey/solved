# 183. Customers Who Never Order

## MySQL
```sql
SELECT
    ct.name as Customers
FROM Customers AS ct
LEFT JOIN Orders AS od
    ON ct.id = od.customerId
WHERE od.customerId IS NULL
```

## Notes
- Left Join
