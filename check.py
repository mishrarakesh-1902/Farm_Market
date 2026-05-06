import urllib.request, urllib.error
try:
  resp = urllib.request.urlopen('http://127.0.0.1:8000/')
  print('Status:', resp.status)
except urllib.error.HTTPError as e:
  print('HTTPError:', e.code)
  print(e.read().decode('utf-8'))
except Exception as e:
  print('Error:', e)
