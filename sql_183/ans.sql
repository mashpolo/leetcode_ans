# 利用in的方法
select a.Name as Customers from Customers a where a.id not in (select CustomerId from Orders);

# 利用左联join, 判断左边值在右边为空的情况
select a.Name as Customers from Customers a left join Orders b on a.id = B.CustomerId where b.CustomerId is NULL;