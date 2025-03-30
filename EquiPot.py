import numpy as np
import matplotlib.pyplot as plt 

valores = np.loadtxt('/home/juancarlos/GIT/repositorio1GH/repositorio1-ejemplo/datos.txt')

x = np.linspace(1, 7, 7)  # Eje x
y = np.linspace(5, 1, 5)  # Eje y
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, valores, cmap='plasma')  
plt.colorbar(label='Voltaje')

for i in range(len(y)):
    for j in range(len(x)):
        plt.text(X[i, j], Y[i, j], f'{valores[i, j]:.2f}', ha='center', va='center', color='black')

plt.title('Voltaje en solucion NaCl deepth=5mm to 5V')
plt.xlabel('Dirección Horizontal')
plt.ylabel('Dirección Vertical')
plt.grid()
plt.savefig('LineasEquipotenciales.png')
plt.show()
