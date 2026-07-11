from app.tools.github_tool import GitHubTool


class SecurityAgent:

    def __init__(self):
        self.name = "Security Agent"
        self.github = GitHubTool()

    def scan(self, application):

        repo = self.github.check_repository(application)

        return {
            "agent": self.name,
            "repository": repo,
            "status": "secure"
        }
