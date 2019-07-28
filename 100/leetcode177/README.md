# 第N高的薪水

> 编写一个 SQL 查询，获取 Employee 表中第 n 高的薪水（Salary）。

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
例如上述 Employee 表，n = 2 时，应返回第二高的薪水 200。如果不存在第 n 高的薪水，那么查询应返回 null。

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

```


## 解决办法：
1. 创建函数的方法。。有点难

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
  SELECT  IF(count<N,NULL,min)
  FROM
    (SELECT MIN(Salary) AS min, COUNT(1) AS count
    FROM
      (SELECT DISTINCT Salary
      FROM Employee ORDER BY Salary DESC LIMIT N) AS a
    ) as b
  );
END
```
