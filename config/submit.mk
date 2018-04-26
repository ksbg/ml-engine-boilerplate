TIMESTAMP := $(shell date +%d/%m/%Y-%H:%M:%S)

# General
PKG_NAME = trainer													# Name of the trainer package (in project root)		
PKG_PATH = ./$(PKG_NAME)											# Path to the package
JOB_NAME = $(PKG_NAME)_$(TIMESTAMP)									# Unique job name using timestamp
MODULE_NAME = $(PKG_NAME).train										# Module to be executed (must have __main__)

# GCloud instance options (for training)
SCALE_TIER = BASIC_GPU												# GCloud scale tier
RUNTIME_VERSION = 1.6												# Runtime (Tensorflow) version
REGION = us-east1													# GCloud region

# GCloud Storage options
BUCKET_NAME = my_bucket												# GCloud storage bucket name
JOB_DIR = gs://$(BUCKET_NAME)/jobs/$(JOB_NAME)						# Directory to store job data
# Custom command-line arguments
LOG_DIR = $(LOG_DIR_MAIN)/log_$(JOB_NAME)							# Directory to store logs
CHECKPOINT_DIR = gs://$(BUCKET_NAME)/checkpoints/ckp_$(JOB_NAME)	# Directory to store training checkpoints
MODEL_PROTO_DIR = gs://$(BUCKET_NAME)/model-proto/pb_$(JOB_NAME)	# Directory to store exported model protos
TRAIN_DATA_DIR = gs://$(BUCKET_NAME)/data/							# Directory where training data can be found

# Overwrites for local training (same as above, just local paths instead of gs)
%-local: JOB_DIR = ./out/jobs/$(JOB_NAME
%-local: LOG_DIR = ./out/logs/log_$(JOB_NAME)
%-local: CHECKPOINT_DIR = ./out/checkpoints/ckp_$(JOB_NAME)
%-local: MODEL_PROTO_DIR = ./out/proto-models/pb_$(JOB_NAME)
%-local: TRAIN_DATA_DIR = ./data/
