import kue from "kue";
import { expect } from "chai";

import createPushNotificationsJobs from "./8-job.js";

const queue = kue.createQueue();

describe("push notifications", () => {
  before(() => {
    queue.testMode.enter();
  });
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it("throw error when message is not an array", () => {
    expect(createPushNotificationsJobs)
      .to.throw("Jobs is not an array")
      .with(123, queue);
  });
});
