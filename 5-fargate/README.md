
# Pre-requisites

## Install eskctl

### MacOs
```bash
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

### Linux
```shell
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```


## Create a namespace
e.g namespace: `myns`
```shell
kubectl create namespace myns
```

## Create fargate profile
```bash
AWS_REGION=us-east-1 eksctl create fargateprofile --cluster my-eks-cluster --name fargate-profile --namespace myns --labels fargate=enable
```

## Get profile
```bash
eksctl get fargateprofile --cluster my-eks-cluster -o yaml
```


## Test

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-web
  namespace: myns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-nginx-app
  template:
    metadata:
      labels:
        app: simple-nginx-app
        fargate: enable
    spec:
      containers:
        - name: nginx
          image: nginx
```


## Resources
https://www.eksworkshop.com/docs/fundamentals/fargate/enabling/


### ISSUE
Fargate will use the security group of the cluster -> therefore need to add inbound rule to accept traffic from other pods
https://github.com/aws/containers-roadmap/issues/625
Add to the security group created by eksctl
e.g `sg-03348403a2258ffdd - eks-cluster-sg-my-eks-cluster-735157785`