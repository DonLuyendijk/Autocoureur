from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt
import pickle

lines = np.loadtxt('default.samples')

inputs = lines[:, :-1]
outputs = lines[:, -1]

neural_net = MLPRegressor(
    max_iter = 40000,
    hidden_layer_sizes = (120),
    alpha = 1
).fit(inputs, outputs)

print('score:', neural_net.score(inputs, outputs))

with open('neural_net', 'wb') as handle:
        pickle.dump(neural_net, handle)

plt.plot(neural_net.loss_curve_)
plt.show()
