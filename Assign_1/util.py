def recur(lst, index, width, height):
    if isinstance(lst,float):
        if index == 0: #width  
            return int(lst* width) 
        elif index == 1: #height
            return int(lst* height)    
    else:
        return [recur(i, lst.index(i), width, height) for i in lst]



def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)


dct = {'Bumper': (50,100,255),
 'Light' : (50,200,155),
 'Bonnet' : (100,50,255),
 'Windshield' : (200,50,155),
 'Boot' : (250, 50, 155),
 'Broken' : (200, 100, 255),

 'Mirror' : (50,255,100),
 'Wheel' : (50,155,200),
 'Door' : (100,255,50),
 'RockerPanel' : (200,155,50),
 'Dent&Scratch(zoom)': (200,255,50),
 'Radiator' : (100, 155, 200),
 
 'WindowPanel' : (255,50,100),
 'Fender' : (155,50,200),
 'Roof' : (255,100,50),
 'BackaboveFender' : (155,200,50),
 'Dent&Scratch' : (255,100,50)}


isClosed = True
thickness = 1
alpha = 0.2  # Transparency factor.
gap=5
