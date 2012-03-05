import glob
from setuptools import setup, find_packages
from ubuntutweak import __version__

setup(name='ubuntu-tweak',
      version=__version__,
      description='magic tool to configure Ubuntu',
      author='TualatriX',  
      author_email='tualatrix@gmail.com',
      url='http://ubuntu-tweak.com',
      scripts=['ubuntu-tweak'],
      packages=find_packages(exclude=['tests']),
      data_files=[
          ('../etc/dbus-1/system.d/', ['data/ubuntu-tweak-daemon.conf']),
          ('share/dbus-1/services', ['data/unity-lens-ubuntu-tweak.service']),
          ('share/dbus-1/system-services', ['data/com.ubuntu_tweak.daemon.service']),
          ('share/glib-2.0/schemas', ['data/com.ubuntu-tweak.tweak.gschema.xml']),
          ('share/unity/lenses/tweak/', ['data/tweak.lens']),
          ('share/ubuntu-tweak/ui/', glob.glob('data/ui/*.ui')),
          ('share/ubuntu-tweak/pixmaps/', glob.glob('data/pixmaps/*.png')),
          ('share/ubuntu-tweak/scripts/', glob.glob('data/scripts/*')),
          ('share/ubuntu-tweak/templates/', glob.glob('data/templates/*')),
          ('share/ubuntu-tweak/', ['data/script-worker', 'data/uturl', 'data/ubuntu-tweak-daemon',
                                   'data/unity-lens-tweak']),
          ],
      license='GNU GPL',
      platforms='linux',
      test_suite='tests',
)
