from keras import models
from keras import layers
from keras.layers.normalization import BatchNormalization

block_1=models.Sequential()
model=models.Sequential()
block_1.add(layers.Conv2D(64,(7,7),strides=2,padding="same",activation="relu",input_shape=(112,112,3)))
block_1.add(layers.MaxPooling2D((3,3),strides=2))
block_1.add( BatchNormalization())
block_2_incp=models.Sequential()
block_2_incp.add(layers.Conv2D(64,(1,1),activation="relu"))
block_2_incp.add(layers.Conv2D(192,(3,3),activation="relu"))
block_2_incp.add(BatchNormalization())
block_2_incp.add(layers.MaxPooling2D((3,3),strides=2))
block_3a=models.Sequential()
tower_1_3a=Sequential()
tower_2_3a=Sequential()
tower_3_3a=Sequential()
tower_1_3a.add(layers.Conv2D(96,(1,1),activation="relu"))
tower_1_3a.add(layers.Conv2D(128,(3,3),activation="relu"))
tower_2_3a.add(layers.Conv2D(16,(1,1),activation="relu"))
tower_2_3a.add(layers.Conv2D(32,(5,5),activation="relu"))
tower_3_3a.add(layers.MaxPooling2D((3,3),strides=2))
tower_3_3a.add(layers.Conv2D(32,(1,1),activation="relu"))
block_3a=layers.merge([tower_1_3a,tower_2_3a,tower_3_3a,layers.Conv2D(64,(1,1),activation="relu")],mode='concat',concat_axis=1)
block_3b=models.Sequential()
tower_1_3b=Sequential()
tower_2_3b=Sequential()
tower_3_3b=Sequential()
tower_1_3b.add(layers.Conv2D(96,(1,1),activation="relu"))
tower_1_3b.add(layers.Conv2D(128,(3,3),activation="relu"))
tower_2_3b.add(layers.Conv2D(32,(1,1),activation="relu"))
tower_2_3b.add(layers.Conv2D(64,(5,5),activation="relu"))
tower_3_3b.add(layers.MaxPooling2D((3,3),strides=2))
tower_3_3b.add(layers.Conv2D(64,(1,1),activation="relu"))
block_3b=layers.merge([tower_1_3a,tower_2_3a,tower_3_3a,layers.Conv2D(64,(1,1),activation="relu")],mode='concat',concat_axis=1)
