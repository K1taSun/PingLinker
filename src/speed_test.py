"""Moduł testowania szybkości internetu."""
import speedtest
from dataclasses import dataclass, field
from functools import cached_property


@dataclass(slots=True)
class SpeedTestResult:
    """Wyniki testu szybkości."""
    download: float = 0.0
    upload: float = 0.0
    ping: float = 0.0
    server: str = ""
    country: str = ""
    isp: str = ""


class SpeedTester:
    """Tester szybkości internetu."""
    
    __slots__ = ('_st', '_server')
    
    def __init__(self):
        self._st: speedtest.Speedtest | None = None
        self._server: dict | None = None
    
    def _ensure_init(self) -> None:
        if not self._st:
            self._st = speedtest.Speedtest()
            self._st.get_best_server()
            self._server = self._st.results.server
    
    @property
    def ping(self) -> float:
        self._ensure_init()
        return self._server.get('latency', 0.0)
    
    @property
    def server_info(self) -> tuple[str, str]:
        self._ensure_init()
        return self._server.get('sponsor', '?'), self._server.get('country', '?')
    
    @property
    def isp(self) -> str:
        self._ensure_init()
        return self._st.results.client.get('isp', '?')
    
    def download(self) -> float:
        self._ensure_init()
        return self._st.download() / 1_000_000
    
    def upload(self) -> float:
        self._ensure_init()
        return self._st.upload() / 1_000_000
    
    def full_test(self) -> SpeedTestResult:
        self._ensure_init()
        name, country = self.server_info
        return SpeedTestResult(
            download=self.download(),
            upload=self.upload(),
            ping=self.ping,
            server=name,
            country=country,
            isp=self.isp
        )
