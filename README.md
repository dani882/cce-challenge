# CCE Code Challenge

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders:

- functions - Code for the application's Lambda functions to manipulate json objects
- template.yaml - A template that defines the application's AWS resources.

This application creates a serverless infrastructure to handle events on S3 when new json files are uploaded and persisted it to the DynamoDB Table called `Brands`.

## Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local)
### Build Your Application

When you make a change to the code, you can run the following command to install dependencies
and convert your Lambda function source code into an artifact that can be deployed and run on Lambda.

```bash
sam build
```

## Use the SAM CLI to build locally

Build the Lambda functions in your application with the `sam build --use-container` command.

```bash
sam build --use-container
```

The SAM CLI installs dependencies defined in `functions/*/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.


## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name [stack-name]
```
