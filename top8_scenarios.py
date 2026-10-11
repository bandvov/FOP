top8_scenarios = {
    # 1. Best pure silencing (from your large run)
    "Deep_Silencing_0.08": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 2. Best combination from your 100k run
    "Sil0.15_Kin0.40": {
        "mut": 5.0, "sil": 0.15, "inh_k": 0.40, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 3. Strong multi-node (highest HO suppression in your run)
    "Strong_Multi": {
        "mut": 5.0, "sil": 0.10, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 4. Deep silencing + mild protective background
    "DeepSil_MildProtective": {
        "mut": 5.0, "sil": 0.08, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 0.50, "prot_phos": 1.6, "prot_fap": 0.60,
        "prot_noncan": 0.70, "prot_repair": 1.5,
        "gt_efficiency": 0.0, "gt_onset": 9999, "gt_rise_time": 8.0,
        "gt_escape_rate": 0.0, "residual_activity": 0.05
    },

    # 5. Realistic gene therapy + moderate silencing
    "GT55_Sil0.12": {
        "mut": 5.0, "sil": 0.12, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 18.0, "gt_rise_time": 9.0,
        "gt_escape_rate": 0.006, "residual_activity": 0.06
    },

    # 6. Realistic GT + kinase bridge (practical translational strategy)
    "GT55_Kinase_Bridge": {
        "mut": 5.0, "sil": 1.0, "inh_k": 0.35, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.55, "gt_onset": 20.0, "gt_rise_time": 10.0,
        "gt_escape_rate": 0.008, "residual_activity": 0.08
    },

    # 7. High-efficiency early gene therapy
    "Early_GT80_Permanent": {
        "mut": 5.0, "sil": 1.0, "inh_k": 1.0, "inh_noncan": 1.0,
        "prot_inflam": 1.0, "prot_phos": 1.0, "prot_fap": 1.0,
        "prot_noncan": 1.0, "prot_repair": 1.0,
        "gt_efficiency": 0.80, "gt_onset": 8.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },

    # 8. Theoretical best multi-modal (from advanced set)
    "Theoretical_Optimum": {
        "mut": 5.0, "sil": 0.08, "inh_k": 0.30, "inh_noncan": 0.40,
        "prot_inflam": 0.38, "prot_phos": 1.85, "prot_fap": 0.45,
        "prot_noncan": 0.50, "prot_repair": 1.8,
        "gt_efficiency": 0.75, "gt_onset": 8.0, "gt_rise_time": 6.0,
        "gt_escape_rate": 0.002, "residual_activity": 0.03
    },
}
