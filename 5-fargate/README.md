
## Pre-requisites

### Install eskctl
```bash
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```


## 
```bash
kubectl create namespace fargate-workload
```

```bash
AWS_PROFILE=acloudguru2 AWS_REGION=us-east-1 eksctl create fargateprofile --cluster thlinh-eks-local-eks --name fargate --namespace fargate-workload
```



## Resources
https://www.eksworkshop.com/docs/fundamentals/fargate/enabling/