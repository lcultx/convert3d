import sys

class z3DS(object):
    def __init__(self,filename):
        print "3ds"
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class DAE(object):
    def __init__(self,filename):
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class OBJ(object):
    def __init__(self,filename):
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class STL(object):
    def __init__(self,filename):
        print "stl"
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class THREE(object):
    def __init__(self,filename):
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class AWD(object):
    def __init__(self,filename):
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class SWM(object):
    def __init__(self,filename):
        pass

    def SetFilename(self, filename):
        pass

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

def main():
    print "start...."
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_file_type = input_file.split(".")[1]
    output_file_type = output_file.split(".")[1]

    switch={
        "3ds":z3DS,
        "dae": DAE,
        "obj":OBJ,
        "stl": STL,
        "json":THREE,
        "awd":AWD,
        "swm":SWM
    }

    input_model = switch[input_file_type](input_file)
    output_model = switch[output_file_type](output_file)

    shape = input_model.GetShape()
    output_model.SetShape(shape)
    output_model.WriteFile()

    print "done!..."

if __name__ == '__main__':
	main()