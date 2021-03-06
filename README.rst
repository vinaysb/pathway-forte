PathwayForte |build| |docs| |coverage| |zenodo|
===============================================
A Python package for benchmarking pathway databases with functional enrichment and prediction methods
tasks.

If you find ``pathway_forte`` useful for your work, please consider citing:

.. [1] Mubeen, S., *et al* (2019). `The Impact of Pathway Database Choice on
       Statistical Enrichment Analysis and Predictive Modeling
       <https://doi.org/10.3389/fgene.2019.01203>`_. *Front. Genet.*, 10:1203.


Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``pathway_forte`` can be installed from `PyPI <https://pypi.org/project/pathway-forte>`_
with the following command in your terminal:

.. code-block:: sh

    $ python3 -m pip install pathway_forte

The latest code can be installed from `GitHub <https://github.com/pathwayforte/pathway-forte>`_
with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/pathwayforte/pathway-forte.git

For developers, the code can be installed with:

.. code-block:: sh

    $ git clone https://github.com/pathwayforte/pathway-forte.git
    $ cd pathway-forte
    $ python3 -m pip install -e .

Main Commands
-------------
The table below lists the main commands of PathwayForte.

+------------+--------------------------------+
| Command    | Action                         |
+============+================================+
| datasets   | Lists of Cancer Datasets       |
+------------+--------------------------------+
| export     | Export Gene Sets using ComPath |
+------------+--------------------------------+
| ora        | List of ORA Analyses           |
+------------+--------------------------------+
| fcs        | List of FCS Analyses           |
+------------+--------------------------------+
| prediction | List of Prediction Methods     |
+------------+--------------------------------+

Functional Enrichment Methods
-----------------------------
- **ora**. Lists Over-Representation Analyses (e.g., one-tailed hyper-geometric test).
- **fcs**. Lists Functional Class Score Analyses such as GSEA and ssGSEA using
  `GSEAPy <https://github.com/ostrokach/gseapy>`_.

Prediction Methods
------------------
``pathway_forte`` enables three classification methods (i.e., binary classification, training SVMs for
multi-classification tasks, or survival analysis) using individualized pathway activity scores. The scores can be
calculated from any pathway with a variety of tools (see [2]_) using any pathway database that enables to export its
gene sets.

- **binary**. Trains an elastic net model for a binary classification task (e.g., tumor vs. normal patients). The
  training is conducted using a nested cross validation approach (the number of cross validation in both loops can be
  selected). The model used can be easily changed since most of the models in
  `scikit-learn <https://scikit-learn.org/>`_ (the machine learning library used by this package) required the same
  input.
- **subtype**. Trains a SVM model for a multi-class classification task (e.g., predict tumor subtypes). The training is
  conducted using a nested cross validation approach (the number of cross validation in both loops can be selected).
  Similarly as the previous classification task, other models can quickly be implemented.
- **survival**. Trains a Cox's proportional hazard's model with elastic net penalty. The training is conducted using a
  nested cross validation approach with a grid search in the inner loop. This analysis requires pathway activity
  scores, patient classes and lifetime patient information.

Other
-----
- **export**. Export GMT files with current gene sets for the pathway databases included in ComPath [3]_.
- **datasets**. Lists the TCGA data sets [4]_ that are ready to run in ``pathway_forte``.

References
----------
.. [2] Lim, S., *et al.* (2018). `Comprehensive and critical evaluation of individualized pathway activity measurement
       tools on pan-cancer data <https://doi.org/10.1093/bib/bby097>`_. *Briefings in bioinformatics*, bby125.
.. [3] Domingo-Fernández, D., *et al.* (2018). `ComPath: An ecosystem for exploring, analyzing, and curating mappings
       across pathway databases <https://doi.org/10.1038/s41540-018-0078-8>`_. *npj Syst Biol Appl.*, 4(1):43.
.. [4] Weinstein, J. N., *et al.* (2013). `The cancer genome atlas pan-cancer analysis project
       <https://doi.org/10.1038/ng.2764>`_. *Nature genetics*, 45(10), 1113.

License
-------
The Pathway Forte logo is derived from `"Muscle Fat" <https://game-icons.net/1x1/lorc/muscle-fat.html>`_ by Lorc, used under CC BY 3.0.

Disclaimer
-----------
PathForte is a scientific software that has been developed in an academic capacity, and thus comes with no warranty or
guarantee of maintenance, support, or back-up of data.

.. |build| image:: https://travis-ci.com/pathwayforte/pathway-forte.svg?branch=master
    :target: https://travis-ci.com/pathwayforte/pathway-forte
    :alt: Build Status

.. |docs| image:: http://readthedocs.org/projects/pathwayforte/badge/?version=latest
    :target: https://pathwayforte.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |coverage| image:: https://codecov.io/gh/pathwayforte/pathway-forte/coverage.svg?branch=master
    :target: https://codecov.io/gh/pathwayforte/pathway-forte?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pathway_forte.svg
    :target: https://pypi.org/project/pathway-forte
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pathway_forte.svg
    :target: https://pypi.org/project/pathway-forte
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pathway_forte.svg
    :target: https://github.com/pathwayforte/pathway-forte/blob/master/LICENSE
    :alt: Apache-2.0

.. |zenodo| image:: https://zenodo.org/badge/178654585.svg
    :target: https://zenodo.org/badge/latestdoi/178654585
