# mtgrdb

```
sudo docker run -d --name psql -e POSTGRES_PASSWORD=secret -p 15432:5432 postgres
./generator.sh
PGPASSWORD=secret psql -h localhost -p 15432 -U postgres -f run.sql
```

```
sudo docker run -it --rm --link psql:psql -e PGPASSWORD=secret postgres pg_dump -h psql -p 5432 -U postgres > dump.sql
```

