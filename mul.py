# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

const1 = tf.constant(3)
const2 = tf.constant(4)
add_op = tf.add(const1, const2)
mul_op = tf.mul(add_op, const2)

with tf.Session() as sess:
  result1, result2 = sess.run([add_op, mul_op])
  print(result1)
  print(result2)

  tf.train.SummaryWriter('./', sess.graph)
