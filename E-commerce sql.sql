use [E-commerce];

--Total customer per segment
select segment,count(*) as count
From [RFM.New]
group by segment;

---Find Best Customer
select customer_id,Monetary
from [RFM.New] where segment='Regular Customer'
order by Monetary Desc;

select Distinct segment From [RFM.New];

--Total Revenue
select sum(Monetary) as total_revenue
from [RFM.New];