#!/usr/bin/env python3
import click

@click.group
def cli():
    pass

def main():
    print("Hello from pymd2googleslides")

if __name__ == "__main__":
    cli()
