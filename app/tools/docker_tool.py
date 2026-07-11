class DockerTool:

    def build(self, image):

        return {
            "tool": "Docker",
            "action": "build",
            "image": image,
            "status": "success"
        }
