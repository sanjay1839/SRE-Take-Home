
#!/bin/bash

# Using this template please create a bash script that would accept the name of the stack as a first parameter and then execute the following command
aws cloudformation create-change-set \ --stack-name sre-take-home \
    --change-set-name my-change-set \
    --template-body file://cloudformation.json \
    --capabilities CAPABILITY_IAM
