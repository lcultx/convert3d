__author__ = 'ELatA'
import sys
from collada import *
import zlib
import StringIO
import struct

def main():
    dae_path = swm_path = ""
    try:
        dae_path = sys.argv[1]
        swm_path = sys.argv[2]
    except:
        print 'Error: dae or swm path not exist!'
        sys.exit()
    if not os.path.exists(swm_path):
        os.makedirs(swm_path)
    mesh = Collada(dae_path)
    geom = mesh.geometries[0]
    triset = geom.primitives[0]
    swm_i_array = triset.vertex_index
    swm_v_array = triset.vertex
    swm_n_array = triset.normal


    write_swm_i(swm_i_array,swm_path)
    write_swm_n(swm_n_array,swm_path)
    write_swm_v(swm_v_array,swm_path)
    if len(triset.texcoordset)>0:
        swm_t_array = triset.texcoordset[0]
        write_swm_t(swm_t_array,swm_path)


def write_swm_i(array,swm_path):
    io = StringIO.StringIO()
    length = len(array)
    io.write(struct.pack("!I",length))
    for i in array:
        io.write(struct.pack("!I",i))
    dst = os.path.join(swm_path,"swmi")
    compressWrite(io,dst)

def write_swm_n(array,swm_path):
    io = StringIO.StringIO()
    length = len(array)*3
    io.write(struct.pack("!I",length))
    for i in array:
        for j in i:
            io.write(struct.pack("!d",j))
    dst = os.path.join(swm_path,"swmn")
    compressWrite(io,dst)

def write_swm_v(array,swm_path):
    io = StringIO.StringIO()
    length = len(array)*3
    io.write(struct.pack("!I",length))
    for i in array:
        for j in i:
            io.write(struct.pack("!d",j))
    dst = os.path.join(swm_path,"swmv")
    compressWrite(io,dst)

def write_swm_t(array,swm_path):
    io = StringIO.StringIO()
    length = len(array)*2
    io.write(struct.pack("!I",length))
    for i in array:
        for j in i:
            io.write(struct.pack("!d",j))
    dst = os.path.join(swm_path,"swmt")
    compressWrite(io,dst)

def compressWrite(io, dst, level=9):
    dst = open(dst, 'wb')
    compress = zlib.compressobj(level)
    io.seek(0)
    data = io.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = io.read(1024)
    dst.write(compress.flush())

if __name__ == '__main__':
	main()
