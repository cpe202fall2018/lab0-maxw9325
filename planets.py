def weight_on_planets():
   # write your code here
   weight = float(input("What do you weigh on earth? "))
   Mars = 0.38
   Jupiter = 2.34
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(Mars*weight,Jupiter*weight))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
