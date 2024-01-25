# LfN_2044012
My personal contributions to the final group project of LfN

# below are the instructions on how to get the same results as reported in the document

# there are two executables in the folder /src, namely 'Deg_Center.py' and a python notebook namely 'integration_of_networkx_features.ipynb'.

# the output of the Deg_Center.py are the node-level features, computed on the DHFR dataset. The output comprises of appending content to three already-created .txt files in the /texts folder. These features are later used by the python notebook, in order to compute the graph-level features for classification.

# The dataset must be downloaded from 'https://www.chrsmrrs.com/graphkerneldatasets/DHFR.zip', unzipped in a folder called "DHFR" in the  directory /src where the executables are located in.

# the .py file can be executed in any standard IDE which supports the python language. For this project, the code was implemented using Visual Studio Code.

# the python notebook was implemented completely in the Google Colab Service, using the standard python 3 CPU runtime.

# the notebook as input, takes the 5 text files in the /texts directory. 

# the two text files of 'graphlet_counts_len_3.txt' and 'graphlet_counts_len_4.txt' are among the contributions of KARIMI ARMIN (a member of the group) and thus they are already provided in the /texts directory.

# the notebook also saves 7 .pt files which are tensors, in the /tensors directory, these files are later loaded by the same notebook.

# this save/load mechanism was implemented to facilitate running the notebook several times.

