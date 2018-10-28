# 删除重复的电子邮箱

> 编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id 是这个表的主键。
例如，在运行你的查询语句之后，上面的 Person 表应返回以下几行:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

## 解决思路：
1. 不能一边查询一边修改同一个表，需要将表中查询的数据先做成一个临时表，再来删除

```bash
delete from  Person where Id not in (select Id from (select min(id) id from Person group by email) p);

# select from Person where Id not in (select min(id) from Person group by email);
```


# 上升的温度

> 给定一个 Weather 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。

```
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
例如，根据上述给定的 Weather 表格，返回如下 Id:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
```

## 解决思路:
1. 利用sql的date相关函数来解决

```bash
select w1.Id from Weather w1, Weather w2 where w1.Temperature>w2.Temperature and TO_DAYS(w1.RecordDate)-TO_DAYS(w2.RecordDate)=1;
```
