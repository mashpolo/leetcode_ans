select a.Name as Employee from Employee a, Employee b where a.ManagerId = b.Id and a.Salary > b.Salary

# 使用内联join
select a.Name as Employee from Employee a inner join Employee b on a.ManagerId = b.Id and a.Salary > b.Salary;