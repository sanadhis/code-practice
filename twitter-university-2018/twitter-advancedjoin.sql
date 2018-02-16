select ROUND(sum(t1.TIV_2012),2) 
from INSURANCE t1, 
(select TIV_2011 from INSURANCE group by TIV_2011 having count(*)>1) t2, 
(select LAT,LON from INSURANCE group by LAT,LON having count(*) = 1) t3 
where t1.TIV_2011 = t2.TIV_2011 and (t1.LAT = t3.LAT and t1.LON = t3.LON)
