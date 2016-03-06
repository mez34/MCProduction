from CRABClient.UserUtilities import config
config = config()
config.JobType.allowUndistributedCMSSW = True
config.General.requestName = 'MonoHgg_Zp2HDM_MZP600_13TeV_miniAODv2_76X'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EXO-RunIIFall15MiniAODv2-Zp2HDM_MZP600_1_cfg.py'
config.Data.inputDataset = '/MonoHgg_Zp2HDM_MZP600_13TeV_76X/mzientek-MonoHgg_Zp2HDM_MZP600_13TeV_76X-43969d768c4f72c55ce15f193cfffc77/USER'

config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_Zp2HDM_MZP600_13TeV_76X_miniAODv2'

config.section_('User')
config.section_('Site')
config.Site.whitelist = ["T2_CH_CERN"]
config.Site.storageSite = 'T2_CH_CERN'
