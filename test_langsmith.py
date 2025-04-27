from langsmith import Client

client = Client()

# Try listing your projects
projects = client.list_projects()

for project in projects:
    print(project.name)
