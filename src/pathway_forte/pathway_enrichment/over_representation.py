# -*- coding: utf-8 -*-

"""This module contains the functions to run Over Representation Analysis (ORA)."""
import logging

import numpy as np
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests

log = logging.getLogger(__name__)


def _prepare_hypergeometric_test(query_gene_set, pathway_gene_set, gene_universe):
    """Prepare the matrix for hypergeometric test calculations.

    :param set[str] query_gene_set: gene set to test against pathway
    :param set[str] pathway_gene_set: pathway gene set
    :param int gene_universe: number of HGNC symbols
    :rtype: numpy.ndarray
    :return: 2x2 matrix
    """
    return np.array(
        [[len(query_gene_set.intersection(pathway_gene_set)),
          len(query_gene_set.difference(pathway_gene_set))
          ],
         [len(pathway_gene_set.difference(query_gene_set)),
          gene_universe - len(pathway_gene_set.union(query_gene_set))
          ]
         ]
    )


def perform_hypergeometric_test(
        genes_to_test, pathway_dict, gene_universe=42609, apply_threshold=False, threshold=0.01):
    """Perform hypergeometric tests.

    :param set[str] genes_to_test: gene set to test against pathway
    :param dict[str,set] pathway_dict: manager to pathways
    :param int gene_universe: number of HGNC symbols
    :param Optional[bool] apply_threshold: return only significant pathways
    :param Optional[float] threshold: significance threshold (by default 0.05)
    :rtype: dict[str,dict[str,dict]]
    :return: manager_pathways_dict with p value info
    """
    manager_p_values = dict()
    results = dict()

    for pathway_id, pathway_gene_set in pathway_dict.items():
        # Prepare the test table to conduct the fisher test
        test_table = _prepare_hypergeometric_test(genes_to_test, pathway_gene_set, gene_universe)

        # Calculate fisher test
        oddsratio, pvalue = fisher_exact(test_table, alternative='greater')

        manager_p_values[pathway_id] = pvalue

    # Split the dictionary into names_id tuples and p values to keep the same order
    manager_pathway_id, p_values = zip(*manager_p_values.items())
    correction_test = multipletests(p_values, method='fdr_bh')

    q_values = correction_test[1]

    # Update original dict with p value corrections
    for i, pathway_id in enumerate(manager_pathway_id):

        q_value = round(q_values[i], 4)
        results[pathway_id] = q_value

        # [Optional] Delete the pathway if does not pass the threshold
        if apply_threshold and q_value > threshold:
            del results[pathway_id][pathway_id]

    return results
