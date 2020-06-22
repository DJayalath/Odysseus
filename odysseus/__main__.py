import click
import numpy as np
from .network import Network
from .globals import FILE_TYPE_SET

@click.command()
@click.argument('file')
def main(file):
    click.echo("\n*** Initialising network ***\n")
    network = Network()

    click.echo("\n*** Making predictions ***\n")

    results = network.predict(file)
    printTop3(results)

    click.echo("\n*** Finished ***\n")

def printTop3(results):
    fts = FILE_TYPE_SET[:]
    for j in range(3):
        idx = np.argmax(results, axis=0)
        prediction = fts[idx]
        prob = results[idx]
        click.echo("    " + prediction + " " + "{:5.2f}%".format(prob * 100))
        results = np.delete(results, idx)
        fts.remove(prediction)

if __name__ == '__main__':
    main()
