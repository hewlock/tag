import setuptools
import tag

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    author=tag.__author__,
    author_email=tag.__email__,
    data_files=[('share/man/man1', ['docs/tag.1'])],
    description='File name tag tool',
    install_requires=['click'],
    license=tag.__license__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='tag',
    setup_requires=['click'],
    url='https://github.com/hewlock/tag-cli',
    version=tag.__version__,

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'tag = tag.cli:cli'
        ],
    },
    packages=[
        'tag',
        'tag.command',
        'tag.util',
    ],
)
