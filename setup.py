from distutils.core import setup


setup(
  name = 'tkinterpp',
  packages = ['tkinterpp'],
  version = '0.1',
  license='MIT',
  description = 'A collection of additional widgets for tkinter and ttk',
  author = 'Dogeek',
  author_email = 'simon.bordeyne@gmail.com',
  url = 'https://github.com/Dogeek/tkinter-pp',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['tkinter', 'addon'],
  install_requires=[
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)