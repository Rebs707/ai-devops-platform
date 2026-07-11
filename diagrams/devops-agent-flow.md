# DevOps Agent Workflow

```text
Developer Change

      |
      v

CI/CD Agent

      |
      v

Security Agent

      |
      v

Deployment Agent

      |
      +---- Docker Build
      |
      +---- Kubernetes Deploy

      |
      v

Monitoring Agent

      |
      v

Incident Agent

      |
      v

Automated Response
