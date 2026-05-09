#!/bin/bash
set -e
cd "$(dirname "$0")"

# Reset git to empty state (no commits)
rm -rf .git
git init
git branch -m develop
git remote add origin ./dummy-git-remote
git config user.email "dev@example.com"
git config user.name "Dev User"

# Reset dummy git remote (bare repo, no commits)
rm -rf dummy-git-remote
git init --bare dummy-git-remote

# Clear dummy S3 storage
rm -rf dummy-s3
mkdir -p dummy-s3

# Remove DVC pipeline outputs and cache
rm -rf data/split data/features models metrics plots
mkdir -p models metrics plots
rm -f dvc.lock

# Reset DVC directory (recreate config from scratch)
rm -rf .dvc
dvc init
dvc remote add -d dvc-store $(pwd)/dummy-s3
dvc remote modify dvc-store verify true
dvc config core.autostage true
dvc config cache.type copy
dvc config exp.auto_push true
dvc config exp.git_remote origin
dvc install

# Stage and commit initial state
#dvc repro --force
git add .
git commit --allow-empty -m "Initial commit"
git push origin develop
git config push.default current
