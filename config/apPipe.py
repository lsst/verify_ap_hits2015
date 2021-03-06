# Config override for lsst.ap.pipe.ApPipeTask
import os.path
from lsst.utils import getPackageDir

configDir = os.path.dirname(__file__)
decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

config.ccdProcessor.load(os.path.join(decamConfigDir, "processCcd.py"))

# Use dataset's reference catalogs
config.ccdProcessor.calibrate.load(os.path.join(configDir, 'calibrate.py'))

# Use dataset's specific templates
config.differencer.load(os.path.join(configDir, 'imageDifference.py'))
