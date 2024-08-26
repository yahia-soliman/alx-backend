import { createClient } from "redis";

const redis = createClient()

redis.subscribe("holberton school channel");

redis.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redis.on("connect", () => {
  console.log("Redis client connected to the server");
});

redis.on("message", (channel, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    redis.unsubscribe(channel);
    process.exit();
  }
});
