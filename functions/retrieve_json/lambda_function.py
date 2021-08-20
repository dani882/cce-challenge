import boto3
import logging
import json
from urllib.parse import unquote_plus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb_client = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    logger.info(event)
    
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    logger.info('Reading from {}'.format(bucket))
    
    #  Get the file/key name
    key = event['Records'][0]['s3']['object']['key']
    logger.info('File name {}'.format(key))

    try:
        #  Fetch the file from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        
        #  Deserialize the file's content
        jsonFileReader = response["Body"].read().decode()
        jsonDict = json.loads(jsonFileReader)
        
        # Use Brands table
        table = dynamodb_client.Table('Brands')
        
        #  Loop the car brands
        brands = jsonDict['brands']
        for records in brands:

            # Add items to table
            table.put_item(Item={
                'id': records['id'],
                'name': records['name'],
            })

    except Exception as e:
        logger.error(e)
        logger.error('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
