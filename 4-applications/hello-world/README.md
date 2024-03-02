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