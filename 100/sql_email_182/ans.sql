select distinct a.Email from Person a, Person b where a.Email = b.Email and a.Id != b.Id;

# 利用group by 和 having来达到同样的结果(having主要使用在where语句无法计算的环境中)
select distinct Email from Person group by Email having count(Email) > 1;