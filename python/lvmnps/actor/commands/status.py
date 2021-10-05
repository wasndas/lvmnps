#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Florian Briegel (briegel@mpia.de)
# @Date: 2021-08-12
# @Filename: status.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import click
from clu.command import Command

from lvmnps.actor.commands import parser
from lvmnps.switch.dli.powerswitch import PowerSwitch
from lvmnps.switch.exceptions import PowerException


@parser.command()
@click.argument("NAME", type=str, default="")
@click.argument("PORTNUM", type=int, default=0)
async def status(command: Command, switches: PowerSwitch, name: str, portnum: int):
    """Returns the status of the outlets."""

    command.info(text=f"Printing the current status of port {name}")

    try:
        status = {}
        for switch in switches:
            # status |= await switch.statusAsJson(name, portnum) works only with python 3.9
            status = dict(list(status.items()) +
                                    list((await switch.statusAsJson(name, portnum)).items()))

    except PowerException as ex:
        return command.fail(ex)

    return command.finish(status)


