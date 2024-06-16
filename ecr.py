import boto3

#enabling programmatic interaction with ECR in python || It's a API
ecr_client = boto3.client('ecr')


#used to specify the name of the ECR repository to create
repository_name="cloud-native-repo"
#Calls the create_repository method of the ECR client to create a new repository with the specified name (repository_name) and stores the response
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr/client/create_repository.html
response = ecr_client.create_repository(repositoryName=repository_name)

#extracts the URI of the newly created repository from the response and assigns it to the variable
repository_uri = response['repository']['repositoryUri']
print(repository_uri)