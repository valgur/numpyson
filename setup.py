
from setuptools import setup

if __name__ == "__main__":
    setup(name="numpyson",
          version='0.4',
          long_description=open("README.rst").read() + "\n\n" +
                           open("CHANGELOG.rst").read(),
          py_modules=['numpyson', 'test_numpyson'],
          author="holger krekel, David Moss",
          classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3'],
          install_requires=["numpy", "pandas>=0.13", "jsonpickle>=0.7.1"],
          platforms=['unix', 'linux', 'osx', 'win32'],
    )
