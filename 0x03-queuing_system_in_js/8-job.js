/**
 * Insert Notifications in a job queue
 *
 * @param {object[]} jobs
 * @param {import("kue").Queue} queue
 */
export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw new Error("Jobs is not an array");
  jobs.forEach((item) => {
    const job = queue.createJob("push_notification_code_3", item);

    job.on("enqueue", () => console.log(`Notification job created: ${job.id}`));
    job.on("complete", () =>
      console.log(`Notification job #${job.id} completed`),
    );
    job.on("failed", (err) =>
      console.log(`Notification job #${job.id} failed: ${err}`),
    );
    job.on("progress", (percent) =>
      console.log(`Notification job #${job.id} ${percent}% complete`),
    );
    job.save();
  });
}
