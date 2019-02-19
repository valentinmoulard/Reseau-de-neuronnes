from fann2 import libfann
from langdetect import detect

connection_rate = 1
learning_rate = 0.2

num_input = 2
num_hidden = 2
num_output = 1

desired_error = 0.0000001
max_iterations = 100000
iterations_between_reports = 1

ann = libfann.neural_net()
ann.create_sparse_array(connection_rate, (num_input, num_hidden, num_output))
ann.set_learning_rate(learning_rate)
ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)

ann.train_on_file("xor.data", max_iterations, iterations_between_reports, desired_error)

ann.save("xor.net")

ann = libfann.neural_net()
ann.create_from_file("xor.net")

toto=ann.run([1, 1])


print (toto)




print(detect("Language detection algorithm is non-deterministic, which means that if you try to run it on a text which is either too short or too ambiguous, you might get different results everytime you run it."))
