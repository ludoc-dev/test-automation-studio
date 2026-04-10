from locust import HttpUser, task, between, events
from locust.runners import MasterRunner
import time
import random


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://the-internet.herokuapp.com"

    def on_start(self):
        """Executado quando um usuário inicia"""
        self.client.get("/")

    @task(3)
    def login_logout(self):
        """Fluxo completo de login/logout (pesado)"""
        # Página de login
        response = self.client.get("/login")
        if response.status_code == 200:
            # Submit login
            self.client.post("/login", {
                "username": "tomsmith",
                "password": "SuperSecretPassword!"
            })
            # Logout
            self.client.get("/logout")

    @task(2)
    def view_pages(self):
        """Navegação por páginas (médio)"""
        pages = ["/", "/abtest", "/checkboxes"]
        page = random.choice(pages)
        self.client.get(page)

    @task(1)
    def status_codes(self):
        """Verifica status codes (leve)"""
        codes = [200, 301, 404, 500]
        code = random.choice(codes)
        self.client.get(f"/status_codes/{code}")


class APIUser(HttpUser):
    wait_time = between(0.5, 2)
    host = "https://jsonplaceholder.typicode.com"

    @task
    def get_posts(self):
        """Busca posts (API call)"""
        self.client.get("/posts")

    @task
    def get_users(self):
        """Busca usuários (API call)"""
        self.client.get("/users")

    @task(weight=2)
    def create_post(self):
        """Cria post (POST request)"""
        self.client.post("/posts", json={
            "title": "Test Post",
            "body": "This is a test post from Locust",
            "userId": 1
        })


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Executado quando o teste termina"""
    if isinstance(environment.runner, MasterRunner):
        print("\n📊 Teste finalizado!")
        print(f"Total de requisições: {environment.runner.stats.total.num_requests}")
        print(f"Falhas: {environment.runner.stats.total.num_failures}")
        print(f"RPS médio: {environment.runner.stats.total.total_rps:.2f}")


@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, **kwargs):
    """Listener para cada requisição"""
    if exception:
        print(f"❌ Erro: {request_type} {name} - {exception}")
    elif response_time > 1000:
        print(f"⚠️  Lento: {request_type} {name} - {response_time}ms")
