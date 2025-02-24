def tanh_function(value):
    exp_val = 2.71828 ** (2 * value)
    return (exp_val - 1) / (exp_val + 1)   
input1, input2 = 0.07, 0.15  
weight1, weight2, weight3, weight4 = 0.18, -0.22, 0.29, -0.12
weight5, weight6, weight7, weight8 = -0.27, 0.38, -0.15, 0.26
bias1, bias2 = 0.45, 0.65  
hidden_net1 = (weight1 * input1) + (weight2 * input2) + bias1
hidden_net2 = (weight3 * input1) + (weight4 * input2) + bias1
hidden_out1 = tanh_function(hidden_net1)
hidden_out2 = tanh_function(hidden_net2)
output_net1 = (weight5 * hidden_out1) + (weight6 * hidden_out2) + bias2
output_net2 = (weight7 * hidden_out1) + (weight8 * hidden_out2) + bias2
output1 = tanh_function(output_net1)
output2 = tanh_function(output_net2)
print("Final Output 1:", output1)
print("Final Output 2:", output2)