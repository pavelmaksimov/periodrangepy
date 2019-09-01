import setuptools

VERSION = '2019.9.1'

setuptools.setup(
    name='periodrangepy',
    version=VERSION,
    description="Генерация списка периодов",
    packages=['periodrangepy'],
    install_requires=['python-dateutil'],
    license='MIT',
    url='https://github.com/pavelmaksimov/periodrangepy',
    author='Pavel Maksimov',
)
