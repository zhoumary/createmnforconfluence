# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://confluence.itc.sap.com.atlassian.net/wiki/rest/api/content"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps(
{
  "id": "<string>",
  "title": "<string>",
  "type": "page",
  "space": {
    "key": "<string>"
  },
  "status": "current",
  "ancestors": [
    {
      "id": "<string>"
    }
  ],
  "body": {
    "view": {
      "value": "<string>",
      "representation": "view"
    },
    "export_view": {
      "value": "<string>",
      "representation": "view"
    },
    "styled_view": {
      "value": "<string>",
      "representation": "view"
    },
    "storage": {
      "value": "<string>",
      "representation": "view"
    },
    "editor2": {
      "value": "<string>",
      "representation": "view"
    },
    "anonymous_export_view": {
      "value": "<string>",
      "representation": "view"
    }
  }
}
)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))