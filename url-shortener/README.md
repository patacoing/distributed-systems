# Distributed url shortener

## Purpose : 

Build a distributed url shortener.

## Requirements :

- Ability to serve 11600 reads/s
- Ability to serve 1160 writes/s

## Id

To generate a unique id among the the instances, we used the twitter snowflake approach.

## Url shortening

We use the generated id and convert it to base62 in order to get the shortened url.

## Load balancing

In order to serve http requests to the applications instances, we set up
a load balancer. We used Nginx.

## Availability

We set up a Redis cluster as caching layer to faster read operations.

## Execution

```bash
docker compose up -d --build
```

## Performance test

We used Apache Jmeter in order to execute a load testing. You can use the `loading_test.jmx` file