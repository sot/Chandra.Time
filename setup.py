# from distutils.core import setup, Extension
import os
cvs_version= '$Id: setup.py,v 1.11 2007-08-27 21:30:51 aldcroft Exp $'; 

if (os.name == "nt") :
    compile_args = ['/EHs','/D_CRT_SECURE_NO_DEPRECATE']
else:
    compile_args = ['-Wno-switch-enum', '-Wno-switch', '-Wno-switch-default',
                    '-Wno-deprecated', '-Wno-parentheses']

# (gcc_stdin, gcc_stdouterr) = os.popen4(['gcc','-v', '--help'])
# gcc_opt = gcc_stdouterr.read()
# if gcc_opt.find('fstack-protector') != -1:
#    compile_args.append('-fno-stack-protector')

# machine = Popen(['uname','--machine'], stdout=PIPE).communicate()[0]
# if machine.startswith('x86_64'):

library_dirs = os.environ.get('LD_LIBRARY_PATH', '').split(':')

from setuptools import setup, Extension
setup(name='Chandra.Time',
      author = 'Tom Aldcroft',
      description='Convert between various time formats relevant to Chandra',
      author_email = 'taldcroft@cfa.harvard.edu',
      py_modules = ['Chandra.axTime3', 'Chandra.Time'],
      version='1.13',
      zip_safe=False,
      test_suite = "Chandra.test_Time",

      namespace_packages=['Chandra'],
      packages=['Chandra'],
      package_dir={'Chandra' : 'Chandra'},
      ext_modules = [Extension('Chandra._axTime3',
                               ['Chandra/axTime3.cc',
                                'Chandra/XTime.cc',
                                'Chandra/axTime3.i',
                                ],
                               swig_opts=['-c++'],
                               language='c++',
                               # library_dirs=library_dirs,
                               # extra_link_args=['-lXTime'],
                               extra_compile_args=compile_args,
                               )
                     ]
      )
