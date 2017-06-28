from setuptools import setup, Extension

vdm_module = Extension(
    '_cpp',
    sources=[
        'aisparser/core/cpp.i', 'aisparser/core/cpp/vdm_opt.cpp',
        'aisparser/core/cpp/srcdata_opt.cpp',
        'aisparser/core/cpp/vdm_parse_core.cpp'
    ],
    swig_opts=['-c++'])

setup(
    name='aisparser',
    version='0.0.6',
    keyword=['AIS', 'Automatic Identification System'],
    description='Python library parsing AIS message',
    author=['Macrovve', 'callMePlus'],
    license='MIT License',
    install_requires=[],
    url='https://github.com/macrovve/aisparser',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    ext_modules=[vdm_module])
