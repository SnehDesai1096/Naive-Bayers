# Author : SNEH DESAI
# Description : THIS IS THE CODE FOR NAIVE BAYES THEOREM
#               AND IT HAD ALSO BEEN TESTED FOR ALL THE POSSIBLE RESULTS.

# DATA MINING


# Open File to read
myFile = open('Play Or Not.csv', 'r')

# Logic

ListOfLines = myFile.read().splitlines()                  # Reads The Lines
print(ListOfLines[0])

# All The Counter Variable.
count = 0
sunny = 0
overcast = 0
rainy = 0
hot = 0
mild = 0
cool = 0
high = 0
normal = 0
t = 0
f = 0
yes = 0
no = 0

# The Yes Along with Individual Counter Variable
y_sunny = 0
y_overcast = 0
y_rainy = 0
y_hot = 0
y_mild = 0
y_cool = 0
y_high = 0
y_normal = 0
y_t = 0
y_f = 0

# The No Along with Individual Counter Variables

n_sunny = 0
n_overcast = 0
n_rainy = 0
n_hot = 0
n_mild = 0
n_cool = 0
n_high = 0
n_normal = 0
n_t = 0
n_f = 0

# The Real Program starts from Here

for i in range(1,len(ListOfLines),1):                   # Loop for all the column in a row.
    aLine = ListOfLines[i]
    lineItem = aLine.split(',')
    Outlook = lineItem[0]
    Temp = lineItem[1]
    Humidity = lineItem[2]
    Windy = lineItem[3]
    Play = lineItem[4]
    count += 1
    print(Outlook,' | ', Temp, ' | ', Humidity, ' | ', Windy, " | ", Play)
    print("Count = ",count)
# Casual Checking
    if Outlook == 'sunny' :
        sunny += 1
    if Outlook == 'overcast':
        overcast += 1
    if Outlook == 'rainy':
        rainy += 1
    if Temp == 'mild':
        mild += 1
    if Temp == 'cool':
        cool += 1
    if Temp == 'hot':
        hot += 1
    if Humidity == 'high':
        high += 1
    if Humidity == 'normal':
        normal += 1
    if Windy == 'TRUE':
        t += 1
    if Windy == 'FALSE':
        f += 1
    if Play == 'yes':
        yes += 1
    if Play == 'no':
        no += 1
# End Casual Checking

# Checking Individual with 'Yes' and 'No'

    if Outlook == 'sunny' and Play == 'yes':
        y_sunny += 1
    if Outlook == 'overcast' and Play == 'yes':
        y_overcast += 1
    if Outlook == 'rainy' and Play == 'yes' :
        y_rainy += 1
    if Temp == 'mild' and Play == 'yes':
        y_mild += 1
    if Temp == 'cool' and Play == 'yes':
        y_cool += 1
    if Temp == 'hot' and Play == 'yes':
        y_hot += 1
    if Humidity == 'high' and Play == 'yes':
        y_high += 1
    if Humidity == 'normal' and Play == 'yes':
        y_normal += 1
    if Windy == 'TRUE' and Play == 'yes':
        y_t += 1
    if Windy == 'FALSE' and Play == 'yes':
        y_f += 1

# Checking Individual with 'Yes' and 'No'

    if Outlook == 'sunny' and Play == 'no':
        n_sunny += 1
    if Outlook == 'overcast' and Play == 'no':
        n_overcast += 1
    if Outlook == 'rainy' and Play == 'no' :
        n_rainy += 1
    if Temp == 'mild' and Play == 'no':
        n_mild += 1
    if Temp == 'cool' and Play == 'no':
        n_cool += 1
    if Temp == 'hot' and Play == 'no':
        n_hot += 1
    if Humidity == 'high' and Play == 'no':
        n_high += 1
    if Humidity == 'normal' and Play == 'no':
        n_normal += 1
    if Windy == 'TRUE' and Play == 'no':
        n_t += 1
    if Windy == 'FALSE' and Play == 'no':
        n_f += 1




# The PRINT of Count of Individual TYPE

