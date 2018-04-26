import logging
import os
from argparse import ArgumentParser

import tensorflow as tf

from .summary_logger import Logger

LOGGER_NAME = 'ModelTrain'
LOGGER_LEVEL = logging.DEBUG


def init_training(is_local, train_data_dir, log_dir, job_dir, checkpoint_dir, proto_dir):
    # Create directories if they don't exist
    if is_local:
        for directory in [log_dir, job_dir, checkpoint_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)

    # Init tensorboard summary logger
    tb_logger = Logger(log_dir)

    # Init stack logger
    logging.basicConfig(level=LOGGER_LEVEL)
    stack_logger = logging.getLogger(LOGGER_NAME)

    # Train
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        stack_logger.info('Starting...')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--is-local',
        type=int,
        help='GCS or local paths to csv file containing sparse training data',
        required=True
    )
    parser.add_argument(
        '--train-data-dir',
        help='GCS or local paths containing training data',
        required=True
    )
    parser.add_argument(
        '--log-dir',
        help='Location where the training log files should be stored (for tensorboard)',
        required=True
    )
    parser.add_argument(
        '--job-dir',
        help='GCS location to write job information',
        required=True
    )
    parser.add_argument(
        '--checkpoint-dir',
        help='GCS location to write checkpoints',
        required=True
    )
    parser.add_argument(
        '--proto-dir',
        help='GCS location to the json file containing training parameters',
        required=True
    )
    args = parser.parse_args()

    init_training(**args.__dict__)
