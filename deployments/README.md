

```bash
kubectl get pods --all-namespaces
```


## Install Ingress Controller

https://github.com/kubernetes/ingress-nginx
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.5/deploy/static/provider/cloud/deploy.yaml
```

Get external ip
```bash
kubectl get service ingress-nginx-controller --namespace=ingress-nginx
```