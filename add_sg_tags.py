import boto3
from botocore.exceptions import ClientError
def get_sg_rules(sg_id):
    client = boto3.client('ec2')
    response = client.describe_security_group_rules(
    Filters=[
        {
            'Name': 'group-id',
            'Values': sg_id
        }
    ],
    )
    
    return response

if __name__ == "__main__":
    sg_list = ["XXX", "XXX"]
    for sg_rule in get_sg_rules(sg_list)['SecurityGroupRules']:
        try:
            client = boto3.client('ec2')
            response = client.create_tags(
            DryRun=False,
            Resources=[
                sg_rule['SecurityGroupRuleId'],
            ],
            Tags=[
                {
                    'Key': 'dateAdded',
                    'Value': '2022-11-05'
                },
            ]
        )
        except ClientError as e:
            print(e)