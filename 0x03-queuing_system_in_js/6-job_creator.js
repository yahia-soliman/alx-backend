import kue from "kue";

const q = kue.createQueue();

const job = q.create("push_notification_code", {
  phoneNumber: "123",
  message: "hi there",
}).save();


job.on("enqueue", () => console.log(`Notification job created: ${job.id}`));
job.on("complete", () => console.log("Notification job completed"));
job.on("failed", () => console.log("Notification job failed"));
