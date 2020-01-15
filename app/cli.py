import os
import click
from app import app

@app.cli.group()
def translate():
	"""Translation and localization commands."""
	pass

@translate.command()
@click.argument('lang')
def init(lang):
	"""Initialize a new language"""
	if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):