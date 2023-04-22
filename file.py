#Linking
import matplotlib.pyplot as plt

#Plot
data = [[0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,0,1,1,0,1,0],
        [0,1,0,1,1,0,1,0],
        [0,1,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]]

#ToShow
plt.imshow(data, cmap='gray')
plt.show()