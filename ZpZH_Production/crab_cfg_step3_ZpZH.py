from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV_step3'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_ZpZH.py'
config.Data.inputDataset = '/MonoHgg_2HDM_ZpZH_MZP600_13TeV/mzientek-MonoHgg_2HDM_ZpZH_MZP600_13TeV_step2-08c88d8c6462a788d65c7567052c2fbd/USER'

config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH_CERN"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHgg_2HDM_ZpZH_MZP600_13TeV_step3'
config.section_('User')
config.section_('Site')

config.Site.whitelist = ["T2_CH_CERN"]
config.Site.storageSite = 'T2_CH_CERN'
