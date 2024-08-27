import kue from "kue";
import { expect } from "chai";

import createPushNotificationsJobs from "./8-job.js";

const queue = kue.createQueue();
const jobs = [
  { phoneNumber: "123", message: "hello" },
  { phoneNumber: "456", message: "bye bye" },
];

describe("createPushNotificationsJobs:", () => {
  before(() => {
    queue.testMode.enter();
    createPushNotificationsJobs(jobs, queue);
  });
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it("throws error when message is not an array", () => {
    const fn = () => createPushNotificationsJobs("not an array", queue);
    expect(fn).to.throw("Jobs is not an array");
  });

  it("creates a job queue with correct length", () => {
    expect(queue.testMode.jobs.length).to.equal(jobs.length);
  });

  it("jobs has the correct type", () => {
    queue.testMode.jobs.forEach((job) => {
      expect(job.type).to.equal("push_notification_code_3");
    });
  });
});
