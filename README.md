# CCE Code Challenge
### Summary of options

For this assignment I decided to use serverless services with the possibility to deploy and destroy it whenever I want with no charge([Free Tier](https://aws.amazon.com/free/)).

I chose AWS API Gateway as the entry point for the requests. Then I thought would be good to someone that doesn't have aws account can also upload files, so I implement a Lambda to generate a signedURl with expiration. Then the user would be able to upload the file to an S3 Bucket.

The other part of the project consisted on persist the data just uploaded in the bucket, so I chose another Lambda to take that event, decode it and then using the sdk to connect to dynamodb put those items in the `Brands` table.

## Overview
The application starts when the user make a request the get the temporary URL to upload the file.

When request happen. A trigger to invoke a lambda function to get the signed url is executed. Once the function get the url from the s3 bucket, this is returned to the user in order to be able to upload the file.

Another event is triggered once the object with .json extension is uploaded to S3 bucket. It takes the json information, it's keys and values and persist it to the dynamodb Table



This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders:

  ## File Structure

|                |                          |
----------------|------------------------------------------------------------
|functions|Code for the application's Lambda functions to manipulate json objects       
|template.yaml |A template that defines the application's AWS resources.
|

This application creates a serverless infrastructure to handle events on S3 when new json files for Car brands are uploaded and persisted it to the DynamoDB Table called `Brands`.

## Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [NodeJs installed](https://https://nodejs.org/en/download/)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local)

## Project Infrastructure

The architecture consist of: 
- APi Gateway to receive the requests
- Two lambda functions
- An S3 Bucket
- Dynamodb with Table called `Brands`

Here is the image of the infrastructure

![Architecture](/images/aws_architecture.png)


## Deploy the application to AWS
To create the stack just use the `san deploy --guided` command in the root directory. Then just follow the wizard.

## CI/CD implementation

To implement Ci/CD for this project I would use [sam pipelines](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications/). AWS Sam Pipelines makes it easier to create secure continuous integration and deployment (CI/CD) pipelines for your organizations preferred continuous integration and continuous deployment (CI/CD) system.

To create a pipeline in the CI/CD system of your preference just type in the command line `sam pipeline init --bootstrap`, then just choose the CI/CD you want to use

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name [stack-name]
```
