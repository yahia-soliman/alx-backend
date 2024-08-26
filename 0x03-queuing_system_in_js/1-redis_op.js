import { createClient } from "redis";

const redis = createClient()

redis.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

redis.on("connect", () => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  redis.set(schoolName, value, (_, reply) => console.log(`Reply: ${reply}`));
}

function displaySchoolValue(schoolName) {
  redis.get(schoolName, (_, reply) => console.log(reply));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
