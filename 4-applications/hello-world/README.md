```bash
docker build -t myapi:0.0.1 .
docker run -p 8080:8080 --rm myapi:0.0.1
```



```bash
curl -w "dns_resolution: %{time_namelookup}, tcp_established: %{time_connect}, ssl_handshake_done: %{time_appconnect}, TTFB: %{time_starttransfer}\n" -o /dev/null -s "http://localhost:8080/"
dns_resolution: 0.067, tcp_established: 0.175, ssl_handshake_done: 0.598, TTFB: 0.708
```

```bash
AWS_PROFILE=acloudguru2 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 851725381160.dkr.ecr.us-east-1.amazonaws.com/myapp
```

```bash
docker tag myapi:0.0.1 851725381160.dkr.ecr.us-east-1.amazonaws.com/myapp:0.0.1
```

```bash
docker push 851725381160.dkr.ecr.us-east-1.amazonaws.com/myapp:0.0.1
```

```bash
kubectl apply -f ./deploy.yaml
```

```bash
kubectl get pod my-deployment-7f7ff984f5-6grj9 -o jsonpath={.status.hostIP}
```

Add inbound security group to allow access via port 32410
```note
 curl -v 3.84.122.74:32410  
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