from CRABClient.UserUtilities import config
config = config()
config.JobType.allowUndistributedCMSSW = True
config.General.requestName = 'MonoHgg_Zp2HDM_MZP600_13TeV_step1DR_76X'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EXO-step1DR_Zp2HDM.py'
config.Data.inputDataset = '/MonoHgg_Zp2HDM_MZP600_13TeV_76X/mzientek-MonoHgg_Zp2HDM_MZP600_13TeV_76X-a112f43e9dfd5ee88774e4feea6b64e7/USER'

config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_Zp2HDM_MZP600_13TeV_76X'

config.section_('User')
config.section_('Site')
config.Site.whitelist = ["T2_CH_CERN"]
config.Site.storageSite = 'T2_CH_CERN'
