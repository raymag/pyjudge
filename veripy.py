# -*- coding: utf-8 -*-
import yaml, pexpect, click

@click.group()
def main():
	'''
********************\n
***** VERIPY  ******\n
********************\n
	'''
	pass

@main.command()
@click.argument('test-file')
def verify(test_file):
	''' Execute the tests from a given tests file '''
	with open(test_file, 'r') as file:
		tests_file = yaml.load(file)
		path = test_file.split('/')
		path = '/'.join(path[:-1])+'/'
		log = open('log.txt', 'w')

		for tests in tests_file:
			click.echo('='*30)
			click.echo(f'Título: {tests["title"]}')
			click.echo(f'Descrição: {tests["description"]}')

			log.write('='*30)
			log.write('\n')
			log.write(f'Título: {tests["title"]}')
			log.write('\n')
			log.write(f'Descrição: {tests["description"]}')
			log.write('\n')

			for test in tests['tests']:
				click.echo('-'*30)
				log.write('-'*30)
				log.write('\n')
				command = f'python3 {path}{tests["program"]}'
				ch = pexpect.spawn( command )

				for input in test['input']:
					ch.expect('.*')
					ch.sendline(str(input))
				ch.expect(pexpect.EOF)

				outputs = ch.before.decode('utf-8').split('\r\n')
				outputs.pop()
				for output in outputs:
					click.echo(output)
					log.write(output)
					log.write('\n')
				if outputs[-1] == test['output']:
					click.echo('Ok')
					log.write('Ok')
					log.write('\n')
				else:
					click.echo('Not ok')
					log.write('Not ok')
					log.write('\n')
		log.close()

if __name__ == '__main__':
	main()
