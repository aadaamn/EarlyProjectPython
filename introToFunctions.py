# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Temperature converter from F to C
def f_to_c(f_temp):
  c_temp = round(((f_temp - 32) * 5/9), 2)
  return c_temp
# if 100f
f100_in_celcius = f_to_c(100)


# Temperature converter from C to F
def c_to_f(c_temp):
  f_temp = round((c_temp * (9/5) + 32) , 2)
  return f_temp
# if 0C
c0_in_fahrenheit = c_to_f(0)


# Get force
def get_force(mass, acceleration):
  product = mass * acceleration
  return product
# Train force
train_force = get_force(train_mass , train_acceleration)
print("The GE train supplies", train_force , "Newtons of force.")



# Get energy
def get_energy(mass, c = 3*10**8):
  product = mass * c
  return product
# Bomb mass
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies" , bomb_energy , "Joules")



# Get Work
def get_work(mass , acceleration , distance):
  force = get_force(mass , acceleration)
  product = force * distance
  return product
# Try
train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does", train_work ,  "Joules of work over" ,  train_distance ,  "meters.")