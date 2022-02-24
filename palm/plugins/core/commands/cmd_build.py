import click
import subprocess


@click.command("build")
@click.option("--compose-file", default="docker-compose.yml")
def cli(compose_file):
    """Rebuilds the image for the current working directory"""
    build_cmd = [
        "docker", 
        "buildx", 
        "bake", 
        "-f", compose_file
    ]
    subprocess.run(build_cmd, check=True)
