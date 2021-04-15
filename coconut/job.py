import coconut
from coconut import api

class Job:
  @classmethod
  def apply_settings(self, job):
    if coconut.storage is not None:
      if job.get('storage') is None:
        job['storage'] = {}

      job['storage'].update(coconut.storage)

    if coconut.notification is not None:
      if job.get('notification') is None:
        job['notification'] = {}

      job['notification'].update(coconut.notification)

    return job

  @classmethod
  def retrieve(self, job_id, **kwargs):
    return api.request('GET', '/jobs/' + job_id, **kwargs)

  @classmethod
  def create(self, job, **kwargs):
    return api.request('POST', '/jobs', json=self.apply_settings(job), **kwargs)