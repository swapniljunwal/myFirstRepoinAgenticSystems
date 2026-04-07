import numpy as np
import matplotlib.pyplot as plt

epochs = list(range(1, 11))
print(epochs)

loss = np.linspace(1.0, 0.2, 10)
print(loss)

plt.figure(figsize=(8, 5))
plt.plot(epochs, marker = "s") 
plt.plot(loss, marker = "o")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.title("bar graph")
plt.grid()

plt.figure(figsize=(8, 5))
plt.scatter(epochs,loss)
plt.xlabel("epochs")
plt.ylabel("loss")
plt.title("scatter graph")
plt.show()

models = ["modelA" , "modelB" , "modelC"]
accuracy = [0.85, 0.90, 0.88]
plt.bar(models , accuracy)
plt.figure(figsize=(8, 5))
plt.xlabel("models")
plt.ylabel("accuracy")
plt.title("bar graph")

plt.show()