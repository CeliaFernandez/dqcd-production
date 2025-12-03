import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '2022/{name}'
config.General.workArea = '2022/{name}'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_cfg_skim.py'
config.JobType.maxMemoryMB = 3000
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/mmasciov/dqcd-samples/AODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'AODSIM_2022-final'

config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Florida','T2_US_Nebraska','T2_US_Caltech','T2_US_Purdue', 'T2_US_UCSD']
config.Site.storageSite = 'T2_US_UCSD'
"""


datasets = {
    "scenarioA_mpi_12_mA_1p20_ctau_1000": "/scenarioA_mpi_12_mA_1p20_ctau_1000/mmasciov-scenarioA_mpi_12_mA_1p20_ctau_1000_2022-3c3edc919e7c4668e1ab9290e5275a95/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_1000": "/scenarioA_mpi_2_mA_0p67_ctau_1000/mmasciov-scenarioA_mpi_2_mA_0p67_ctau_1000_2022-9117bc358dec59e63135080854cf2478/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_1000": "/scenarioA_mpi_4_mA_1p33_ctau_1000/mmasciov-scenarioA_mpi_4_mA_1p33_ctau_1000_2022-55899c43e6b6776961f2faaae3a6c05c/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_1000": "/scenarioA_mpi_5_mA_1p67_ctau_1000/mmasciov-scenarioA_mpi_5_mA_1p67_ctau_1000_2022-0380d94853290679e84b1e5add533534/USER",
    "scenarioA_mpi_6_mA_2_ctau_1000": "/scenarioA_mpi_6_mA_2_ctau_1000/mmasciov-scenarioA_mpi_6_mA_2_ctau_1000_2022-36156b5ae2ad240e0af78eb06727803a/USER",
    "scenarioA_mpi_7p50_mA_2p50_ctau_1000": "/scenarioA_mpi_7p50_mA_2p50_ctau_1000/mmasciov-scenarioA_mpi_7p50_mA_2p50_ctau_1000_2022-825825fb24ddc4f3a66c5f8c2d822709/USER",
    "scenarioB1_mpi_12_mA_1p20_ctau_1000": "/scenarioB1_mpi_12_mA_1p20_ctau_1000/mmasciov-scenarioB1_mpi_12_mA_1p20_ctau_1000_2022-866aa73572dc953161cb1166731afe1b/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_1000": "/scenarioB1_mpi_2_mA_0p67_ctau_1000/mmasciov-scenarioB1_mpi_2_mA_0p67_ctau_1000_2022-54a1c975abb4c7b82cd4e24ed2fc5a56/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_1000": "/scenarioB1_mpi_4_mA_1p33_ctau_1000/mmasciov-scenarioB1_mpi_4_mA_1p33_ctau_1000_2022-1ed602d2c83d952e0f7187f9e8584944/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_1000": "/scenarioB1_mpi_5_mA_1p67_ctau_1000/mmasciov-scenarioB1_mpi_5_mA_1p67_ctau_1000_2022-7479e51b961544d6c66b008a70bae9df/USER",
    "scenarioB1_mpi_6_mA_2_ctau_1000": "/scenarioB1_mpi_6_mA_2_ctau_1000/mmasciov-scenarioB1_mpi_6_mA_2_ctau_1000_2022-d62efb42a097d0667004ec3b1320082c/USER",
    "scenarioB1_mpi_7p50_mA_2p50_ctau_1000": "/scenarioB1_mpi_7p50_mA_2p50_ctau_1000/mmasciov-scenarioB1_mpi_7p50_mA_2p50_ctau_1000_2022-7d9c5fc6b6ccbb36bdb206a640eea33a/USER"
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    print(name)
    if os.path.exists(f"2022/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2022/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2022/crab_submit_%s.py" % name)

