import click
import subprocess

from cs_client import build_chatbot_engine


@click.group()
def main(args=None):
    """Console script for chatbot"""
    pass


@main.group()
def log(args=None):
    """Log handling"""
    pass


@log.command()
def download(args=None):
    """Download log from server"""
    subprocess.call(["rsync", "-Pav", "root@undertheseanlp.com:/root/service/chatbot/logs/*", "logs"])
    print("Download log")


@main.group()
def server(args=None):
    """Server handling"""
    pass


@server.command()
def cs():
    """Start ChatScript server"""
    print("Start ChatScript server")
    subprocess.call("./script_cs.sh", shell=True)


@server.command()
def cs_local():
    """Start ChatScript server"""
    print("Start ChatScript local")
    subprocess.call("./script_cs_local.sh", shell=True)


@server.command()
def web():
    """Start Web server"""
    print("Start Web server")
    subprocess.call("./script_web.sh", shell=True)

@main.command()
def build():
    """Build chatbot engine"""
    print("Build chatbot engine")
    build_chatbot_engine()
    print("Chatbot engine is built successfully.")


if __name__ == '__main__':
    main()
