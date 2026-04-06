import asyncio
import random
import socket
from typing import Any
from core_engine.domain.interfaces import ISurveillanceEngine

class AdvancedScanner(ISurveillanceEngine):
    """Motor de vigilancia asíncrono con escaneo sigiloso y banner grabbing."""
    def __init__(self, ports=None, timeout=2, retries=2):
        self.ports = ports or [22, 80, 443, 8080, 3306, 3389]
        self.timeout = timeout
        self.retries = retries

    async def scan(self, target: str) -> Any:
        results = []
        sem = asyncio.Semaphore(10)
        ports = self.ports[:]
        random.shuffle(ports)
        async def scan_port(port):
            for attempt in range(self.retries):
                try:
                    await asyncio.sleep(random.uniform(0.05, 0.2))
                    reader, writer = await asyncio.wait_for(asyncio.open_connection(target, port), timeout=self.timeout)
                    banner = await self._grab_banner(reader, writer)
                    writer.close()
                    await writer.wait_closed()
                    return {"port": port, "banner": banner}
                except Exception:
                    await asyncio.sleep(2 ** attempt * 0.1)
            return {"port": port, "banner": None}
        async with sem:
            tasks = [scan_port(port) for port in ports]
            results = await asyncio.gather(*tasks)
        return results

    async def _grab_banner(self, reader, writer):
        try:
            writer.write(b'\r\n')
            await writer.drain()
            data = await asyncio.wait_for(reader.read(100), timeout=1)
            return data.decode(errors='ignore')
        except Exception:
            return None
