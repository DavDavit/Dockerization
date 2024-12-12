import docker

docker_url = 'https://654e-5-77-201-114.ngrok-free.app:2375'
client = docker.DockerClient(base_url=docker_url)

# Retrieve the container and commit it as an image
container_name = "docker-hadoop"
image_name = "hadoop_ml_model"
container = client.containers.get(container_name)
image = container.commit(repository=image_name)

# Tag and push the image
client.images.push(repository="root/hadoop_ml_model", tag="latest")
print("Image pushed successfully!")
