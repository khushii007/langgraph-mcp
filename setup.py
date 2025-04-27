from setuptools import setup, find_packages

setup(
    name='langgraph-mcp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here, for example:
        # 'numpy',
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line interfaces if applicable
            # 'your_command = your_module:main_function',
        ],
    },
    include_package_data=True,
    package_data={
        # Include any non-Python files
        # '': ['static/*', 'media/*'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
