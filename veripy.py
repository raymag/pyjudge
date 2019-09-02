#!/usr/bin/python
# -*- coding: utf-8-*-

import click, wexpect

@click.group()
def main():
    """| VERIPY |"""
    pass

@main.command()
@click.argument('program', type=click.File('rb'))
@click.argument('model', type=click.File('rb'))
# @click.option('--model', default="", help="Test's model")
def verify_one(program, model):
    """ Verify the stdout of one program using a given model """
    # if model == "":
    #     model = os.open( '.'.join(program.name.split('.')[:-1])+'.json', os.O_RDONLY)
    # else:
    #     model = os.open(model, os.O_RDONLY)
    ch = wexpect.spawn( 'python {}'.format(program.name) )
    ch.expect(r'.*')
    result = ch.after.replace('\r', '').replace('\n', '')

    if result == '8':
        click.echo('Ok.')
    else:
        click.echo('Oh.')

if __name__ == '__main__':
    main() 