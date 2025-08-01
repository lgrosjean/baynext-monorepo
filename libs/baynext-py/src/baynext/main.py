"""Main entry point."""

import typer

from baynext import __version__
from baynext.commands import auth, config, datasets, projects

app = typer.Typer(
    name="Baynext",
    help="🚀 Baynext CLI - Manage your projects and teams from the command line",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

# Add command groups
app.add_typer(auth.app)
app.add_typer(config.app)
app.add_typer(projects.app)
app.add_typer(datasets.app)


@app.command()
def version() -> None:
    """📋 Show version information."""
    typer.echo(f"Baynext CLI v{__version__}")


if __name__ == "__main__":
    app()
