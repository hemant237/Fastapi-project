## DATE-21/07/2026 

## What is a PostgreSQL Server?
A PostgreSQL Server is the database management system (DBMS) that manages one or more databases.

## What is a Database?
A database is a logical container that stores tables, views, functions, and other database objects.

## What is a Schema?
A schema is a logical container (or namespace) inside a database used to organize tables, views, functions, and other database objects.

## What is a Table?
A table is a structured collection of rows and columns used to store data.

## Difference between a Row and a Column
A row represents one complete record, while a column represents one attribute of that record.

## What is a Primary Key?
A primary key is a unique, non-NULL identifier for each row in a table.

## SQL commands for CRUD
- Create → INSERT
- Read → SELECT
- Update → UPDATE
- Delete → DELETE

## DATE - 22/07/2026

## What is DDL?
DDL (Data Definition Language) is used to define and modify the structure of a database. Examples include CREATE, ALTER, DROP, and TRUNCATE.

## What does CREATE TABLE do?
The CREATE TABLE command creates a new table in the database.

## What does SERIAL do?
SERIAL automatically generates incrementing integer values, making it useful for auto-incrementing primary keys.

## Why do we use PRIMARY KEY?
A PRIMARY KEY uniquely identifies each row in a table. It must contain unique values and cannot be NULL.

## Difference between INTEGER and VARCHAR
INTEGER stores whole numbers, while VARCHAR stores variable-length text.

## Why don't we insert IDs manually when using SERIAL?
Because PostgreSQL automatically generates sequential IDs, reducing errors and maintaining consistency.

## SQL command to create a table
The CREATE TABLE command is used to create a new table in the database.


## DATE -- 24/07/2026

## What is a CTE?
A Common Table Expression (CTE) is a temporary named result set that exists only for the duration of a single SQL query.
It is created using the `WITH` keyword.

## Syntax
```sql
WITH cte_name AS (
    SELECT ...
)

SELECT *
FROM cte_name;
```
## Advantages of CTEs
- Improves readability
- Makes complex queries easier to understand
- Easier to debug
- Can be referenced multiple times within the same query

## CTE vs View
CTE:
- Temporary
- Exists only during query execution
- Created using `WITH`
View:
- Permanent database object
- Created using `CREATE VIEW`

## Important Note
A CTE is not a real table. It is a temporary result set that disappears after the query finishes.

## DATE - 03/08/2026 

## What is a Window Function?
A window function performs calculations across a set of rows while preserving the original rows in the result.

## What does OVER() do?
The OVER() clause tells SQL to perform the calculation over a window of rows without reducing the number of rows.

## Aggregate Function vs Window Function
Aggregate Function:
- Reduces multiple rows into one row.
- Often used with GROUP BY.
Window Function:
- Performs calculations while keeping all rows.
- Uses the OVER() clause.

## Aggregate Functions as Window Functions
Aggregate functions like AVG(), SUM(), COUNT(), MIN(), and MAX() can be used as window functions by adding the OVER() clause.

Example:

```sql
SELECT
    name,
    AVG(salary) OVER() AS average_salary
FROM employees;
```
## Advantages of Window Functions
- Preserve original rows.
- Perform calculations without collapsing data.
- Useful for ranking, running totals, comparisons, and analytics.

## What is PARTITION BY?
PARTITION BY divides rows into logical groups (partitions) and applies a window function separately to each group while preserving all rows.

## Does PARTITION BY reduce rows?
No. It keeps all rows and performs calculations within each partition.

## GROUP BY vs PARTITION BY
GROUP BY:
- Reduces rows.
- Used with aggregate functions.
PARTITION BY:
- Preserves rows.
- Used with window functions.

## Aggregate Functions with PARTITION BY
Functions like AVG(), SUM(), COUNT(), MIN(), and MAX() can be used with PARTITION BY to calculate values within each partition.
Example:
```sql
SELECT
    name,
    salary,
    AVG(salary) OVER(PARTITION BY department_id)
FROM employees;
```

# DATE - 04/08/2026

## What is ROW_NUMBER()?
ROW_NUMBER() assigns a unique sequential number to each row based on the specified ordering.

## Why is ORDER BY required?
ORDER BY determines the sequence in which row numbers are assigned.

## Does ROW_NUMBER() assign duplicate numbers?
No. Every row receives a unique row number, even if multiple rows have the same values.

## ROW_NUMBER() with PARTITION BY
When PARTITION BY is used, row numbering restarts from 1 for each partition.
Example:
```sql
SELECT
    name,
    salary,
    ROW_NUMBER() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS row_num
FROM employees;
```
## Common Use Cases
- Find the highest-paid employee in each department.
- Find the Top N records.
- Remove duplicate records.
- Create leaderboards.
- Implement pagination.

## ROW_NUMBER()
ROW_NUMBER() assigns a unique sequential number to every row, even if multiple rows have the same value.

## RANK()
RANK() assigns the same rank to equal values. If there is a tie, the next rank is skipped.
Example:
1, 2, 2, 4

## DENSE_RANK()
DENSE_RANK() assigns the same rank to equal values but does not skip the next rank.
Example:
1, 2, 2, 3

## Difference Between ROW_NUMBER(), RANK(), and DENSE_RANK()
ROW_NUMBER():
- Unique number for every row.
RANK():
- Same rank for ties.
- Skips the next rank.
DENSE_RANK():
- Same rank for ties.
- Does not skip the next rank.

## Common Use Cases
ROW_NUMBER():
- Pagination
- Removing duplicates
- Latest record per group
RANK():
- Sports competitions
- Leaderboards with ties
DENSE_RANK():
- Salary bands
- Product rankings
- Performance rankings without gaps

