import components as com
import matplotlib.pyplot as plt

svg_path_d = com.read_svg('./svg_files/Maple_Leaf.svg')

# WITHOUT MIRRORING THE POINTS
# discrete_points = com.create_discrete_points(svg_path_d, 150, mirror_wrt_x_axis=False)

discrete_points = com.create_discrete_points(svg_path_d, 150, mirror_wrt_y_axis=True)

# plt.plot(
# 	[p.real for p in discrete_points], 
# 	[p.imag for p in discrete_points]
# )
# plt.show()

cn = com.dft(discrete_points)
com.draw_with_coefficients(cn)