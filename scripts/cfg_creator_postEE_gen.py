import os

p = "Configuration/GenProduction/data/"
files = os.listdir(p)

cmnd = """
    cmsDriver.py Configuration/GenProduction/python/{name}_cfi.py --python_filename 2022postEE-final/gen_{name}_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:gen_{name}.root --conditions 124X_mcRun3_2022_realistic_postEE_v3 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN --geometry DB:Extended --era Run3 --no_exec --mc -n -1
"""

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2022postEE-final/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '2022/gen_{name}_cfg.py'

config.Data.outputPrimaryDataset = '{name}'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 2000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/$USER/samples/'
config.Data.publication = True
config.Data.outputDatasetTag = '{name}_2022postEE'

config.Site.blacklist = ['T2_US_MIT']
config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Florida', 'T2_US_UCSD']
config.Site.storageSite = 'T2_US_UCSD'
"""

files = [
    #"scenarioA_mpi_2_mA_0p67_ctau_250p0.slha",
    #"scenarioA_mpi_2_mA_0p67_ctau_600p0.slha",
    "scenarioA_mpi_2_mA_0p67_ctau_1000.slha",
    #"scenarioA_mpi_4_mA_1p33_ctau_250p0.slha",
    #"scenarioA_mpi_4_mA_1p33_ctau_600p0.slha",
    "scenarioA_mpi_4_mA_1p33_ctau_1000.slha",
    #"scenarioA_mpi_5_mA_1p67_ctau_250p0.slha",
    #"scenarioA_mpi_5_mA_1p67_ctau_600p0.slha",
    "scenarioA_mpi_5_mA_1p67_ctau_1000.slha",
    #"scenarioA_mpi_6_mA_2_ctau_250p0.slha",
    #"scenarioA_mpi_6_mA_2_ctau_600p0.slha",
    "scenarioA_mpi_6_mA_2_ctau_1000.slha",
    #"scenarioA_mpi_7p50_mA_2p50_ctau_250p0.slha",
    #"scenarioA_mpi_7p50_mA_2p50_ctau_600p0.slha",
    "scenarioA_mpi_7p50_mA_2p50_ctau_1000.slha",
    #"scenarioA_mpi_12_mA_1p20_ctau_250p0.slha",
    #"scenarioA_mpi_12_mA_1p20_ctau_600p0.slha",
    "scenarioA_mpi_12_mA_1p20_ctau_1000.slha",
    #"scenarioB1_mpi_2_mA_0p67_ctau_250p0.slha",
    #"scenarioB1_mpi_2_mA_0p67_ctau_600p0.slha",
    "scenarioB1_mpi_2_mA_0p67_ctau_1000.slha",
    #"scenarioB1_mpi_4_mA_1p33_ctau_250p0.slha",
    #"scenarioB1_mpi_4_mA_1p33_ctau_600p0.slha",
    "scenarioB1_mpi_4_mA_1p33_ctau_1000.slha",
    #"scenarioB1_mpi_5_mA_1p67_ctau_250p0.slha",
    #"scenarioB1_mpi_5_mA_1p67_ctau_600p0.slha",
    "scenarioB1_mpi_5_mA_1p67_ctau_1000.slha",
    #"scenarioB1_mpi_6_mA_2_ctau_250p0.slha",
    #"scenarioB1_mpi_6_mA_2_ctau_600p0.slha",
    "scenarioB1_mpi_6_mA_2_ctau_1000.slha",
    #"scenarioB1_mpi_7p50_mA_2p50_ctau_250p0.slha",
    #"scenarioB1_mpi_7p50_mA_2p50_ctau_600p0.slha",
    "scenarioB1_mpi_7p50_mA_2p50_ctau_1000.slha",
    #"scenarioB1_mpi_12_mA_1p20_ctau_250p0.slha",
    #"scenarioB1_mpi_12_mA_1p20_ctau_600p0.slha",
    "scenarioB1_mpi_12_mA_1p20_ctau_1000.slha",
    #
]



for f in files:
    name = f.split(".")[0]
    if os.path.exists(f"2022postEE-final/{name}/crab_{name}"):
        continue
    print("Launching", name)
    # continue
    # print(cmnd.format(name=name))
    # print(name)
    os.system(cmnd.format(name=name))
    with open("2022postEE-final/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name))
    os.system("crab submit 2022postEE-final/crab_submit_%s.py" % name)

