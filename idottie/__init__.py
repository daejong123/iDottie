from .core import *

import click
from idottie import tools

def ls(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    tools.translate.hello()
    ctx.exit()

@click.command()
@click.option('--hello', is_flag=True, callback=ls, expose_value=False, is_eager=True, help='list files')
@click.option('-t', help='transalte')
def cli(t):
    tools.translate.translate(t)
