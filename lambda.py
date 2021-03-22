from __future__ import print_function
import json
import boto3
import constants
import os
import commonutil
print('Loading function')




logger = commonutils.get_logger()
sns = boto3.client(constants.AWS_SNS, os.getenv(constants.AWS_REGION, constants.AWS_DEFAULT_REGION))

        def lambda_handler(event, context):
        #print("Received event: " + json.dumps(event, indent=2))
        message = event['Records'][0]['Sns']['Message']
        print("From SNS: " + message)
        return message

        def send_error(error, event, context):
            message = _get_message(error, event, context)
            logger.info("Sending error message as {}".format(message))
            response = sns.publish(
            TopicArn=os.getenv(constants.SNS_ERROR_ARN),
            Subject=constants.DEPOSIT_SNS_SUBJECT,
            Message=message,
            )
    
        def publish_message(self, complete_record):

        try:
            response = self.sns_client.publish(
                TopicArn=self.sns_topic_name,    
                Message=json.dumps(complete_record),
                MessageStructure = "string"
            )

        except Exception as ex:
            logger.error("**Function : SNS.publish_message() " + 
                        " **Error Type : " + str(type(ex).__name__) + 
                        " **Error Description : " + str(ex))
            return False
        return True
