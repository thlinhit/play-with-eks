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