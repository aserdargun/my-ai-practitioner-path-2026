# Month 05: SQL & Databases

**Duration**: 4 weeks
**Focus**: Database fundamentals and SQL

---

## Objectives

By the end of this month, you will:

- [ ] Write SQL queries (SELECT, JOIN, GROUP BY)
- [ ] Design simple database schemas
- [ ] Use SQLite from Python
- [ ] Combine SQL with Pandas
- [ ] Build a database-backed application

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | SQL Basics | Basic queries |
| Week 2 | Joins & Subqueries | Complex queries |
| Week 3 | Python + SQLite | Database integration |
| Week 4 | Project | Complete application |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| SQLite | Database engine |
| SQL | Query language |
| sqlite3 | Python DB module |

---

## Project: Inventory Management

Build an inventory system with:

- SQLite database backend
- CRUD operations
- Reporting queries
- Python interface

---

## Key Concepts

### Basic SQL

```sql
SELECT product_name, price
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC;
```

### Joins

```sql
SELECT o.order_id, c.name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id;
```

### Python Integration

```python
import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM products WHERE price > ?", (100,))
results = cursor.fetchall()

conn.close()
```
