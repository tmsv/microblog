import os
import click
from app import app

@app.cli.group()
def translate():
	"""Translation and localization commands."""
	pass

@translate.command()
@click.argument('lang')
def init(lang)