from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MonoHgg_2HDM_MZP600_MA0300_13TeV_miniAODv2'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1_PAT.py'
config.Data.inputDataset = '/MonoHgg_2HDM_MZP600_A0300_13TeV/mzientek-2HDM_MZP600_A0300_Hgg_step2-5-fb358e8852a60e2ae7f5961d9ec35138/USER'
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH_CERN"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.publishDataName = '2HDM_MZP600_A0300_Hgg_miniAODv2'
#config.Data.userInputFiles = list(open('Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_RECO_v1.txt'))
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'
