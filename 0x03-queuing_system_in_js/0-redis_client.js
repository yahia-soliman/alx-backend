import { createClient } from "redis";

const redis = createClient()

redis.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redis.on("connect", () => {
  console.log("Redis client connected to the server");
});
