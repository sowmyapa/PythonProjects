# Assign the variable total on line 8!

meal = float(raw_input("Get Meal Cost\n"));
tax = float(raw_input("Get Tax perecent\n"))/100;
tip = 0.15

meal = meal + meal * tax
total=meal+meal*tip

print("%.2f" % total)