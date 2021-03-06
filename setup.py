
from distutils.core import setup
setup(
  name = 'oxicord',        
  packages = ['oxicord'],  
  version = '1.0.0',     
  license='MIT',       
  description = 'oxicord An API Wrapper for discord',  
  author = 'Md Rehaan',                   
  author_email = 'mdrehaan7766@gmail.com',     
  url = 'https://github.com/oxy-Op/oxicord',  
  download_url = 'https://github.com/oxy-Op/oxicord/archive/refs/tags/1.0.0.tar.gz',    
  keywords = ['oxicord', 'loves', 'you'],  
  install_requires=[            
          'requests',
          'time',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)