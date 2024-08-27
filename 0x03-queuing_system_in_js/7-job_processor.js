import kue from "kue";

const blacklist = ["4153518780", "4153518781"];

function sendNotification(job, done) {
  const { phoneNumber, message } = job.data;
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`,
  );
  done();
}

const q = kue.createQueue();
q.process("push_notification_code_2", sendNotification);
