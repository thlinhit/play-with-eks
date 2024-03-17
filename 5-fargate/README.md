
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
eksctl create fargateprofile --cluster my-eks-cluster --name fargate-profile --namespace myns --labels fargate=enable
```



## Resources
https://www.eksworkshop.com/docs/fundamentals/fargate/enabling/