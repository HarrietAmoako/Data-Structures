#script for car deals
#list of carbrand available with their corresponding prices
carbrand={'honda':33700,
          'tesla':49800,
          'ferrari':244355,
          'ford mustang':27360,
          'audi':34800,
          'jeep':30300,
          'maserati':63499,
          'lamborghini':400000,
          'hyundai':30500,
          'mazda':23565,
          'jaguar':52500,
          'nissan':26290,
          'lexus':40100,
          'chevrolet':36200,
          'mercedes-benz':94350,
          'volkswagen':44010,
          'infiniti':40000,
          'pontiac':14700,
          'tata':10000,
          'yutong':55100,
          'ultima':15717,
          'lotus':94600,
          'toyota':33700,
          'land rover':80000,
          'opel':30000,
          'hummer':112696,
          'luxgen':9000,
          'rolls-royce':460000,
          'kia':40200,
          'mitsubishi':27955}
#find input for car name
carName=input("Enter a carName:")
#check if car name is in the list of carbrand available
if carName in carbrand:
    print("yes")
    #if car name is available,get its corresponding price
    carPrice=carbrand[carName]
    print(f"The price of {carName} is ${carPrice}.")
else:
    #if car name is absent,notify the user
    print(f"sorry,{carName} is unavailable.")
#link to github account
#https://github.com/HarrietAmoako

          
          
          