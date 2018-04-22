# -*- coding: utf-8 -*-

"""Run this script with :code:`python3 -m bio2bel_drugbank`."""

import click

from .manager import Manager

main = Manager.get_cli()


@main.group()
def manage():
    """Manage the database."""


@manage.group()
def patents():
    """Manage patents."""


@patents.command()
@click.pass_obj
def ls(manager):
    """List patents."""
    click.echo_via_pager('\n'.join(
        f'{patent.patent_id}\t{patent.country}\t{"|".join(drug.name for drug in patent.drugs)}'
        for patent in manager.list_patents()
    ))


if __name__ == '__main__':
    main()
