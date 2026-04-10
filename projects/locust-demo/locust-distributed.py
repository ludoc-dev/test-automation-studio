from locust import HttpUser, task, between
from locust.runners import MasterRunner
import random


class DistributedUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://the-internet.herokuapp.com"

    @task
    def browse_site(self):
        """Navegação realista pelo site"""
        actions = [
            self.view_homepage,
            self.login,
            self.view_dynamic_content,
            self.view_secure_area
        ]
        random.choice(actions)()

    def view_homepage(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status {response.status_code}")

    def login(self):
        with self.client.post("/login", {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
        }, catch_response=True) as response:
            if response.status_code in [200, 302]:
                response.success()
            else:
                response.failure(f"Login failed: {response.status_code}")

    def view_dynamic_content(self):
        with self.client.get("/dynamic_content", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status {response.status_code}")

    def view_secure_area(self):
        # Primeiro faz login
        self.client.post("/login", {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
        })
        # Acessa área segura
        with self.client.get("/secure", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Secure area failed: {response.status_code}")
