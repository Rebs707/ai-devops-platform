class DockerExecutor:
    """
    Executes Docker operations.
    """

    def __init__(self):
        self.name = "Docker Executor"

    def build_image(self, application):

        return {
            "executor": self.name,
            "action": "docker build",
            "image": application,
            "status": "success"
        }

    def run_container(self, application):

        return {
            "executor": self.name,
            "action": "docker run",
            "container": application,
            "status": "running"
        }
