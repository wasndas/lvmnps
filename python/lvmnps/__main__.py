import os

import click
from click_default_group import DefaultGroup
from clu.tools import cli_coro

from sdsstools.daemonizer import DaemonGroup

from lvmnps.actor.actor import lvmnps as NpsActorInstance


@click.group(cls=DefaultGroup, default="actor", default_if_no_args=True)
@click.option(
    "-c",
    "--config",
    "config_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Path to the user configuration file.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Debug mode. Use additional v for more details.",
)
@click.pass_context
def lvmnps(ctx, config_file, verbose):
    """Nps controller"""

    ctx.obj = {"verbose": verbose, "config_file": config_file}

from yaml import SafeLoader, load
from sdsstools import read_yaml_file

class Loader(SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)
        self.add_constructor('!include', Loader.include)
    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return load(f, Loader)


@lvmnps.group(cls=DaemonGroup, prog="nps_actor", workdir=os.getcwd())
@click.pass_context
@cli_coro
async def actor(ctx):
    """Runs the actor."""
    default_config_file = os.path.join(os.path.dirname(__file__), "etc/lvmnps_dli.yml")
    config_file = ctx.obj["config_file"] or default_config_file

    lvmnps_obj = NpsActorInstance.from_config(read_yaml_file(config_file, loader=Loader))

    if ctx.obj["verbose"]:
        lvmnps_obj.log.fh.setLevel(0)
        lvmnps_obj.log.sh.setLevel(0)

    await lvmnps_obj.start()
    await lvmnps_obj.run_forever()


if __name__ == "__main__":
    lvmnps()
