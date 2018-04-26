"""Logs model metrics for tensorboard"""
import tensorflow as tf

LOG_LOGLOSS_TAG = 'logloss'
LOG_TRAIN_AUC_TAG = 'train_auc'
LOG_TEST_AUC_TAG = 'test_auc'
LOG_FINISHED_ITERATIONS_TAG = 'finished_iterations'


class Logger:
    def __init__(self, log_dir):
        tf.summary.scalar(LOG_LOGLOSS_TAG, 0)
        tf.summary.scalar(LOG_TRAIN_AUC_TAG, 0)
        tf.summary.scalar(LOG_TEST_AUC_TAG, 0)
        tf.summary.scalar(LOG_FINISHED_ITERATIONS_TAG, 0)

        self.summary_writer = tf.summary.FileWriter(log_dir, graph=tf.get_default_graph())

    def write_log(self, log_loss, train_score, test_score, no_iterations):
        summary = tf.Summary(value=[tf.Summary.Value(tag=LOG_LOGLOSS_TAG, simple_value=log_loss),
                                    tf.Summary.Value(tag=LOG_TRAIN_AUC_TAG, simple_value=train_score),
                                    tf.Summary.Value(tag=LOG_TEST_AUC_TAG, simple_value=test_score),
                                    tf.Summary.Value(tag=LOG_FINISHED_ITERATIONS_TAG, simple_value=no_iterations)])

        self.summary_writer.add_summary(summary)
