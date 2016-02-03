from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV_miniAODv2'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_ZpZH.py'
config.Data.inputDataset = '/MonoHgg_2HDM_ZpZH_MZP600_13TeV/kmcdermo-MonoHgg_2HDM_ZpZH_MZP600_13TeV_step3-fb358e8852a60e2ae7f5961d9ec35138/USER'

config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH_CERN"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV_miniAODv2'
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'
