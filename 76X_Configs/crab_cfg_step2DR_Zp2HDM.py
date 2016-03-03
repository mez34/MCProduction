from CRABClient.UserUtilities import config
config = config()
config.JobType.allowUndistributedCMSSW = True
config.General.requestName = 'MonoHgg_Zp2HDM_MZP600_13TeV_step2DR_76X_v2'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EXO-step2DR_Zp2HDM.py'
config.Data.inputDataset = '/MonoHgg_Zp2HDM_MZP600_13TeV_76X/mzientek-MonoHgg_Zp2HDM_MZP600_13TeV_76X-32f870ac2e5a27e6c7b243a0bfc25281/USER'

config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_Zp2HDM_MZP600_13TeV_76X_step2DR'

config.section_('User')
config.section_('Site')
config.Site.whitelist = ["T2_CH_CERN"]
config.Site.storageSite = 'T2_CH_CERN'
