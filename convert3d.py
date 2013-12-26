import sys
import os
from Dice3DS import dom3ds
import zlib
import StringIO
import struct

class Model(object):
    def __init__(self,filename):
        self.SetFilename(filename)
        self._shape = None

    def SetFilename(self, filename):
        self._filename = filename

    def ReadFile(self):
         if not os.path.isfile(self._filename):
            print "Error: file %s not found."% self._filename

    def WriteFile(self):
        pass
    def GetShape(self):
        self.ReadFile()
        return self._shape
    def SetShape(self, aShape):
        self._shape = aShape


class Shape(object):
    pass

class z3DS(Model):
    def ReadFile(self):
        dom = dom3ds.read_3ds_file(self._filename,tight=False)
        for j,d_nobj in enumerate(dom.mdata.objects):
            if type(d_nobj.obj) != dom3ds.N_TRI_OBJECT:
                continue
            for d_point in d_nobj.obj.points.array:
                print d_point
                pass
            d_texverts = [ tuple(tpt) for tpt in d_nobj.obj.texverts.array ]
            for d_face in d_nobj.obj.faces.array:
                pass
            for k,d_material in enumerate(d_nobj.obj.faces.materials):
                pass

    def WriteFile(self):
        pass

class DAE(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass

class OBJ(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass

class STL(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass

class THREE(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass

class AWD(Model):
    def ReadFile(self):
        pass
    def WriteFile(self):
        pass

class SWM(Model):
    def compressWrite(self,io, dst, level=9):
        dst = open(dst, 'wb')
        compress = zlib.compressobj(level)
        data = io.read(1024)
        while data:
            dst.write(compress.compress(data))
            data = io.read(1024)
        dst.write(compress.flush())
    def decompressRead(self,infile):
        io = StringIO.StringIO()
        infile = open(infile, 'rb')
        decompress = zlib.decompressobj()
        data = infile.read(1024)
        print type(data)
        while data:
            io.write(decompress.decompress(data))
            data = infile.read(1024)
        io.write(decompress.flush())
        io.seek(0)
        return io

    def ReadFile(self):
        io = self.decompressRead(self._filename)
        obj_number = struct.unpack("!I",io.read(4))[0]
        for i in range(0,obj_number):
            index_number = struct.unpack("!I",io.read(4))[0]
            for j in range(0,index_number):
                print struct.unpack("!I",io.read(4))[0]
            point_number = struct.unpack("!I",io.read(4))[0]
            for j in range(0,point_number):
                print struct.unpack("!d",io.read(8))[0]

    def WriteFile(self):
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