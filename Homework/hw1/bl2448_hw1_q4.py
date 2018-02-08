years=int(input("Input number of years: "))
seconds=years*365*24*60*60
population=307357870
population=population+int((1/7)*seconds)+int((1/35)*seconds)-int((1/13)*seconds)
print("Estimated population:", population)
