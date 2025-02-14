from kubernetes import client, config

#Load Kubernetes configuration
config.load_kube_config()

#create a kubernetes api client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-flask-app"),      #this the app name
    spec=client.V1DeploymentSpec
    (
        replicas=1,
        selector=client.V1LabelSelector
        (
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec
        (
            metadata=client.V1ObjectMeta
            (
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec
            (
                containers=[
                    client.V1Container
                    (
                        name="my-flask-container",
                        image="831574952305.dkr.ecr.ap-south-1.amazonaws.com/cloud-native-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)


#create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),      #this is my service name
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)