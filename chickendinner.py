## Chicken Dinner

def evalNeuralNetwork(inputArr, weightArr):
    result = 0

    for i  in range(len(inputArr)):
        prod = inputArr [i] * weightArr [i]
        result += prod
    return result

def learn(weightArr, inputArr, learningRate):
    for i in range (len(inputArr)):
        if (inputArr[i] == 1):
            weightArr [i] += learningRate

def training(learningRate, weightArr, inputArr, trials):
    for i in range (trials):
            result = evalNeuralNetwork(inputArr, weightArr)
            learn(weightArr, inputArr, learningRate)
            print("result: ", result)
            weightArr[2] = round(weightArr[2], 3)
            print(weightArr)

if __name__ == "__main__":
    inputArr = [0, 0, 1, 0]
    weightArr = [0, 0, 0, 0]
    learningRate = 0.10
    trials = 10
    training(learningRate, weightArr, inputArr, trials)
