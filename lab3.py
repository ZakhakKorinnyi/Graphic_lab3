import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Зчитуємо дані
points_list = []
with open('DS4.txt', 'r') as file:
    for line in file:
        coords = line.split()
        if len(coords) == 2:
            points_list.append([int(coords[0]), int(coords[1])])

# список у масив
points = np.array(points_list)

# Знаходимо опуклу оболонку
hull = ConvexHull(points)

# Зберігаємо координати вершин опуклої оболонки
with open('convex_hull_DS4.txt', 'w') as f_out:
    for vertex in hull.vertices:
        f_out.write(f"{points[vertex, 0]} {points[vertex, 1]}\n")

# розмір полотна 960x540
plt.figure(figsize=(9.6, 5.4), dpi=100)

# Відображає всі точки вихідного датасету
plt.scatter(points[:,0], points[:,1], color='black', s=5)

# Відображає опуклу оболонку відрізками синього кольору
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'b-')

plt.xlim(0, 960)
plt.ylim(0, 540)
plt.savefig('result_lab3.png')
plt.close()

print("Опуклу оболонку знайдено. Файли convex_hull_DS4.txt та result_lab3.png успішно збережено.")