# MCProduction

////////////////////////////////////////////////////////////////////////

//      FOR miniAODv1

////////////////////////////////////////////////////////////////////////

STEP1 : (in CMSSW_7_4_1)
- cmsRun step1.py (GEN-SIM)
- use crab_cfg_step1.py to submit via crab
- ALWAYS check when submitting crab that the input LHE is correct in step1.py 
(This is a bug that should be fixed at some point).   

STEP2 : (in CMSSW_7_4_1)
- cmsRun step2.py 
- use crab_cfg_step2.py to submit via crab

STEP3 : (in CMSSW_7_4_1_patch4) *
- cmsRun step3_v2.py
- use crab_cfg_step3_v2.py to submit via crab

STEP4 : (in CMSSW_7_4_14)
- cmsRun step4_v2.py
- use crab_cfg_step4_v2.py to submit via crab



////////////////////////////////////////////////////////////////////////

//      FOR miniAODv1

////////////////////////////////////////////////////////////////////////

STEP1 and STEP2 are the same. 
However, STEP3 should be in CMSSW_7_4_1
- cmsRun step3.py
- use crab_cfg_step3.py to submit via crab 

