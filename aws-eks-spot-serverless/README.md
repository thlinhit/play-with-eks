## How to deploy to aws profile

### ACloudGuru
```bash
aws configure --profile acloudguru
```


```bash
AWS_PROFILE=acloudguru sls deploy
```

### Deploy product

#### Deploy custom domain
```bash
AWS_PROFILE=stag sls create_domain --stage=dev
```

#### Test
```bash
AWS_PROFILE=acloudguru sls products:deploy
```

#### DEV
```bash
AWS_PROFILE=stag sls products:deploy --stage=dev
```


# After deploying EKS Cluster
### Update Kube config
As soon as Kubernetes cluster deployment finishes, we need to create ~/.kube/config file, with the following command (please, use the latest awscli):
```bash
AWS_PROFILE=acloudguru aws eks update-kubeconfig --region us-east-1 --name aws-eks-spot-serverless-dev
```

**ATTENTION**: if you can not connect to the cluster please double check the ip address in KubernetesClusterMasterFromWorkstationSecurityGroupRule section of serverless.yml