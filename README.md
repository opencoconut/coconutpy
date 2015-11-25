# Python client Library for encoding Videos with HeyWatch

## Install

``` language-console
sudo easy_install heywatch_api
```

## Submitting the job

Use the [API Request Builder](https://app.heywatch.com/job/new) to generate a config file that match your specific workflow.

Example of `heywatch.conf`:

``` language-hw
var s3 = s3://accesskey:secretkey@mybucket

set webhook = http://mysite.com/webhook/heywatch?videoId=$vid

-> mp4  = $s3/videos/$vid.mp4
-> webm = $s3/videos/$vid.webm
-> jpg_300x = $s3/previews/thumbs_#num#.jpg, number=3
```

Here is the ruby code to submit the config file:

``` language-python
import heywatch
from heywatch import job

job = heywatch.job.create(
  api_key='k-api-key',
  conf='heywatch.conf',
  source='http://yoursite.com/media/video.mp4',
  vars={'vid': 1234}
)

if job['status'] == 'ok':
  print job['id']
else:
  print job['error_code']
  print job['error_message']
```

Note that you can use the environment variable `HEYWATCH_API_KEY` to set your API key.

*Released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).*

---

* HeyWatch website: http://www.heywatchencoding.com
* API documentation: http://www.heywatchencoding.com/docs
* Github: http://github.com/heywatch/heywatch_api-ruby
* Contact: [support@heywatch.com](mailto:support@heywatch.com)
* Twitter: [@heywatch](http://twitter.com/heywatch) / [@sadikzzz](http://twitter.com/sadikzzz)