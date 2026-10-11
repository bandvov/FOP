baseline_scenarios = {
    # 1. Baselines
    "Untreated_Classic_FOP": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Wild_Type": {
        "mut": 1.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 2. Gene silencing only
    "Silencing_Mild_0.30": {
        "mut": 5.0, "sil": 0.30, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Silencing_Strong_0.10": {
        "mut": 5.0, "sil": 0.10, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Silencing_Deep_0.05": {
        "mut": 5.0, "sil": 0.05, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 3. Kinase / pathway inhibition
    "Kinase_Inh_0.40": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.40, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Kinase_Strong_0.20": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.20, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "NonCanonical_Inh_0.30": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 0.30,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 4. Combinations of silencing + inhibition
    "Sil_015_Kin_0.40": {
        "mut": 5.0, "sil": 0.15, "inh_k": 0.40, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Sil_010_Kin_030_NC_0.40": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 5. Protective genetic modifiers
    "Mild_Protective_Modifier": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.45, "prot_phos": 1.8, "prot_fap": 0.55,
        "prot_noncan": 0.60, "prot_repair": 1.6,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Strong_Protective_Modifier": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.30, "prot_phos": 2.2, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 2.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 6. Gene therapy (realistic delivery)
    "GT_Ideal_100pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 1.00, "gt_onset": 20.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.02
    },

    "GT_Realistic_55pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "GT_LowEff_30pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.30, "gt_onset": 20.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.012, "residual_activity": 0.10
    },

    # 7. Gene therapy + pharmacological bridge
    "GT_55pct_Kinase_Bridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.35, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "GT_55pct_Strong_Bridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.25, "inh_noncan": 0.50,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    # 8. Combined advanced strategies
    "Protective_Mild_GT_55pct": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.45, "prot_phos": 1.8, "prot_fap": 0.55,
        "prot_noncan": 0.60, "prot_repair": 1.6,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    "Deep_Sil_Protective_Mild": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.70, "prot_repair": 1.5,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "Ultimate_Combo": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.35, "inh_noncan": 0.50,
        "prot_inflam": 0.40, "prot_phos": 1.7, "prot_fap": 0.50,
        "prot_noncan": 0.55, "prot_repair": 1.7,
        "gt_efficiency": 0.60, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },
    "GTDeepSil_MildProt": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.70, "prot_repair": 1.5,
        "gt_efficiency": 0.60, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.06
    },

    "GTKinBridge_Prot": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.30, "inh_noncan": 0.60,
        "prot_inflam": 0.55, "prot_phos": 1.5, "prot_fap": 0.65,
        "prot_noncan": 0.75, "prot_repair": 1.4,
        "gt_efficiency": 0.70, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.05
    },

    "EarlyGT_HighEff_Permanent": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.85, "gt_onset": 5.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.001, "residual_activity": 0.03
    },

    "SilGTKin025": {
        "mut": 5.0, "sil": 0.15, "inh_k": 0.25, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.007, "residual_activity": 0.07
    },

    "Maximal_Buffering": {
        "mut": 5.0, "sil": 0.12, "inh_k": 0.40, "inh_noncan": 0.45,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.9,
        "gt_efficiency": 0.50, "gt_onset": 25.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "Late_GT_Strong_Pharma": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.20, "inh_noncan": 0.35,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.65, "gt_onset": 40.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.06
    },

    "Protective_GT_NoPharma": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.40, "prot_phos": 1.9, "prot_fap": 0.50,
        "prot_noncan": 0.55, "prot_repair": 1.8,
        "gt_efficiency": 0.60, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "Balanced_MultiModal": {
        "mut": 5.0, "sil": 0.18, "inh_k": 0.45, "inh_noncan": 0.55,
        "prot_inflam": 0.60, "prot_phos": 1.4, "prot_fap": 0.70,
        "prot_noncan": 0.80, "prot_repair": 1.3,
        "gt_efficiency": 0.50, "gt_onset": 22.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.007, "residual_activity": 0.08
    },

    "Aggressive_Cure_Seeking": {
        "mut": 5.0, "sil": 0.05, "inh_k": 0.25, "inh_noncan": 0.30,
        "prot_inflam": 0.35, "prot_phos": 1.8, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 1.5,
        "gt_efficiency": 0.75, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "Conservative_Safe": {
        "mut": 5.0, "sil": 0.25, "inh_k": 0.55, "inh_noncan": 0.70,
        "prot_inflam": 0.70, "prot_phos": 1.3, "prot_fap": 0.80,
        "prot_noncan": 0.85, "prot_repair": 1.4,
        "gt_efficiency": 0.45, "gt_onset": 30.0, "gt_rise_time": 12.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.09
    },
    "Early_GTPermanent": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.90, "gt_onset": 8.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.001, "residual_activity": 0.02
    },

    "GTSilKin030": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.30, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.65, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.05
    },

    "StrongProt_GTNoDrug": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.30, "prot_phos": 2.1, "prot_fap": 0.40,
        "prot_noncan": 0.45, "prot_repair": 2.0,
        "gt_efficiency": 0.50, "gt_onset": 15.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.06
    },

    "SilGTBridge": {
        "mut": 5.0, "sil": 0.05, "inh_k": 0.28, "inh_noncan": 0.50,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.70, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "Pulsed_Pharma_GT55": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.35, "inh_noncan": 0.45,
        "prot_inflam": 0.65, "prot_phos": 1.4, "prot_fap": 0.70,
        "prot_noncan": 0.75, "prot_repair": 1.3,
        "gt_efficiency": 0.55, "gt_onset": 25.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.07
    },

    "DeepSil_StrongProt_NoGT": {
        "mut": 5.0, "sil": 0.06, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.42,
        "prot_noncan": 0.48, "prot_repair": 1.9,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "GTMildProt_LowDrug": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.60, "inh_noncan": 0.75,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.55,
        "prot_noncan": 0.65, "prot_repair": 1.6,
        "gt_efficiency": 0.80, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "Triple_Sil_Kin_NC": {
        "mut": 5.0, "sil": 0.12, "inh_k": 0.30, "inh_noncan": 0.35,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    "GTSilProtMild": {
        "mut": 5.0, "sil": 0.15, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.48, "prot_phos": 1.7, "prot_fap": 0.58,
        "prot_noncan": 0.62, "prot_repair": 1.55,
        "gt_efficiency": 0.60, "gt_onset": 16.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "Late_HighEff_GT_StrongBridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.22, "inh_noncan": 0.30,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.75, "gt_onset": 45.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "Balanced_Four_Pillars": {
        "mut": 5.0, "sil": 0.18, "inh_k": 0.40, "inh_noncan": 0.50,
        "prot_inflam": 0.55, "prot_phos": 1.5, "prot_fap": 0.65,
        "prot_noncan": 0.70, "prot_repair": 1.4,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.07
    },

    "Minimal_Drug_Max_Genetics": {
        "mut": 5.0, "sil": 0.08, "inh_k": 0.80, "inh_noncan": 0.85,
        "prot_inflam": 0.32, "prot_phos": 2.2, "prot_fap": 0.38,
        "prot_noncan": 0.42, "prot_repair": 2.1,
        "gt_efficiency": 0.65, "gt_onset": 12.0, "gt_rise_time": 7.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.04
    },

    "Aggressive_Early_Intervention": {
        "mut": 5.0, "sil": 0.07, "inh_k": 0.25, "inh_noncan": 0.30,
        "prot_inflam": 0.40, "prot_phos": 1.8, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.6,
        "gt_efficiency": 0.80, "gt_onset": 5.0, "gt_rise_time": 5.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "Safe_LongTerm_Maintenance": {
        "mut": 5.0, "sil": 0.22, "inh_k": 0.50, "inh_noncan": 0.65,
        "prot_inflam": 0.65, "prot_phos": 1.4, "prot_fap": 0.75,
        "prot_noncan": 0.80, "prot_repair": 1.5,
        "gt_efficiency": 0.40, "gt_onset": 30.0, "gt_rise_time": 14.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.08
    },

    "GTSilStrongProt": {
        "mut": 5.0, "sil": 0.10, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.35, "prot_phos": 2.0, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.9,
        "gt_efficiency": 0.55, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "HighEff_GT_NoSil_MildBridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.45, "inh_noncan": 0.60,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.85, "gt_onset": 10.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    "Layered_Protection": {
        "mut": 5.0, "sil": 0.14, "inh_k": 0.35, "inh_noncan": 0.40,
        "prot_inflam": 0.42, "prot_phos": 1.9, "prot_fap": 0.48,
        "prot_noncan": 0.52, "prot_repair": 1.75,
        "gt_efficiency": 0.50, "gt_onset": 22.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.005, "residual_activity": 0.06
    },

    "Rescue_After_Progression": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.20, "inh_noncan": 0.25,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.65, "prot_repair": 1.4,
        "gt_efficiency": 0.70, "gt_onset": 50.0, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.004, "residual_activity": 0.05
    },

    "Ultra_Conservative": {
        "mut": 5.0, "sil": 0.30, "inh_k": 0.65, "inh_noncan": 0.80,
        "prot_inflam": 0.75, "prot_phos": 1.25, "prot_fap": 0.85,
        "prot_noncan": 0.90, "prot_repair": 1.3,
        "gt_efficiency": 0.35, "gt_onset": 35.0, "gt_rise_time": 15.0,
        "gt_escape_rate": 0.003, "residual_activity": 0.10
    },

    "Theoretical_Optimum": {
        "mut": 5.0, "sil": 0.08, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 0.38, "prot_phos": 1.85, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.8,
        "gt_efficiency": 0.75, "gt_onset": 8.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },
}
