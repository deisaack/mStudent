from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, 'qeos', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(name='qeos',
      version=os.getenv('BUILD_VERSION', about['__version__']),
      description='Qubeans Django - EOS Interface',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='QBN',
      author_email='qubeans@gmail.com',
      url='https://gitlab.com/qubeans/swarm',
      packages=find_packages(),
      test_suite = 'nose.collector',
      install_requires=[
          'requests',
          'base58',
          'ecdsa',
          'colander',
          'pytz',
          'six',
          'pyyaml',
      ],
      entry_points = {
          'console_scripts' :[
              'validate_chain = qeos.command_line:validate_chain',
              'pycleos = qeos.command_line:cleos',
              'pytesteos = qeos.command_line:testeos',
          ],
      }
)
