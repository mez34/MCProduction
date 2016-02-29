from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_MZP600_MA0300_13TeV_step3'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_RECO.py'
config.Data.inputDataset = '/MonoHgg_2HDM_MZP600_A0300_13TeV/mzientek-2HDM_MZP600_A0300_Hgg_step2-08c88d8c6462a788d65c7567052c2fbd/USER'
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH_CERN"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.publishDataName = '2HDM_MZP600_A0300_Hgg_step2-5'
#config.Data.userInputFiles = list(open('Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_RECO_v1.txt'))
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'
