
### Create ECR

```bash
AWS_PROFILE=acloudguru2 aws ecr create-repository --repository-name pynproc  --region us-east-1 --tags '[{"Key":"env","Value":"dev"},{"Key":"team","Value":"9999"}]'
```


### Build images

```bash
docker build -t pynproc:0.0.3 .
docker run -p 8080:8080 --rm pynproc:0.0.3
```


```bash
curl -w "dns_resolution: %{time_namelookup}, tcp_established: %{time_connect}, ssl_handshake_done: %{time_appconnect}, TTFB: %{time_starttransfer}\n" -o /dev/null -s "http://54.208.159.100:32410"
dns_resolution: 0.067, tcp_established: 0.175, ssl_handshake_done: 0.598, TTFB: 0.708
```

```bash
AWS_PROFILE=acloudguru2 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 044737250745.dkr.ecr.us-east-1.amazonaws.com/pynproc
```

```bash
docker tag pynproc:0.0.3 044737250745.dkr.ecr.us-east-1.amazonaws.com/pynproc:0.0.3
```

```bash
docker push 044737250745.dkr.ecr.us-east-1.amazonaws.com/pynproc:0.0.3
```

```bash
kubectl apply -f ./deploy.yaml
```

```bash
kubectl get pod my-deployment-796c67dfc4-h2ch8 -o jsonpath={.status.hostIP}
```

Add inbound security group to allow access via port 32410
```note
 curl -v 54.208.159.100:32410  
*   Trying 3.84.122.74:32410...
* Connected to 3.84.122.74 (3.84.122.74) port 32410 (#0)
> GET / HTTP/1.1
> Host: 3.84.122.74:32410
> User-Agent: curl/8.1.2
> Accept: */*
> 
< HTTP/1.1 200 OK
< date: Sat, 02 Mar 2024 07:55:06 GMT
< server: uvicorn
< content-length: 25
< content-type: application/json
< 
* Connection #0 to host 3.84.122.74 left intact
{"message":"Hello World"}%
```




