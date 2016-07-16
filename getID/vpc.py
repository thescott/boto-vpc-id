import boto3

ec2 = boto3.resource ('ec2', region_name='us-east-1')

filters = [{'Name':'tag:Name', 'Values':['Default']}]
Default = list(ec2.vpcs.filter(Filters=filters))[0]
Default.vpc_id

print (Default.vpc_id)