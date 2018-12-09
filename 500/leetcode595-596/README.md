# sql集锦

## 595
> 主要是考察了mysql中的or的用法

```sql
select name, population, area from World where area > 3000000 or population > 25000000;
```

## 596
> 考察了group by 和having的用法。
> 这里注意一点的是，需要注意不能有重复的学生选课，所有需要加上distinct

```sql
select class from courses group by class having count(distinct student) >=5
```
