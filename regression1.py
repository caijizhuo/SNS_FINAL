import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense,Activation
import matplotlib.pyplot as plt # 可视化模块
import math

# create some data
X = np.linspace(-1, 1, 200) #从-1到1等分成200份
print(X)
np.random.shuffle(X)    # randomize the data 洗牌函数 改变数组位置
Y = 2*X*X*X + 2 + np.random.normal(0, 0.05, (200, ))  #模拟噪声
# plot data
# plt.scatter(X, Y)
# plt.show()

X_train, Y_train = X[:160], Y[:160]     # train 前 160 data points
X_test, Y_test = X[160:], Y[160:]       # test 后 40 data points



model = Sequential()
# model.add(Dense(100,input_shape=(1,)))
# model.add(Activation('sigmoid'))
model.add(Dense(output_dim = 34,input_dim=1,activation='relu'))
model.add(Dense(output_dim = 34,activation = 'relu'))
model.add(Dense(output_dim = 100,activation = 'relu'))
# model.add(Dense(output_dim = 100,activation = 'relu'))
# model.add(Dense(output_dim = 100,activation = 'relu'))
# model.add(Dense(output_dim = 100,activation = 'relu'))
# model.add(Dense(output_dim = 100,activation = 'relu'))
# model.add(Dense(output_dim = 100,activation = 'relu'))

model.add(Dense(output_dim = 1,activation = 'relu'))
# model.add(Dense(30,activation='relu',input_shape=(1,)))

# choose loss function and optimizing method
model.compile(loss='mse', optimizer='adam')

# training
plt.scatter(X_test, Y_test)
print('Training -----------')
for step in range(1501):  #这个301是训练次数
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print('train cost: ', cost)
        
        X_test.sort()
        Y_pred = model.predict(X_test)
        ln, = plt.plot(X_test, Y_pred,'r')
        plt.ion()
        plt.show()
        plt.pause(0.1)
        if step!= 1500:
        	ln.remove()

plt.pause(0)


# test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)
print(model.layers[-1])
W, b = model.layers[-1].get_weights()
print('Weights=', W, '\nbiases=', b)


# plotting the prediction


plt.scatter(X_test, Y_test)
X_test.sort()
Y_pred = model.predict(X_test)
plt.plot(X_test, Y_pred,'r')
plt.ion()
plt.show()
