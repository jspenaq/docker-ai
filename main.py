import click
import sys


@click.command()
@click.argument('query', required=False)
@click.option('--quiet', '-q', is_flag=True, help='Execute command without confirmation.')
def main(query, quiet):
    """
    Docker-AI: An intelligent interface for managing Docker environments using natural language.

    Translates natural language queries into Docker commands.
    """

    if not query:
        if not sys.stdin.isatty():
            query = sys.stdin.read().strip()  # Read from stdin if available
        else:
            click.echo("Please provide a query either as a command-line argument or via standard input.", err=True)
            sys.exit(1)

    if not query:
       click.echo("No query provided.", err=True)
       sys.exit(1)


    click.echo(f"Query received: {query}")
    click.echo(f"Quiet mode: {quiet}")

    # Here you would normally pass the query to the query interpretation component.
    # For now, we'll just print a message.
    click.echo("Passing query to interpretation component...")


if __name__ == '__main__':
    main()