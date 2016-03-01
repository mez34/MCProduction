# MCProduction

////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////

      FOR: 76X miniAODv2

////////////////////////////////////////////////////////////////////////

GEN-SIM: (in CMSSW_7_1_21_patch1)
- specify input LHE file
- cmsRun EXO-step1GS_Zp2HDM.py
- crab submit crab_cfg_step1GS_Zp2HDM.py 

DIGI-RECO: (in CMSSW_7_6_1)
 step1:
- cmsRun EXO-step1DR_Zp2HDM.py

 step2: 
- cmsRun EXO-step2DR_Zp2HDM.py


MiniAODv2: (in CMSSW_7_6_3)
- cmsRun EXO-miniAODv2_Zp2HDM.py

////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////

Directions came from David Sheffield:
You can find examples of the cmsDriver.py sequences you'll need to use in the below links. 
Now using 7_1_21_patch1 instead of 7_1_20.

Convert LHE to root file https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIIWinter15pLHE-01893 
Change lhe:number for file:your.lhe

GEN-SIM https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIISummer15GS-02086
Changed the default hadronization to Pythia8 

DIGI-RECO https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIIFall15DR76-01651

MiniAODv2 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIIFall15MiniAODv2-01376

////////////////////////////////////////////////////////////////////////

