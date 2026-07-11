class KubernetesTool:

    def deploy(self, service):

        return {
            "tool": "Kubernetes",
            "action": "deploy",
            "service": service,
            "status": "success"
        }
