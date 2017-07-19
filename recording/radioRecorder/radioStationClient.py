import requests

print '== POST =='
attrs = {'url':'http://streaming.radionomy.com/Cheche-International-Radio', 'title':'Title 4 One Here'}
r = requests.post('http://localhost:5000/add', data=attrs)
print r
print r.text
print '== GET =='
r = requests.get('http://localhost:5000/get-info')
print r
print r.text
