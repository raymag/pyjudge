#!/usr/bin/python
# -*- coding: utf-8-*-

import click, pexpect, json

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

    with open(model.name, 'r') as jsonf:
        modelf = json.load(jsonf)

    for test in modelf['tests']:
        print(test)

        ch = pexpect.spawn( 'python {} {}'.format(program.name, test['input']) )
        ch.expect(pexpect.EOF)
        result = ch.before.replace('\n', '').replace('\r', '')
        print('Result: ' + result)
        print('Out: '+ str(test['output']) )
        if str(result) == str(test['output']):
            click.echo('Ok.')
        else:
            click.echo('Oh.')

if __name__ == '__main__':
    main() 
