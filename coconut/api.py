import json
import os
import httplib2
import base64

import coconut
from coconut.client import Client
from coconut.error import CoconutError
from coconut import version

def get_authorization_header(api_key):
  if api_key is None:
    raise ValueError('API key must be specified using coconut.api_key=')

  api_key = api_key + ":"
  data_bytes = api_key.encode("utf-8")
  return 'Basic ' + base64.b64encode(data_bytes).decode("utf-8")

def user_agent():
  return "Coconut/v2 PythonBindings/"# VERSION

def request(verb, path, **kwargs):
  h = httplib2.Http()
  cli = kwargs.get('client') or Client.default()

  headers = {'User-Agent': user_agent(), 'Content-Type': 'application/json', 'Accept': 'application/json'}
  headers['Authorization'] = get_authorization_header(cli.api_key)

  if verb == 'POST':
    body = json.dumps(kwargs.get('json'))
  else:
    body = None

  response, content = h.request(cli.endpoint() + path, verb, body=body, headers=headers)

  if response.status > 399:
    if response.status == 400 or response.status == 401:
      err = json.loads(content.decode('utf-8'))
      raise CoconutError(err["message"] + " (code=" + err["error_code"] + ")")
    else:
      raise CoconutError("Server returned HTTP status " + str(response.status) + ".")


  return json.loads(content.decode('utf-8'))