## DATE - 05/08/2026

## What is LAG()?
LAG() returns the value from the previous row based on the specified ordering.

## What is LEAD()?
LEAD() returns the value from the next row based on the specified ordering.

## Why does LAG() return NULL for the first row?
The first row has no previous row, so LAG() returns NULL by default.

## Offset in LAG() and LEAD()
The offset specifies how many rows backward or forward to look.
Example:
```sql
LAG(sales,2)
```
Returns the value from two rows before the current row.

## Default Value
A default value can be provided if there is no previous or next row.
Example:

```sql
LAG(sales,1,0)
```
Returns 0 instead of NULL for the first row.

## Common Use Cases
- Month-over-month growth
- Year-over-year comparison
- Salary increment analysis
- Sales trend analysis
- Time-series analytics

## What is a Running Total?
A running total is the cumulative sum of values from the first row up to the current row based on a specified order.

## Running Total Syntax
```sql
SELECT
    month,
    sales,
    SUM(sales) OVER(ORDER BY month) AS running_total
FROM sales;
```
## Difference Between SUM() OVER() and SUM() OVER(ORDER BY ...)
SUM() OVER():
- Returns the total sum for every row.
SUM() OVER(ORDER BY ...):
- Returns the cumulative sum up to the current row.

## Why is ORDER BY Required?
ORDER BY defines the sequence in which values are accumulated. Without it, SQL cannot calculate a running total.

## Running Totals with PARTITION By
PARTITION BY restarts the running total for each partition.
Example:
```sql
SUM(salary)
OVER(
    PARTITION BY department_id
    ORDER BY salary
)
```
## Common Use Cases
- Running sales
- Cumulative revenue
- Month-to-Date (MTD)
- Year-to-Date (YTD)
- Running customer count

## DATE - 06/08/2026

## What is a Moving Average?
A moving average is the average calculated over a fixed-size window of rows that moves as SQL processes each row.

## Why can't AVG() OVER() calculate a Moving Average?
AVG() OVER() calculates the average over the entire window. A moving average requires a fixed-size window, which is defined using ROWS BETWEEN.

## What does ROWS BETWEEN do?
ROWS BETWEEN defines the window frame by specifying which rows should be included in the calculation.

## Moving Average Syntax
```sql
SELECT
    month,
    sales,
    AVG(sales)
    OVER(
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM sales;
```

## Running Total vs Moving Average
Running Total:
- Uses all previous rows up to the current row.
- The window keeps growing.
Moving Average:
- Uses a fixed-size window.
- The window moves with each row.

## Common Use Cases
- Stock market analysis
- Sales forecasting
- Website traffic analysis
- Time-series analytics
- Machine learning trend analysis

## What is an Index?
An index is a data structure that helps the database retrieve rows faster without scanning the entire table.

## Why are Indexes Used?
Indexes improve query performance by allowing the database to locate rows quickly.

## Advantages of Indexes
- Faster SELECT queries
- Faster filtering using WHERE
- Faster JOIN operations
- Can improve ORDER BY performance

## Disadvantages of Indexes
- Uses additional storage space
- Slows down INSERT operations
- Slows down UPDATE operations
- Slows down DELETE operations

## Primary Key and Index
In PostgreSQL, a PRIMARY KEY automatically creates a unique B-Tree index.

## Good Columns for Indexing
- Primary keys
- Foreign keys
- Email
- Frequently searched columns
- Columns used in JOIN conditions

## Poor Columns for Indexing
Columns with very few unique values, such as gender or boolean fields, are usually poor candidates because the index provides little benefit.

## What is EXPLAIN?
EXPLAIN shows PostgreSQL's estimated execution plan, including how it plans to execute the query and the estimated cost.

## What is EXPLAIN ANALYZE?
EXPLAIN ANALYZE executes the query and shows the actual execution plan along with the actual execution time.

## Sequential Scan vs Index Scan
Sequential Scan:
- Reads the table row by row.
- Used when no suitable index is available or when scanning most of the table.
Index Scan:
- Uses an index to locate rows quickly.
- Efficient for searching a small number of rows.

## What is Cost?
Cost is PostgreSQL's internal estimate of how expensive a query plan is. It is not the actual execution time.

## Difference Between EXPLAIN and EXPLAIN ANALYZE
EXPLAIN:
- Does not execute the query.
- Shows the estimated execution plan.
EXPLAIN ANALYZE:
- Executes the query.
- Shows the actual execution plan and execution statistics.

## Common Use Cases
- Analyze slow queries.
- Check whether an index is being used.
- Compare different query execution plans.
- Optimize database performance.


## What is Query Optimization?
Query optimization is the process of writing SQL queries so they execute faster while using fewer database resources.

## Common Query Optimization Techniques
- Avoid SELECT *
- Retrieve only required columns
- Use appropriate indexes
- Filter data using WHERE
- Optimize JOIN conditions
- Use EXPLAIN ANALYZE to inspect execution plans

## Avoid Functions on Indexed Columns
Applying functions or arithmetic operations to indexed columns (e.g., LOWER(email) or employee_id + 1) may prevent PostgreSQL from using the index efficiently.
Example:

```sql
-- Less efficient
WHERE employee_id + 1 = 100

-- Better
WHERE employee_id = 99
```
## Why Use LIMIT?
LIMIT retrieves only the required number of rows during testing, reducing execution time and unnecessary data transfer.

## First Step for a Slow Query
Use EXPLAIN ANALYZE to understand how PostgreSQL executes the query before making optimizations.


































