import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError
def return_today():
    now = datetime.now()
    return now
def get_sg_rules(sg_id, old_date):
    client = boto3.client('ec2')
    response = client.describe_security_group_rules(
    Filters=[
        {
            'Name': 'group-id',
            'Values': sg_id
        },
        {
            'Name': 'tag:dateAdded',
            'Values': [old_date]
        }
    ],
    )
    
    return response

def lambda_handler(event, context):
    sg_list = ["XXX", "XXX"]
    old_date = datetime.strftime(return_today() - timedelta(days=30), "%Y-%m-%d")
    print(old_date)
    for sg_rule in get_sg_rules(sg_list, old_date)['SecurityGroupRules']:
        try:
            client = boto3.client("ec2")
            response = client.revoke_security_group_ingress(
                GroupId=sg_rule['GroupId'],
                SecurityGroupRuleIds=[sg_rule['SecurityGroupRuleId']]
                )
            print(response)
            print("Successfully deleted the rule")
        except ClientError as e:
            print(e)
            print("Failed to delete rule")