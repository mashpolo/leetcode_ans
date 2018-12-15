# 620
> 考察mysql中的数学运算

```
select * from cinema where description !='boring' and id%2!=0 order by rating desc
```


# 627
> 考察mysql中的逻辑查询

```mysql
update salary set sex=IF(sex='m','f', 'm')
```
