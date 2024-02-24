
## How to deploy to aws profile

### ACloudGuru
```bash
aws configure --profile acloudguru2
```

```bash
AWS_PROFILE=acloudguru2 sls deploy
```

### Deploy each component
```bash
AWS_PROFILE=acloudguru2 sls vpc:deploy
```

```bash
AWS_PROFILE=acloudguru2 sls eks:deploy
```

### Get Iam
```bash
EKS_VERSION=1.26
AWS_PROFILE=acloudguru2 aws ssm get-parameter --name /aws/service/eks/optimized-ami/$EKS_VERSION/amazon-linux-2/recommended/image_id --region us-east-1 --query "Parameter.Value" --output text;
```

----
# After deploying EKS Cluster
### Update Kube config
As soon as Kubernetes cluster deployment finishes, we need to create ~/.kube/config file, with the following command (please, use the latest awscli):
```bash
AWS_PROFILE=acloudguru2 aws eks update-kubeconfig --region us-east-1 --name thlinh-eks-local-eks
```
* `thlinh-eks-local-eks` is the cluster name
**ATTENTION**: if you can not connect to the cluster please double-check the ip address in KubernetesClusterMasterFromWorkstationSecurityGroupRule section of serverless.yml

### Install ConfigMap
```bash
AWS_PROFILE=acloudguru2 sls info --verbose 
```
Retrieve: `KubernetesClusterNodesRoleArn`

```bash
curl -O https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-08-30/aws-auth-cm.yaml
```
Replace nodearn in the file by the value of `KubernetesClusterNodesRoleArn`
```bash
kubectl apply -f aws-auth-cm.yaml && rm aws-auth-cm.yaml
```
