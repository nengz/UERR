This repository is used to release the source code, experimental data, and results of the work titled "UERR".

## I. Repository File Description

1. **code.rar**: This rar file contains the source code of UERR and baselines.

2. **data**: This directory stores all experimental data and results, including three compressed files:

   a) **repos.rar**: This rar file contains the raw data, preprocessing, and analysis results of 29,155 GitHub repositories.

   b) **models.rar**: This rar file includes offline built models, such as word2vec, IDF, and BM25 indices.

   c) **evaluation.rar**: This rar file contains 20 experimental queries and the experimental results for 4 RQs.

**Note**: "URRM" in the code and experimental data refers to "UERR".

## II. Project Configuration and Execution

1. Download the code and data from this repository and extract the rar files.

2. Install and configure Elasticsearch (ES) to support ES index building and retrieval required by the project.

3. Set the experimental data path according to the experimental directory structure in `conf/config.py`.

4. Set the `DEEPSEEK_API_KEY` in `repo/preprocess.py`.

5. Set the GitHub token in `baseline/github_searcher.py`.

6. Run `retrieval/pipeline.py`.
