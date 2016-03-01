from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_Zp2HDM_MZP600_13TeV_step1GS_76X'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'EXO-step1GS_Zp2HDM.py'
config.JobType.inputFiles = ['/afs/cern.ch/user/m/mzientek/public/MZP600_MA0300.lhe']

config.Data.outputPrimaryDataset = 'MonoHgg_Zp2HDM_MZP600_13TeV_76X'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_Zp2HDM_MZP600_13TeV_76X'

config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'

