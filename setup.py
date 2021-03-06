from distutils.core import setup

setup(
    name='devourer',
    packages=['devourer'],
    version='0.3.2',
    install_requires=[
        'requests',
        'six',
    ],
    description='Devourer is a generic API client.'
                'It features an object-oriented, declarative approach to simplify the communication.',
    author='Bonnier Business Polska / Krzysztof Bujniewicz',
    author_email='racech@gmail.com',
    url='https://github.com/bonnierpolska/devourer',
    download_url='https://github.com/bonnierpolska/devourer/tarball/0.3.2',
    keywords=['api', 'generic api', 'api client'],
    classifiers=[]
)
