
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

