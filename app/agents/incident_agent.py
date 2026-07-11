from app.tools.incident_executor import IncidentExecutor


class IncidentAgent:
    """
    Handles incident analysis and response.
    """

    def __init__(self):

        self.name = "Incident Agent"
        self.executor = IncidentExecutor()


    def investigate(self, issue):

        analysis = self.executor.analyze(issue)

        recommendation = self.executor.recommend_action(issue)

        return {
            "agent": self.name,
            "analysis": analysis,
            "recommendation": recommendation
        }
