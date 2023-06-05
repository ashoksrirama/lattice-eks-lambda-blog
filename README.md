# lattice-eks-lambda-blog
VPC Lattice Integration with Amazon EKS &amp; AWS Lambda

## Create a Service Network

* Login to your `Central Networking Account`
* Create a CloudWatch log group to store the VPC Lattice Service Network logs

```shell
aws logs create-log-group --log-group-name lattice-demo-logs
# Export CW Log Group Name
export LOG_GROUP_ARN=$(aws logs describe-log-groups --log-group-name-prefix lattice-demo-logs --output text --query 'logGroups[0].arn')
```

* Create a Service Network

```shell
export LATTICE_ARN = $(aws vpc-lattice create-service-network --name lattice-demo --query 'arn' --output text)
# Create Access log Subscription
aws vpc-lattice create-access-log-subscription --resource-identifier $LATTICE_ARN --destination-arn $LOG_GROUP_ARN
```

* Share the Service Network with EKS & Lambda AWS Accounts

```shell
aws ram create-resource-share --name lattice-demo-sn --resource-arns $LATTICE_ARN --principals 883432218968 259394127454
```