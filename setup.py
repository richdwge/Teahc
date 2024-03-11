from setuptools import setup, find_packages

setup(
    name='Teahc',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'MyTeahc',
        'httpcat-sdk',
        'myhttpcat',
        'myhcat',
    ],
    author='richdwge',
    author_email='rich_dwge@outlook.com',
    description='Teahc',
    license='MIT',
    keywords='Teahc',
    url='https://github.com/richdwge/Teahc',
    download_url='https://github.com/richdwge/Teahc',
    project_url='https://github.com/richdwge/Teahc',
    project_urls={
        "Source":"https://github.com/richdwge/Teahc",
    }
)

