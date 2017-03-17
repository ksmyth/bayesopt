from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

import os
import os.path
import platform

this_dir = os.path.dirname(os.path.abspath(__file__))

version = '0.1'

setup_args = dict(name='bayesopt',
    version=version,
    description="BayesOpt is an efficient implementation of the Bayesian optimization methodology for nonlinear optimization, experimental design and hyperparameter tuning",
#    long_description=u'\n\n'.join([readme, changes]),
#    classifiers=[
#    keywords='',
    author='Ruben Martinez-Cantin',
    author_email='rmcantin@unizar.es',
    url='https://github.com/rmcantin/bayesopt',
    license='AGPL>=3.0',
    requires=[],
    ext_modules=[],
    data_files=[("", ["LICENSE"])],
    )

setup_args['ext_modules'].append(Extension('bayesopt',
    ['sources go here'],
    libraries=['boost'],
    library_dirs=[],
    include_dirs=[])
)

if platform.system() == 'Windows':
    class my_build_ext(build_ext):
        def build_extension(self, ext):
            """Copy the already-compiled pyd."""
            import shutil
            import os.path
            try:
                os.makedirs(os.path.dirname(self.get_ext_fullpath(ext.name)))
            except WindowsError as e:
                if e.winerror != 183:  # already exists
                    raise

            shutil.copyfile(os.path.join(this_dir, r'lib\Release\libbayesopt.dll'), self.get_ext_fullpath(ext.name))

    setup_args['cmdclass'] = {'build_ext': my_build_ext}

setup(**setup_args)
