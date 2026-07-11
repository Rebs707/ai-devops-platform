from app.tools.docker_tool import DockerTool
from app.tools.kubernetes_tool import KubernetesTool


class DeploymentAgent:

    def __init__(self):
        self.name = "Deployment Agent"
        self.docker = DockerTool()
        self.kubernetes = KubernetesTool()

    def deploy(self, application):

        build = self.docker.build(application)

        deployment = self.kubernetes.deploy(application)

        return {
            "agent": self.name,
            "build": build,
            "deployment": deployment,
            "status": "completed"
        }
