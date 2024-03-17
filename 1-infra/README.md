
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

```bash
AWS_PROFILE=acloudguru2 sls eks-workers:deploy
```

```bash
AWS_PROFILE=acloudguru2 sls bastion:deploy
```

```bash
AWS_PROFILE=acloudguru2 sls nat:deploy
```

### Get Iam
```bash
EKS_VERSION=1.26
AWS_PROFILE=acloudguru2 aws ssm get-parameter --name /aws/service/eks/optimized-ami/$EKS_VERSION/amazon-linux-2-arm64/recommended/image_id --region us-east-1 --query "Parameter.Value" --output text;
```

----
# After deploying EKS Cluster (If Private EKS, need to access a node in private subnet and do the following things)

### Download kubectl (Private only - use X86 - ARM has issue)
```shell
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod 755 kubectl
sudo mv ~/kubectl /usr/local/bin
```
https://kubernetes.io/releases/

upload to s3 and then download from s3 in node
```shell
AWS_PROFILE=acloudguru2 aws s3 cp kubectl s3://thlinh-mys3/kubectl
```
```shell
aws s3 cp ${KubectlS3Location} /tmp/kubectl --region ${AWS::Region}
chmod 755 /tmp/kubectl
```


### Update Kube config
As soon as Kubernetes cluster deployment finishes, we need to create ~/.kube/config file, with the following command (please, use the latest awscli):
```bash
AWS_PROFILE=acloudguru2 aws eks update-kubeconfig --region us-east-1 --name my-eks-cluster
```
* `thlinh-eks-local-eks` is the cluster name
**ATTENTION**: if you can not connect to the cluster please double-check the ip address in KubernetesClusterMasterFromWorkstationSecurityGroupRule section of serverless.yml

### Install ConfigMap
```bash
AWS_PROFILE=acloudguru2 sls info --verbose 
```
Get Arn of role "NodeInstanceRole" or
Retrieve: `KubernetesClusterNodesRoleArn`

```bash
curl -O https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-08-30/aws-auth-cm.yaml
```
Replace nodearn in the file by the value of `KubernetesClusterNodesRoleArn`
```bash
kubectl apply -f aws-auth-cm.yaml && rm aws-auth-cm.yaml
```


---
## Verify
```bash
kubectl get nodes --watch
```

```bash
kubectl get pod --all-namespaces
```


---
## Copy Kubectl
```bash
aws s3 cp s3://thlinh-mys3/kubectl /tmp/kubectl --region us-east-1
chmod 755 /tmp/kubectl
```