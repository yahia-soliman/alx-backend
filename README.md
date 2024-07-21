# ALX Software Engineering
The ALX Software Engineering program follows a project-based learning model
in which learners work on a series of increasingly complex projects,
starting with simple ones and progressing to more advanced ones as they gain experience and proficiency.


# Back end
The last 3 months of the 1 year program was focused on backend.

In this repo we will discuss some topics in back-end and solve some problems

## Pagination
When you are sending a list of items across HTTP, at some point you will have a huge number of data, sending a huge list of data will cause expensive heavy network traffic and will cause latency


## Limit & Offset paging
this is the simplest form of paging it is **limiting** the list to specific number and starting form specific index `offset`

`GET /items?limit=20&offset=100` would translated to:
```sql
SELECT * FROM items ORDER BY id LIMIT 20 OFFSET 100;
```


