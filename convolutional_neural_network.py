from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense


class ConvolutionalNeuralNetwork:

    def __init__(self, input_shape, action_space):
        self.model = Sequential()
        self.model.add(Conv2D(8,
                              3,
                              strides=(1, 1),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape))
        self.model.add(Conv2D(16,
                              2,
                              strides=(2, 2),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape))
        '''
        self.model.add(Conv2D(64,
                              3,
                              strides=(1, 1),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape))
        '''
        self.model.add(Flatten())
        self.model.add(Dense(128, activation="relu"))
        self.model.add(Dense(action_space))
        self.model.compile(loss="mean_squared_error",
                           optimizer=RMSprop(lr=0.00025,
                                             rho=0.95,
                                             epsilon=0.01),
                           metrics=["accuracy"])
        self.model.summary()
