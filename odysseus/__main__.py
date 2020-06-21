import click
from .network import Network

@click.command()
@click.argument('file')
def main(file):
    click.echo("\n*** Initialising network ***\n")
    network = Network()

    click.echo("\n*** Making predictions ***\n")
    network.single_predict(file)

    click.echo("\n*** Finished ***\n")

if __name__ == '__main__':
    main()
