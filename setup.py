from setuptools import setup, find_packages


setup(
    name='mkdocs-vim-md-tags-plugin',
    version='0.2.0',
    description='An MkDocs plugin',
    long_description='An MkDocs plugin that creates a vim tag file of all markdown files',
    keywords='mkdocs',
    url='https://github.com/midnightprioriem/mkdocs-vim-md-tags-plugin',
    download_url='https://github.com/midnightprioriem/mkdocs-vim-md-tags-plugin/archive/v_020.tar.gz',
    author='Zach Hannum',
    author_email='zacharyhannum@gmail.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'vim-md-tags = mkdocs_vim_md_tags_plugin.plugin:VimMdTags'
        ]
    }
)
