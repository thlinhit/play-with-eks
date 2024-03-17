
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
AWS_PROFILE=acloudguru2 AWS_REGION=us-east-1 eksctl create fargateprofile --cluster my-eks-cluster --name fargate --namespace myns
```



## Resources
https://www.eksworkshop.com/docs/fundamentals/fargate/enabling/