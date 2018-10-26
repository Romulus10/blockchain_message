from setuptools import setup

setup(
    name='blockchain_message',
    version='0.1.0a3',
    packages=['test', 'client', 'blockchain_message', 'blockchain_message.src'],
    url='',
    license='GPL',
    author='Sean Batzel',
    author_email='romulus108@protonmail.com',
    description='An email-like service that uses Ethereum as a decentralized email service.', install_requires=['web3']
)
