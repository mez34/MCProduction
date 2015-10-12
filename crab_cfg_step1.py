from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_MZP600_MA0300_13TeV'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.inputFiles = ['MZP600_MA0300.lhe']
#['/afs/cern.ch/user/m/mzientek/public/MZP600_MA0300.lhe']
#['/store/group/phys_exotica/monoHiggs/Zp2HDM/MZP600_MA0300.lhe']
#['/afs/cern.ch/user/m/mzientek/private/CMSSW_7_1_14/LHEFiles/2HDM/MZP600_MA0300.lhe']

config.Data.primaryDataset = 'MonoHgg_2HDM_MZP600_A0300_13TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/mzientek/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = '2HDM_MZP600_A0300_Hgg_step1'

#config.Site.blacklist = ["T2_US_UCSD"]
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'

