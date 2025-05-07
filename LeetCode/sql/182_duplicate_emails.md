# 182. Duplicate Emails

## MySQL
```sql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1
```

## Notes
- Group By & Having
