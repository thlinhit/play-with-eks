```bash
docker build -t myapi:0.0.1 .
docker run -p 8080:8080 --rm myapi:0.0.1
```



```bash
curl -w "dns_resolution: %{time_namelookup}, tcp_established: %{time_connect}, ssl_handshake_done: %{time_appconnect}, TTFB: %{time_starttransfer}\n" -o /dev/null -s "http://54.208.159.100:32410"
dns_resolution: 0.067, tcp_established: 0.175, ssl_handshake_done: 0.598, TTFB: 0.708
```

```bash
AWS_PROFILE=acloudguru2 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 992382721649.dkr.ecr.us-east-1.amazonaws.com/myapp
```

```bash
docker tag myapi:0.0.1 992382721649.dkr.ecr.us-east-1.amazonaws.com/myapp:0.0.1
```

```bash
docker push 992382721649.dkr.ecr.us-east-1.amazonaws.com/myapp:0.0.1
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




## PRIVAGTE
```shell
kubectl -nmyns run mycurlpod --image=curlimages/curl -i --tty -- sh
kubectl exec -i --tty mycurlpod -- sh
```
https://www.tutorialworks.com/kubernetes-curl/

```shell
kubectl -nmyns exec mycurlpod -- curl -v http://10-90-73-186.fastapi-dev.myns.svc.cluster.local:8080
kubectl -nmyns exec mycurlpod -- nslookup 10.90.73.177
```


### On EC2 Node
```shell
kubectl get endpoints fastapi-dev -nmyns

NAME          ENDPOINTS           AGE
fastapi-dev   10.90.73.186:8080   16m
```
curl via nodePort 8080
```shell
kubectl -nmyns exec mycurlpod -- curl -v 10.90.73.186:8080
kubectl -nmyns exec mycurlpod -- curl -v 10-90-78-104.fastapi-dev.myns.svc.cluster.local:8080
```
