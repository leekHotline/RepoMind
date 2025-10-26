import tensorflow as tf

scalar = tf.constant(5)  # 标量 向量 矩阵 张量
vector = tf.constant([1, 2])

matrix = tf.constant([[1, 2], [3, 4]])

tensor = tf.constant([[[1, 2], [3, 4]]])

print("标量:", scalar.numpy())

print("形状:", scalar.shape)

print("数据类型:", scalar.dtype)

