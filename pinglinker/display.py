"""Moduł wyświetlania wyników."""
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import box

from .speed_test import SpeedTestResult

console = Console()

SPEED_THRESHOLDS = [(100, "green"), (50, "yellow"), (20, "orange3")]
PING_THRESHOLDS = [(20, "green"), (50, "yellow"), (100, "orange3")]


def _color(value: float, thresholds: list, reverse: bool = False) -> str:
    for limit, color in thresholds:
        if (value <= limit) if reverse else (value >= limit):
            return color
    return "red"


def speed_color(speed: float) -> str:
    return _color(speed, SPEED_THRESHOLDS)


def ping_color(ping: float) -> str:
    return _color(ping, PING_THRESHOLDS, reverse=True)


def welcome() -> None:
    panel = Panel(
        "[bold cyan]🚀 PingLinker[/]\n[dim]Test szybkości internetu[/]",
        box=box.DOUBLE, border_style="cyan", padding=(1, 2)
    )
    console.print(panel, "")


def spinner(msg: str) -> Progress:
    return Progress(
        SpinnerColumn(), TextColumn(f"[bold blue]{msg}"),
        console=console, transient=True
    )


def results(r: SpeedTestResult) -> None:
    t = Table(title="📊 Wyniki", box=box.ROUNDED, border_style="green", title_style="bold green")
    t.add_column("", style="cyan")
    t.add_column("", justify="right")
    
    dc, uc, pc = speed_color(r.download), speed_color(r.upload), ping_color(r.ping)
    t.add_row("⬇️  Pobieranie", f"[{dc}]{r.download:.2f} Mb/s[/]")
    t.add_row("⬆️  Wysyłanie", f"[{uc}]{r.upload:.2f} Mb/s[/]")
    t.add_row("📶 Ping", f"[{pc}]{r.ping:.2f} ms[/]")
    console.print(t, "")
    
    i = Table(title="ℹ️  Połączenie", box=box.ROUNDED, border_style="blue", title_style="bold blue")
    i.add_column("", style="cyan")
    i.add_column("")
    i.add_row("🏢 ISP", r.isp)
    i.add_row("🖥️  Serwer", r.server)
    i.add_row("🌍 Kraj", r.country)
    console.print(i)


def error(msg: str) -> None:
    console.print(f"[bold red]❌ {msg}[/]")


def info(msg: str) -> None:
    console.print(f"[blue]ℹ️  {msg}[/]")
