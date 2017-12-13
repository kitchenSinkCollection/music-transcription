from setuptools import setup, find_packages

setup(name='trainer',
      version='0.1',
      packages=find_packages(),
      description='example to run keras on gcloud ml-engine',
      author='MB',
      license='MIT',
      install_requires=[
          'keras',
          'h5py',
          'matplotlib'
      ],
      zip_safe=False)