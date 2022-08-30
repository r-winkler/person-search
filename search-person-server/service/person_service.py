from repository import Repository
from repository.in_memory import InMemoryRepository


class PersonService(object):
    def __init__(self, repo_client=Repository(adapter=InMemoryRepository)):
        self.repo_client = repo_client

    def find_all(self):
        return self.repo_client.find_all()
