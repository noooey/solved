# 185. Employees Earning More Than Their Managers

## MySQL
```sql
SELECT
    e.name AS Employee
FROM Employee AS e
JOIN Employee AS m
    ON e.managerId = m.id
WHERE e.salary > m.salary
```

## Notes
- Self Join
