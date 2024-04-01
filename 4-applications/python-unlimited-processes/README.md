
### Create ECR

```bash
AWS_PROFILE=acloudguru2 aws ecr create-repository --repository-name pynproc  --region us-east-1 --tags '[{"Key":"env","Value":"dev"},{"Key":"team","Value":"9999"}]'
```


### Build images

```bash
docker build -t pynproc:0.0.8 .
```
```bash
docker run -p 8080:8080 --rm pynproc:0.0.8
```
:

```bash
curl -w "dns_resolution: %{time_namelookup}, tcp_established: %{time_connect}, ssl_handshake_done: %{time_appconnect}, TTFB: %{time_starttransfer}\n" -o /dev/null -s "http://54.208.159.100:32410"
dns_resolution: 0.067, tcp_established: 0.175, ssl_handshake_done: 0.598, TTFB: 0.708
```

```bash
AWS_PROFILE=acloudguru2 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 851725166193.dkr.ecr.us-east-1.amazonaws.com/pynproc
```

```bash
docker tag pynproc:0.0.8 851725166193.dkr.ecr.us-east-1.amazonaws.com/pynproc:0.0.8
```

```bash
docker push 851725166193.dkr.ecr.us-east-1.amazonaws.com/pynproc:0.0.8
```

```bash
kubectl apply -f ./deploy.yaml
```

```bash
kubectl get pod pynproc-74df4dc577-72b86 -o jsonpath={.status.hostIP}
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


```bash
kubectl -nmyns exec -it pynproc-576bc4578b-j79lf -- /bin/bash
```




check hard limit
```shell
ulimit -a -H
```

Adjusting limits within a container, however, requires privileges not available to the application inside the Docker container and must be done as parameters to the docker run command.
refs: https://towardsaws.com/how-to-configuring-linux-ulimit-with-docker-and-aws-ecs-599c71f00473