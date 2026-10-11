baseline_scenarios = {
    # 1. Baselines
    "01_Untreated_Classic_FOP": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "02_Wild_Type": {
        "mut": 1.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 2. Gene silencing only
    "03_Silencing_Mild_0.30": {
        "mut": 5.0, "sil": 0.30, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "04_Silencing_Strong_0.10": {
        "mut": 5.0, "sil": 0.10, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "05_Silencing_Deep_0.05": {
        "mut": 5.0, "sil": 0.05, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 3. Kinase / pathway inhibition
    "06_Kinase_Inh_0.40": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.40, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "07_Kinase_Strong_0.20": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.20, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "08_NonCanonical_Inh_0.30": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 0.30,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 4. Combinations of silencing + inhibition
    "09_Sil_0.15_Kin_0.40": {
        "mut": 5.0, "sil": 0.15, "inh_k": 0.40, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "10_Sil_0.10_Kin_0.30_NC_0.40": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 5. Protective genetic modifiers
    "11_Mild_Protective_Modifier": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.45, "prot_phos": 1.8, "prot_fap": 0.55,
        "prot_noncan": 0.60, "prot_repair": 1.6,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "12_Strong_Protective_Modifier": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.30, "prot_phos": 2.2, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 2.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 6. Gene therapy (realistic delivery)
    "13_GT_Ideal_100pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 1.00, "gt_onset": 20.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.02
    },

    "14_GT_Realistic_55pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "15_GT_LowEff_30pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.30, "gt_onset": 20.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.012, "residual_activity": 0.10
    },

    # 7. Gene therapy + pharmacological bridge
    "16_GT_55pct_Kinase_Bridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.35, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "17_GT_55pct_Strong_Bridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.25, "inh_noncan": 0.50,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    # 8. Combined advanced strategies
    "18_Protective_Mild_GT_55pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.45, "prot_phos": 1.8, "prot_fap": 0.55,
        "prot_noncan": 0.60, "prot_repair": 1.6,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "19_Deep_Sil_Protective_Mild": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.70, "prot_repair": 1.5,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "20_Ultimate_Combo": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.35, "inh_noncan": 0.50,
        "prot_inflam": 0.40, "prot_phos": 1.7, "prot_fap": 0.50,
        "prot_noncan": 0.55, "prot_repair": 1.7,
        "gt_efficiency": 0.60, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },
    "21_GT60_DeepSil_MildProt": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.70, "prot_repair": 1.5,
        "gt_efficiency": 0.60, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.06
    },

    "22_GT70_KinBridge_Prot": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.30, "inh_noncan": 0.60,
        "prot_inflam": 0.55, "prot_phos": 1.5, "prot_fap": 0.65,
        "prot_noncan": 0.75, "prot_repair": 1.4,
        "gt_efficiency": 0.70, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.05
    },

    "23_EarlyGT_HighEff_Permanent": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.85, "gt_onset": 5.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.001, "residual_activity": 0.03
    },

    "24_Sil015_GT55_Kin025": {
        "mut": 5.0, "sil": 0.15, "inh_k": 0.25, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.007, "residual_activity": 0.07
    },

    "25_Maximal_Buffering": {
        "mut": 5.0, "sil": 0.12, "inh_k": 0.40, "inh_noncan": 0.45,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.9,
        "gt_efficiency": 0.50, "gt_onset": 25.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "26_Late_GT_Strong_Pharma": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.20, "inh_noncan": 0.35,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.65, "gt_onset": 40.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.06
    },

    "27_Protective_GT_NoPharma": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.40, "prot_phos": 1.9, "prot_fap": 0.50,
        "prot_noncan": 0.55, "prot_repair": 1.8,
        "gt_efficiency": 0.60, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "28_Balanced_MultiModal": {
        "mut": 5.0, "sil": 0.18, "inh_k": 0.45, "inh_noncan": 0.55,
        "prot_inflam": 0.60, "prot_phos": 1.4, "prot_fap": 0.70,
        "prot_noncan": 0.80, "prot_repair": 1.3,
        "gt_efficiency": 0.50, "gt_onset": 22.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.007, "residual_activity": 0.08
    },

    "29_Aggressive_Cure_Seeking": {
        "mut": 5.0, "sil": 0.05, "inh_k": 0.25, "inh_noncan": 0.30,
        "prot_inflam": 0.35, "prot_phos": 1.8, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 1.5,
        "gt_efficiency": 0.75, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "30_Conservative_Safe": {
        "mut": 5.0, "sil": 0.25, "inh_k": 0.55, "inh_noncan": 0.70,
        "prot_inflam": 0.70, "prot_phos": 1.3, "prot_fap": 0.80,
        "prot_noncan": 0.85, "prot_repair": 1.4,
        "gt_efficiency": 0.45, "gt_onset": 30.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.09
    },
    "31_Early_GT90_Permanent": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.90, "gt_onset": 8.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.001, "residual_activity": 0.02
    },

    "32_GT65_Sil010_Kin030": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.30, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.65, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.05
    },

    "33_StrongProt_GT50_NoDrug": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.30, "prot_phos": 2.1, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 2.0,
        "gt_efficiency": 0.50, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.06
    },

    "34_Sil005_GT70_Bridge": {
        "mut": 5.0, "sil": 0.05, "inh_k": 0.28, "inh_noncan": 0.50,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.70, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "35_Pulsed_Pharma_GT55": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.35, "inh_noncan": 0.45,
        "prot_inflam": 0.65, "prot_phos": 1.4, "prot_fap": 0.70,
        "prot_noncan": 0.75, "prot_repair": 1.3,
        "gt_efficiency": 0.55, "gt_onset": 25.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.07
    },

    "36_DeepSil_StrongProt_NoGT": {
        "mut": 5.0, "sil": 0.06, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.42,
        "prot_noncan": 0.48, "prot_repair": 1.9,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "37_GT80_MildProt_LowDrug": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.60, "inh_noncan": 0.75,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.55,
        "prot_noncan": 0.65, "prot_repair": 1.6,
        "gt_efficiency": 0.80, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "38_Triple_Sil_Kin_NC": {
        "mut": 5.0, "sil": 0.12, "inh_k": 0.30, "inh_noncan": 0.35,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "39_GT60_Sil015_ProtMild": {
        "mut": 5.0, "sil": 0.15, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.48, "prot_phos": 1.7, "prot_fap": 0.58,
        "prot_noncan": 0.62, "prot_repair": 1.55,
        "gt_efficiency": 0.60, "gt_onset": 16.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "40_Late_HighEff_GT_StrongBridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.22, "inh_noncan": 0.30,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.75, "gt_onset": 45.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "41_Balanced_Four_Pillars": {
        "mut": 5.0, "sil": 0.18, "inh_k": 0.40, "inh_noncan": 0.50,
        "prot_inflam": 0.55, "prot_phos": 1.5, "prot_fap": 0.65,
        "prot_noncan": 0.70, "prot_repair": 1.4,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.07
    },

    "42_Minimal_Drug_Max_Genetics": {
        "mut": 5.0, "sil": 0.08, "inh_k": 0.80, "inh_noncan": 0.85,
        "prot_inflam": 0.32, "prot_phos": 2.2, "prot_fap": 0.38,
        "prot_noncan": 0.42, "prot_repair": 2.1,
        "gt_efficiency": 0.65, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "43_Aggressive_Early_Intervention": {
        "mut": 5.0, "sil": 0.07, "inh_k": 0.25, "inh_noncan": 0.30,
        "prot_inflam": 0.40, "prot_phos": 1.8, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.6,
        "gt_efficiency": 0.80, "gt_onset": 5.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "44_Safe_LongTerm_Maintenance": {
        "mut": 5.0, "sil": 0.22, "inh_k": 0.50, "inh_noncan": 0.65,
        "prot_inflam": 0.65, "prot_phos": 1.4, "prot_fap": 0.75,
        "prot_noncan": 0.80, "prot_repair": 1.5,
        "gt_efficiency": 0.40, "gt_onset": 30.0, "gt_rise_time": 14.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.08
    },

    "45_GT55_Sil010_StrongProt": {
        "mut": 5.0, "sil": 0.10, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.9,
        "gt_efficiency": 0.55, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "46_HighEff_GT_NoSil_MildBridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.45, "inh_noncan": 0.60,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.85, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "47_Layered_Protection": {
        "mut": 5.0, "sil": 0.14, "inh_k": 0.35, "inh_noncan": 0.40,
        "prot_inflam": 0.42, "prot_phos": 1.9, "prot_fap": 0.48,
        "prot_noncan": 0.52, "prot_repair": 1.75,
        "gt_efficiency": 0.50, "gt_onset": 22.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "48_Rescue_After_Progression": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.20, "inh_noncan": 0.25,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.65, "prot_repair": 1.4,
        "gt_efficiency": 0.70, "gt_onset": 50.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "49_Ultra_Conservative": {
        "mut": 5.0, "sil": 0.30, "inh_k": 0.65, "inh_noncan": 0.80,
        "prot_inflam": 0.75, "prot_phos": 1.25, "prot_fap": 0.85,
        "prot_noncan": 0.90, "prot_repair": 1.3,
        "gt_efficiency": 0.35, "gt_onset": 35.0, "gt_rise_time": 15.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.10
    },

    "50_Theoretical_Optimum": {
        "mut": 5.0, "sil": 0.08, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 0.38, "prot_phos": 1.85, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.8,
        "gt_efficiency": 0.75, "gt_onset": 8.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },
}
