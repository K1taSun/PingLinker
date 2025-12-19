"""Interfejs wiersza poleceń."""
import click
from . import display
from .speed_test import SpeedTester, SpeedTestResult


def run_with_spinner(msg: str, func):
    with display.spinner(msg) as p:
        p.add_task(msg)
        return func()


@click.command()
@click.option('-d', '--download', 'mode', flag_value='d', help='Tylko pobieranie')
@click.option('-u', '--upload', 'mode', flag_value='u', help='Tylko wysyłanie')
@click.option('-p', '--ping', 'mode', flag_value='p', help='Tylko ping')
@click.option('-i', '--info', 'mode', flag_value='i', help='Tylko info')
def cli(mode: str | None) -> None:
    """🚀 PingLinker - Test szybkości internetu."""
    display.welcome()
    tester = SpeedTester()
    
    try:
        run_with_spinner("Łączenie z serwerem...", tester._ensure_init)
        display.info("Połączono")
        
        match mode:
            case 'p':
                display.console.print(f"\n📶 Ping: [bold]{tester.ping:.2f} ms[/]")
            case 'd':
                dl = run_with_spinner("Test pobierania...", tester.download)
                display.console.print(f"\n⬇️  Pobieranie: [bold]{dl:.2f} Mb/s[/]")
            case 'u':
                ul = run_with_spinner("Test wysyłania...", tester.upload)
                display.console.print(f"\n⬆️  Wysyłanie: [bold]{ul:.2f} Mb/s[/]")
            case 'i':
                name, country = tester.server_info
                display.console.print(f"\n🏢 ISP: [bold]{tester.isp}[/]")
                display.console.print(f"🖥️  Serwer: [bold]{name}[/]")
                display.console.print(f"🌍 Kraj: [bold]{country}[/]")
                display.console.print(f"📶 Ping: [bold]{tester.ping:.2f} ms[/]")
            case _:
                dl = run_with_spinner("Test pobierania...", tester.download)
                ul = run_with_spinner("Test wysyłania...", tester.upload)
                name, country = tester.server_info
                display.console.print()
                display.results(SpeedTestResult(dl, ul, tester.ping, name, country, tester.isp))
    except Exception as e:
        display.error(str(e))
        raise SystemExit(1)


if __name__ == '__main__':
    cli()
