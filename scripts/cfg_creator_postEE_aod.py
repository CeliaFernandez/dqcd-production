import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '2022postEE/{name}'
config.General.workArea = '2022postEE/{name}'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_postEE_skim_cfg.py'
config.JobType.maxMemoryMB = 3000
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/mmasciov/dqcd-samples/AODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'AODSIM_2022postEE'

config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Florida','T2_US_Nebraska','T2_US_Caltech','T2_US_Purdue', 'T2_US_UCSD']
config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    "scenarioA_mpi_12_mA_1p20_ctau_1000": "/scenarioA_mpi_12_mA_1p20_ctau_1000/mmasciov-scenarioA_mpi_12_mA_1p20_ctau_1000_2022postEE-9fde3cc31e6376df0c95839d63d71c55/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_1000": "/scenarioA_mpi_2_mA_0p67_ctau_1000/mmasciov-scenarioA_mpi_2_mA_0p67_ctau_1000_2022postEE-22efb66cde078fe5ce014a25a9b6d9d0/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_1000": "/scenarioA_mpi_4_mA_1p33_ctau_1000/mmasciov-scenarioA_mpi_4_mA_1p33_ctau_1000_2022postEE-7357338f88afc1390512c31fca75bc77/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_1000": "/scenarioA_mpi_5_mA_1p67_ctau_1000/mmasciov-scenarioA_mpi_5_mA_1p67_ctau_1000_2022postEE-37b846698d3b06f3b9397469cb57bfd8/USER",
    "scenarioA_mpi_6_mA_2_ctau_1000": "/scenarioA_mpi_6_mA_2_ctau_1000/mmasciov-scenarioA_mpi_6_mA_2_ctau_1000_2022postEE-68e2f3f786024f7f52b8d997842a93fb/USER",
    "scenarioA_mpi_7p50_mA_2p50_ctau_1000": "/scenarioA_mpi_7p50_mA_2p50_ctau_1000/mmasciov-scenarioA_mpi_7p50_mA_2p50_ctau_1000_2022postEE-2361fa64a45e1e7dd25590f33ef552d9/USER",
    "scenarioB1_mpi_12_mA_1p20_ctau_1000": "/scenarioB1_mpi_12_mA_1p20_ctau_1000/mmasciov-scenarioB1_mpi_12_mA_1p20_ctau_1000_2022postEE-4085e864ea2d360bc9b81bb00f71f653/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_1000": "/scenarioB1_mpi_2_mA_0p67_ctau_1000/mmasciov-scenarioB1_mpi_2_mA_0p67_ctau_1000_2022postEE-aca13f004b6e680f1852c8c033bbdde3/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_1000": "/scenarioB1_mpi_4_mA_1p33_ctau_1000/mmasciov-scenarioB1_mpi_4_mA_1p33_ctau_1000_2022postEE-59e616efd7dcc96705034f3951bca811/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_1000": "/scenarioB1_mpi_5_mA_1p67_ctau_1000/mmasciov-scenarioB1_mpi_5_mA_1p67_ctau_1000_2022postEE-0cb45119dbde112629741e8d60bed98e/USER",
    "scenarioB1_mpi_6_mA_2_ctau_1000": "/scenarioB1_mpi_6_mA_2_ctau_1000/mmasciov-scenarioB1_mpi_6_mA_2_ctau_1000_2022postEE-9e58c09853d0619413574819b9408fdf/USER",
    "scenarioB1_mpi_7p50_mA_2p50_ctau_1000": "/scenarioB1_mpi_7p50_mA_2p50_ctau_1000/mmasciov-scenarioB1_mpi_7p50_mA_2p50_ctau_1000_2022postEE-4db0050299428e8fc96157ea92f1b4d9/USER"
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    # print(name)
    if os.path.exists(f"2022postEE/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2022postEE/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2022postEE/crab_submit_%s.py" % name)

