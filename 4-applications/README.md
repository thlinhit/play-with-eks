### Install a pod for executing curl purpose
```shell
kubectl -nmyns run mycurlpod --image=curlimages/curl -i --tty -- sh
kubectl -nmyns exec -i --tty mycurlpod -- sh
```
https://www.tutorialworks.com/kubernetes-curl/

```shell
kubectl -nmyns exec mycurlpod -- curl -v http://10-90-74-191.pynproc-dev.myns.svc.cluster.local:8080
kubectl -nmyns exec mycurlpod -- nslookup 10.90.73.177
```


### On EC2 Node
```shell
kubectl get endpoints pynproc-dev -nmyns

NAME          ENDPOINTS           AGE
fastapi-dev   10.90.73.186:8080   16m
```
curl via nodePort 8080
```shell
kubectl -nmyns exec mycurlpod -- curl -v 10.90.75.78:8080
kubectl -nmyns exec mycurlpod -- curl -v 10-90-77-89.pynproc-dev.myns.svc.cluster.local:8080
```
