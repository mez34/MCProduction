from CRABClient.UserUtilities import config
config = config()
config.JobType.allowUndistributedCMSSW = True
config.General.requestName = 'MonoHgg_2HDM_MZP2000_MA0300_13TeV_step2'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'step2.py'
config.Data.inputDataset = '/MonoHgg_2HDM_MZP2000_A0300_13TeV/mzientek-2HDM_MZP2000_A0300_Hgg_step1-372f9c2c084c1ab6a6f1dce2f34b05c3/USER'
config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/mzientek/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = '2HDM_MZP2000_A0300_Hgg_step2'
#config.Data.userInputFiles = list(open('Higgs_scalar_nohdecay_gg_1GeV_13TeV_v1.txt'))

config.section_('User')
config.section_('Site')
config.Site.whitelist = ["T2_CH_CERN"]
config.Site.storageSite = 'T2_CH_CERN'
