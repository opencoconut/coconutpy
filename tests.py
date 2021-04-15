import unittest
import os
import time

import coconut
from coconut.client import Client
from coconut.job import Job
from coconut.metadata import Metadata

class CoconutTestCase(unittest.TestCase):

  INPUT_URL = "https://s3-eu-west-1.amazonaws.com/files.coconut.co/bbb_800k.mp4"

  def setUp(self):
    coconut.api_key = os.getenv("COCONUT_API_KEY")
    coconut.endpoint = os.getenv("COCONUT_ENDPOINT")

    coconut.storage = {
      "service": "s3",
      "region": os.getenv("AWS_REGION"),
      "credentials": { "access_key_id": os.getenv("AWS_ACCESS_KEY_ID"), "secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY") },
      "bucket": os.getenv("AWS_BUCKET"),
      "path": "/coconutrb/tests/"
    }

    coconut.notification = {
      "type": "http",
      "url": os.getenv("COCONUT_WEBHOOK_URL")
    }

  def create_job(self, j={}, **kwargs):
    job = {
      "input": { "url": self.INPUT_URL },
      "outputs": {
       "mp4": { "path": "/test_create_job.mp4", "duration": 1 }
      }
    }
    job.update(j)

    return Job.create(job, **kwargs)

  def test_coconut_api_key(self):
    coconut.api_key = "apikey"
    self.assertEqual("apikey", coconut.api_key)

  def test_coconut_region(self):
    coconut.region = "us-east-1"
    self.assertEqual("us-east-1", coconut.region)

  def test_overwrite_endpoint(self):
    myendpoint = "https://coconut-private/v2"
    coconut.endpoint = myendpoint

    self.assertEqual(myendpoint, coconut.endpoint)

  def test_create_job(self):
    job = self.create_job()
    self.assertTrue(isinstance(job, dict))
    self.assertIsNotNone(job["id"])
    self.assertEqual("job.starting", job["status"])

  def test_retrieve_job(self):
    job = Job.retrieve(self.create_job()["id"])
    self.assertTrue(isinstance(job, dict))
    self.assertIsNotNone(job["id"])
    self.assertEqual("job.starting", job["status"])


  def test_retrieve_metadata(self):
    job = self.create_job()
    time.sleep(10)

    md = Metadata.retrieve(job["id"])
    self.assertTrue(isinstance(md, dict))
    self.assertIsNotNone(md["metadata"]["input"])


if __name__ == '__main__':
    unittest.main()