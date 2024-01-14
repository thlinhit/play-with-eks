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
* `aws-eks-spot-serverless-dev` is the cluster name
**ATTENTION**: if you can not connect to the cluster please double-check the ip address in KubernetesClusterMasterFromWorkstationSecurityGroupRule section of serverless.yml

### Install ConfigMap
```bash
AWS_PROFILE=acloudguru sls info --verbose 
```
Retrieve: `KubernetesClusterNodesRoleArn`

```bash
curl -O https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-08-30/aws-auth-cm.yaml
```
Replace nodearn in the file by the value of `KubernetesClusterNodesRoleArn`
```bash
kubectl apply -f aws-auth-cm.yaml && rm aws-auth-cm.yaml
```



### Get Iam
```bash
AWS_PROFILE=acloudguru aws ssm get-parameter --name /aws/service/eks/optimized-ami/1.25/amazon-linux-2/recommended/image_id --region us-east-1 --query "Parameter.Value" --output text;
```