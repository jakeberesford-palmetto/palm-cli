import sys

import click


@click.command("update")
@click.option("--local", is_flag=True, help="attempts to install from cwd")
@click.pass_obj
def cli(environment, local: bool):
    """This updates the current version of palm. meta huh?"""

    cmd = "python3 -m pip install ." if local else "pip install palm -U"

    ex_code, _, _ = environment.run_on_host(cmd)

    if ex_code == 0:
        click.secho("Success! Palm has been updated.", fg="green")
    else:
        click.secho("Failed to update palm", fg="red")
        sys.exit(ex_code)