print('No. of Sunny = ', sunny)
print('No. of Overcast = ', overcast)
print('No. of Rainy = ', rainy)
print('No. of Cool = ', cool)
print('No. of Mild = ', mild)
print('No. of Hot = ', hot)
print('No. of High  = ', high)
print('No. of Normal = ', normal)
print('No. of True = ', t)
print('No. of False = ', f)
print('No. of Yes = ', yes)
print('No. of No = ', no)
print('\n\n')

# The Print of Count of Yes and Individual Type

print('No. of Yes and Sunny = ', y_sunny)
print('No. of Yes and Overcast = ', y_overcast)
print('No. of Yes and Rainy = ', y_rainy)
print('No. of Yes and Cool = ', y_cool)
print('No. of Yes and Mild = ', y_mild)
print('No. of Yes and Hot = ', y_hot)
print('No. of Yes and High  = ', y_high)
print('No. of Yes and Normal = ', y_normal)
print('No. of Yes and True = ', y_t)
print('No. of Yes and False = ', y_f)
print('\n\n')

# The Print of Count of No and Individual Types

print('No. of No and Sunny = ', n_sunny)
print('No. of No and Overcast = ', n_overcast)
print('No. of No and Rainy = ', n_rainy)
print('No. of No and Cool = ', n_cool)
print('No. of No and Mild = ', n_mild)
print('No. of No and Hot = ', n_hot)
print('No. of No and High  = ', n_high)
print('No. of No and Normal = ', n_normal)
print('No. of No and True = ', n_t)
print('No. of NO and False = ', n_f)

# Selection Process to find out the result.
print("\n\nFind Out Weather the Whether is Good enough to play or not??")

# Selection of OUTLOOK

out_yes = 1
out_no = 1

print("\n\n   Select the OutLook. \n1. Sunny\n2. Overcast\n3. Rainy")
print('\n  Enter The Selection : ')
inp = input()

if inp == "1":
    sel = 1
    out_yes = (y_sunny / yes)
    out_no = (n_sunny / no)

elif inp == "2":
    sel = 2
    out_yes = y_overcast / yes
    out_no = n_overcast / no

elif inp == "3":
    sel = 3
    out_yes = y_rainy / yes
    out_no = n_rainy / no

else:
    print("Wrong Choice entered")



# SELECTION OF TEMPERATURE

out1_no = 0
out1_yes = 0

print('\n   Select the Type of Temperature.\n1. Hot\n2. Mild\n3. Cool')
print('\n  Enter The Selection : ')
inp1=input()
if inp1 == '1':
    sel1 = 1
    out1_yes = y_hot / yes
    out1_no = n_hot / no
elif inp1 == '2':
    sel1 = 2
    out1_yes = y_mild / yes
    out1_no = n_mild / no
elif inp1 == '3':
    sel1 = 3
    out1_yes = y_cool / yes
    out1_no = n_cool / no
else:
    print("Wrong Choice entered")

# SELECTION OF HUMIDITY

out2_no = 0
out2_yes = 0

print('\n   Select the Humidity Level.\n1. High\n2. Normal')
print('\n  Enter The Selection : ')
inp2=input()
if inp2 == '1':
    sel2 = 1
    out2_yes = y_high / yes
    out2_no = n_high / no
elif inp2 == '2':
    sel2 = 2
    out2_yes = y_normal / yes
    out2_no = n_normal / no
else:
    print("Wrong Choice entered")

# SELECTION OF WIND PRESENCE

out3_no = 0
out3_yes = 0

print('\n   Select the Wind Presence. \n1. Yes\n2. No')
print('\n  Enter The Selection : ')
inp3=input()
if inp3 == '1':
    sel3 = 1
    out3_yes = y_t / yes
    out3_no = n_t / no
elif inp3 == '2':
    sel3 = 2
    out3_yes = y_f / yes
    out3_no = n_f / no
else:
    print("Wrong Choice entered")

# Implementing Naive Bayesian

p = yes / count
q = no / count

output_yes = out_yes * out1_yes * out2_yes * out3_yes * p
output_no =  out_no * out1_no * out2_no * out3_no * q

probability_y = output_yes / (output_yes + output_no)
probability_n = output_no / (output_yes + output_no)

if probability_y > probability_n :
    print("Yes You Can Play")
elif probability_n > probability_y:
    print("No You Cant Play")


