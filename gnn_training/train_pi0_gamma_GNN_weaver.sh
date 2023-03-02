NAME="fccee_pi_vs_gamma_simpler"
YAML="weaverConfigs/${NAME}.yaml"
INPUTDIR=" /afs/cern.ch/user/h/helsens/public/4Michele/"
OUTPUTDIR="/afs/cern.ch/user/b/brfranco/work/public/Fellow/FCCSW/221123/LAr_scripts/machineLearning/"

#weaver --data-train ${INPUTDIR}/*train*.root  --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models/${NAME} --num-workers 1 --gpus 0 --batch-size 216 --start-lr 5e-3 --num-epochs 1 --optimizer ranger  --fetch-step 0.025
#weaver --data-train /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220623_pi0_flat_1_100_noNoise_caloReco_withVariablesForGNN/fccsw_output_pdgID_111_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130_jobid_1.root /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220618_gamma_flat_1_100_noNoise_caloReco_withVariablesForGNN/fccsw_output_pdgID_22_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130_jobid_1.root --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models/${NAME} --num-workers 1 --gpus "" --batch-size 216 --start-lr 5e-3 --num-epochs 1 --optimizer ranger  --fetch-step 0.025

#GPU condor
#weaver --data-train /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220623_pi0_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_111_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220618_gamma_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_22_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models/${NAME} --num-workers 1 --gpus 0 --batch-size 216 --start-lr 5e-3 --num-epochs 1 --optimizer ranger  --fetch-step 0.025
#CPU
#weaver --data-train /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220623_pi0_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_111_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220618_gamma_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_22_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models/${NAME} --num-workers 1 --gpus "" --batch-size 216 --start-lr 5e-3 --num-epochs 1 --optimizer ranger  --fetch-step 0.025
#GPU FCC
weaver --data-train /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220623_pi0_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_111_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220618_gamma_flat_1_100_noNoise_caloReco_withVariablesForGNN_fullStat_withLabel/fccsw_output_pdgID_22_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130.root --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models_theta_phi/${NAME} --num-workers 1 --gpus 0 --batch-size 64 --start-lr 5e-3 --num-epochs 2 --optimizer ranger  --fetch-step 0.025
#GPU FCC not full stat
#weaver --data-train /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220623_pi0_flat_1_100_noNoise_caloReco_withVariablesForGNN_withLabel/fccsw_output_pdgID_111_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130_jobid_1.root /eos/user/b/brfranco/rootfile_storage/fcc_analysis_ouput/220618_gamma_flat_1_100_noNoise_caloReco_withVariablesForGNN_withLabel/fccsw_output_pdgID_22_pMin_1000_pMax_100000_thetaMin_50_thetaMax_130_jobid_1.root --data-config ${YAML} --network-config weaverConfigs/particle_net_fccee.py --model-prefix weaver_models_theta_phi/${NAME} --num-workers 1 --gpus 0 --batch-size 64 --start-lr 5e-3 --num-epochs 1 --optimizer ranger  --fetch-step 0.025


#weaver --predict --data-test ${INPUTDIR}/*test*.root  --data-config ${YAML} --network-config networks/particle_net_fccee.py --model-prefix weaver_models/${NAME}_best_epoch_state.pt --num-workers 1 --gpus 0 --batch-size 512 --fetch-step 0.025 --predict-output ${OUTPUTDIR}/${NAME}.root
