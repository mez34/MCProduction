from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HDM_ZP600_A0300_13TeV'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1.py'
config.JobType.inputFiles = ['/afs/cern.ch/user/m/mzientek/private/CMSSW_7_1_14/LHEFiles/MZP600_MA0300.lhe']

config.Data.primaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFN = '/store/user/dburns/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = 'HDM_MZP600_A0300_gg_13TeV'

#config.Site.blacklist = ["T2_US_UCSD"]
config.Site.storageSite = 'T2_CH_CERN'
