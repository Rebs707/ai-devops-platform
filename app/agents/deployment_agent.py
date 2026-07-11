from app.tools.docker_executor import DockerExecutor
from app.tools.kubernetes_executor import KubernetesExecutor


class DeploymentAgent:
    """
    Handles application deployment workflows.
    """

    def __init__(self):

        self.name = "Deployment Agent"
        self.docker = DockerExecutor()
        self.kubernetes = KubernetesExecutor()


    def deploy(self, application):

        image = self.docker.build_image(application)

        container = self.docker.run_container(application)

        deployment = self.kubernetes.deploy_service(application)

        status = self.kubernetes.check_status(application)

        return {
            "agent": self.name,
            "image": image,
            "container": container,
            "deployment": deployment,
            "health": status,
            "status": "completed"
        }
