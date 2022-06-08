# flows/my_flow.py

from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import GitHub

@task
def get_data():
    return [1, 2, 3, 4, 5]

@task
def print_data(data):
    print(data)

with Flow("example-docker") as flow:
    data = get_data()
    print_data(data)

flow.storage = GitHub(
    repo="jasonnoxon/prefect-test",                            # name of repo
    path="flows/my_flow.py",                    # location of flow file in repo
    #access_token_secret="GITHUB_ACCESS_TOKEN"   # name of personal access token secret
)
flow.run_config = DockerRun(image="prefecthq/prefect:latest")
