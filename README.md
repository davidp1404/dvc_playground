# DVC Playground

A self-contained sandbox for learning and experimenting with [DVC](https://dvc.org/) (Data Version Control) pipelines. It includes a full ML pipeline (prepare → featurize → train → evaluate) with local dummy remotes for both Git and DVC storage, so no external services are needed.

## Project Structure

```
├── src/                 # Pipeline stage scripts (Python + Bash)
├── data/raw/            # Raw input data
├── models/              # Trained model output
├── metrics/             # Evaluation metrics (JSON)
├── plots/               # Plot data (JSON)
├── dummy-s3/            # Local directory acting as DVC remote storage
├── dummy-git-remote/    # Local bare Git repo acting as Git remote
├── dvc.yaml             # DVC pipeline definition
├── params.yaml          # Hyperparameters and stage configuration
├── vars.yaml            # Variable substitutions (bucket URI, prefix)
├── reset.sh             # Reset everything to a clean initial state
└── create-pipeline.sh   # Recreate the DVC pipeline stages
```

## Prerequisites

- Git
- Python 3
- [DVC](https://dvc.org/doc/install) (`pip install dvc`)

## Usage

### Reset to a clean state

```bash
./reset.sh
```

This reinitializes Git and DVC, sets up local dummy remotes, and creates an initial commit. Run this to start fresh.

### Run the pipeline

```bash
dvc repro
```

Executes all pipeline stages defined in `dvc.yaml`: prepare, featurize, train, and evaluate.

### Modify parameters and experiment

Edit `params.yaml` to change hyperparameters, then rerun:

```bash
dvc repro
dvc metrics show
dvc plots show
```

### Run a DVC experiment

```bash
dvc exp run -S train.lr=0.01 -S train.epochs=50
dvc exp show
```

### Recreate the pipeline definition

```bash
./create-pipeline.sh
```

## Pipeline Stages

| Stage      | Description                          | Output           |
|------------|--------------------------------------|------------------|
| prepare    | Splits raw data into train/test sets | `data/split/`    |
| featurize  | Extracts features from split data    | `data/features/` |
| train      | Trains a model                       | `models/model.pkl` |
| evaluate   | Evaluates model, produces metrics    | `metrics/`, `plots/` |
