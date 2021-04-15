import coconut

class Client:

  def __init__(self, api_key=None, region=None, endpoint=None):
    self.api_key = api_key
    self._region = region
    self._endpoint = endpoint

  def endpoint(self):
    # if endpoint set, we return it
    if self._endpoint:
      return self._endpoint

    # if no endpoint but region is given, we
    # build the endpoint following https://api-region.coconut.co/v2
    if self._region:
      return 'https://api-' + self._region + '.coconut.co/v2'

    # by default:
    return coconut.ENDPOINT

  @classmethod
  def default(self):
   return Client(coconut.api_key, coconut.region, coconut.endpoint)