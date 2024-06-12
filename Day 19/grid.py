import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,3,5,7,9]
plt.plot(x,y1,linestyle='-',color='green',linewidth=3,marker='*',markersize=8,markerfacecolor='red',label='x-axis')
plt.plot(x,y2,linestyle='dotted',color='orange',linewidth=3,marker='4',markersize=8,markerfacecolor='blue',label='y-axis')
plt.title('customized line plot with grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.grid(color='grey',linestyle='--',linewidth=1)
plt.show()