import { createClient, print } from "redis";

const redis = createClient();

redis.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redis.on("connect", () => {
  console.log("Redis client connected to the server");
});

redis.hset("HolbertonSchools", "Portland", 50, print);
redis.hset("HolbertonSchools", "Seattle", 80, print);
redis.hset("HolbertonSchools", "New York", 20, print);
redis.hset("HolbertonSchools", "Bogota", 20, print);
redis.hset("HolbertonSchools", "Cali", 40, print);
redis.hset("HolbertonSchools", "Paris", 2, print);

redis.hgetall("HolbertonSchools", console.log);
