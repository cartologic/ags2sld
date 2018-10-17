from distutils.core import setup

from setuptools import find_packages
setup(
    name='ags2sld',
    packages=find_packages(),
    version="0.1.0",
    description='ags2sld',
    long_description="ags2sld",
    long_description_content_type='text/markdown',
    author='Cartologic',
    author_email='info@cartologic.com',
    url='https://github.com/cartologic/cartoview',
    include_package_data=True,
    keywords=[
        'cartoview', 'gis', 'geonode', "django", "web mapping", "applications",
        "apps", "application management"
    ],
    classifiers=[
        "Development Status :: 4 - Beta", "Framework :: Django :: 1.8",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    license="BSD",
    install_requires=[])
