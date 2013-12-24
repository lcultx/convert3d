import sys
import os
from Dice3DS import dom3ds

class Model(object):
    def __init__(self,filename):
        self.SetFilename(filename)
        self._shape = None

    def SetFilename(self, filename):
        print filename
        if not os.path.isfile(filename):
            print "Error: file %s not found."%filename
            self._filename = None
        else:
            self._filename = filename

    def ReadFile(self):
        pass

    def WriteFile(self):
        pass

    def GetShape(self):
        pass

    def SetShape(self, aShape):
        pass

class Shape(object):
    pass

class z3DS(Model):
    def ReadFile(self):
        dom = dom3ds.read_3ds_file(self._filename,tight=False)
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class DAE(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class OBJ(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class STL(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class THREE(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class AWD(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

class SWM(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass
    def GetShape(self):
        pass
    def SetShape(self, aShape):
        pass

def main():
    input_file = output_file = ""
    input_file_type = output_file_type = ""
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        input_file_type = input_file.split(".")[1]
        output_file_type = output_file.split(".")[1]
    except:
        print 'error: convert3d use example \n convert3d aaa.3ds bbb.swm'
        # here, we are not exiting the program

    switch={
        "3ds":z3DS,
        "dae": DAE,
        "obj":OBJ,
        "stl": STL,
        "json":THREE,
        "awd":AWD,
        "swm":SWM
    }

    print "start...."

    input_model = switch[input_file_type](input_file)
    output_model = switch[output_file_type](output_file)
    shape = input_model.GetShape()
    output_model.SetShape(shape)
    output_model.WriteFile()

    print "done!..."

if __name__ == '__main__':
	main()