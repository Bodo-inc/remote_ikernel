# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same
try:
    from setuptools import setup

    scripts = []
except ImportError:
    from distutils.core import setup

    scripts = ["bin/remote_ikernel"]

import versioneer

setup(
    name="remote_ikernel",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Running IPython kernels through batch queues",
    long_description=open("README.rst").read(),
    author="Tom Daff",
    author_email="tdd20@cam.ac.uk",
    license="BSD",
    url="https://github.com/Bodo-inc/remote_ikernel",
    packages=["remote_ikernel"],
    scripts=scripts,
    entry_points={"console_scripts": ["remote_ikernel = remote_ikernel.__main__:main"]},
    install_requires=["notebook", "pexpect", "tornado"],
    tests_requires=["pytest", "scripttest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: IPython",
        "License :: OSI Approved :: BSD License",
    ],
)
