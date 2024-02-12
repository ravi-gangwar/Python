# from matplotlib import pyplot as plt
  
#  #Plotting to our canvas
  
# plt.plot([1,2,3],[4,5,1])
  
#  #Showing what we plotted
  
# plt.show()

from matplotlib import pyplot as plt
 
plt.bar([0,2,4,6,8],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([1,3,5,7,9],[80,20,20,50,60],
label="Audi",width=.5)
# plt.bar([1.25,2.25,3.25,4.25,5.25],[20,20,30,50,10],
# label="Mercedes",width=.5)
# plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()