import coconut
from coconut import api

class Metadata:
  @classmethod
  def retrieve(self, job_id, **kwargs):
    key = kwargs.pop('key', None) or ""
    return api.request('GET', '/metadata/jobs/' + job_id + '/' + key, **kwargs)