.header on
.mode column
.width 40 10

-- Find the most rated movie
with T as (
	select movieId, count(*) as c
	from ratings
	group by movieId
)
select name, c
from T join movies on T.movieId = movies.id
order by c desc
limit 10;

select "Another query";

with T as (
	select movieId, avg(rating) as r, count(*) as c
	from ratings
	group by movieId
)
select name, r, c
from T join movies on T.movieId = movies.id
order by r desc, c desc
limit 100;


