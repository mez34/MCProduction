from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV_step1'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'step1_ZpZH.py'
#config.JobType.inputFiles = [fileNames=cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/user/mzientek/cmsgrid_final.lhe']

config.Data.outputPrimaryDataset = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/mzientek/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_2HDM_ZpZH_MZP600_Hgg_step1'

#config.Site.blacklist = ["T2_US_UCSD"]
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'

