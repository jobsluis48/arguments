# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(*inputs):
    if len(inputs) == 1:
        string = f'\'Hello, {inputs[0]}!\''
    elif len(inputs) == 2:
        greeting = inputs[1].split(',')[0]
        string = f'\"{greeting}, {inputs[0]}!\"'
    return string

#print(greet('Bob', "What's up, <name>!"))

def force (mass, body): 
    grav = {'sun': 274,'jupiter': 24.9,'neptune': 11.2,'saturn': 10.4,'earth': 9.8,'uranus': 8.9,'venus':8.9,'mars':3.7,'mercury':3.7,'moon':1.6,'pluto':0.6}
    if body in grav:
        return mass * grav[body]

#print(force(2,'sun'))

def pull (m1, m2, d):
    G = 6.674 * (10 ** -11)
    return (G * m1 * m2)/(d ** 2)

#print (pull(800,1500,3))
