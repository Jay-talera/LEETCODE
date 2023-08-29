select s1.score, (select count(distinct score) from scores s2 where s2.score >= s1.score) as "rank" from scores s1
order by s1.score DESC;

#pls upvote if you find solution easy to understand..Thanks..!!