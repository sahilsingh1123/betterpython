
from typing import Optional
from atlassian import Jira
import os
from dotenv import load_dotenv

load_dotenv()

JIRA_API_KEY = os.getenv("JIRA_API_KEY")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_URL = os.getenv("JIRA_URL")

class JiraService:
    def __init__(self) -> None:
        self._jira_key = None
        self._jira_id = None
        self.jira_client = self.create_jira_client()

    def create_jira_ticket(self, fields:dict) -> Optional[str]:
        new_issue = self.jira_client.issue_create(fields=fields)

        self._jira_id = new_issue["id"]
        self._jira_key = new_issue["key"]
    
    def update_jira_issue(self, fields):
        self.jira_client.issue_update(
            issue_key=self._jira_key,
            fields=fields
        )
        return True

    def update_jira_description(self, description: str):
        fields= {"description": description}
        return  self.update_jira_issue(fields)

    def update_jira_summary(self, summary: str):
        fields= {"summary": summary}
        return  self.update_jira_issue(fields)


    def add_jira_comment(self, message):
        self.jira_client.issue_add_comment(self._jira_key, message)

    def set_issue_status(self, status):
        # status - Resolved/Closed/In Progress/To Do
        self.jira_client.set_issue_status(self._jira_key, status)
    
    def create_jira_client(self):
        return Jira(url=JIRA_URL, username=JIRA_EMAIL, password=JIRA_API_KEY)
    

if __name__ == "__main__":
    fields = dict(
        summary = "testing jira summary from script",
        description = "descriptin from script",
        project = {"key": "KAN"},
        issuetype = {"name": "Task"}
    )
    fields_update = dict(
        summary = "testing jira summary from script [field update]",
        description = "descriptin from script [field update]",
    )
    jira_service = JiraService()
    jira_service._jira_key = "KAN-11"
    # data = jira_service.create_jira_ticket(fields)
    # jira_service.add_jira_comment("Adding jira comment from script")
    # data = jira_service.set_issue_status("Done")
    # data = jira_service.update_jira_description(fields_update)
    # Retrieve the permission scheme for the project
    # print(data)
    
