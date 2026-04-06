import httpx

class AIGatewayClient:
    """Cliente para interactuar con el AI Gateway (DLP, inferencia, etc)."""
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    async def analyze(self, data: dict) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self.base_url}/analyze", json=data)
            resp.raise_for_status()
            return resp.json()
