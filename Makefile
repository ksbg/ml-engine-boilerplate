include ./config/submit.mk

define SUBMIT_LOCAL
gcloud ml-engine local train \
	--module-name $(MODULE_NAME) \
	--package-path $(PKG_PATH) \
	--job-dir $(JOB_DIR) \
	-- \
	--is_local 1 \
endef

define SUBMIT_GCLOUD
gcloud ml-engine jobs submit training $(JOB_NAME) \
	--job-dir $(JOB_DIR) \
	--module-name $(MODULE_NAME) \
	--package-path $(PKG_PATH) \
	--region $(REGION) \
	--config ./config/python.yaml \
	--scale-tier $(SCALE_TIER) \
	--runtime-version $(RUNTIME_VERSION) \
	--region $(REGION) \
	-- \
	--is_local 0 \
endef

define CMD_ARGS
	--train-data-dir ${TRAIN_DATA_DIR} \
	--log-dir ${LOG_DIR} \
	--checkpoint-dir ${CHECKPOINT_DIR} \
	--proto-dir ${MODEL_PROTO_DIR}
endef

train-local:
	$(SUBMIT_LOCAL) \
	$(CMD_ARGS)

train-gcloud:
	$(SUBMIT_GCLOUD) \
	$(CMD_ARGS)