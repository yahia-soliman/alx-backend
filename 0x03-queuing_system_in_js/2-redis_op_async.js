import { createClient } from "redis";
import { promisify } from "util";

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

async function displaySchoolValue(schoolName) {
  redis.get(schoolName, (_, reply) => console.log(reply));
}

promisify(displaySchoolValue);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
