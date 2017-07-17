import pickle
import logging
import os

from baskets import rnnmodel
from baskets import utils
from baskets import common

def feed_dict_for_batch(batch, model):
  """where batch is a thing returned by a Batcher"""
  x, y, seqlens, lossmask, pids, aids, dids, uids = batch
  feed = {
      model.input_data: x,
      model.labels: y,
      model.sequence_lengths: seqlens,
      model.lossmask: lossmask,
  }
  if model.hps.product_embedding_size:
    feed[model.product_ids] = pids
  if model.hps.aisle_embedding_size:
    feed[model.aisle_ids] = aids
  if model.hps.dept_embedding_size:
    feed[model.dept_ids] = dids
  return feed

