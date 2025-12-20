create database churn_db;
use churn_db;
show tables;
rename table churn_db.`customer-churn` to customer_churn;
select * From customer_churn limit 5;

-- 1] Total Customers--
select count(*) as total_customers 
from customer_churn;

-- 2] How Many Customers Churned--
select churn, count(*) as count
from customer_churn
group by churn; 

-- 3] Churn Percentage--
select churn, 
round(count(*) * 100.0 / (select count(*) from customer_churn),2) as churn_percentage
from customer_churn
group by churn;   

-- 4] Check missing TotalCharges--
select count(*)
from customer_churn
where TotalCharges is null or TotalCharges = '' ;

-- 5] Churn by Contract Type--
select
	Contract,
    count(*) as total_customers,
    sum(case when churn = 'Yes' then 1 else 0 end) as churned_customers,
    round(
		sum(case when churn = 'Yes' then 1 else 0 end) * 100.0 / count(*),
        2
	) as churn_percentage
from customer_churn
group by Contract
order by churn_percentage desc;

-- 6] Churn by Payment Method-- 
select
	PaymentMethod,
    count(*) as total_customers,
    round(
		sum(case when churn = 'Yes' then 1 else 0 end) * 100.0 / count(*),
        2
	) as churn_percentage
from customer_churn
group by PaymentMethod
order by churn_percentage desc;

-- 7] Tenure vs Churn (Critical Insight)--
select
	case
		when tenure <= 12 then '0-12 months'
        when tenure <= 24 then '13-24 months'
        when tenure <= 48 then '25-48 months'
        else '49+ months'
	end as tenure_group,
    count(*) as total_customers,
    round(
		sum(case when churn = 'Yes' then 1 else 0 end) * 100.0 / count(*),
        2
	) as churn_percentage
from customer_churn
group by tenure_group
order by churn_percentage desc;







  