

def plot_points(in_file, out_file, interactive=False) -> None:
    """ This function plots data from file after predetermined affine transformation
    :param in_file: text file with x,y coordiante of points
    :param out_file: file to save plot
    :param interactive: bool, if True show interective pyplot GUI, if False save to file

    in_file should contain data in next format:
    2 3
    4 5
    3 5
    ...
    """
    O = pi/2
    C = (480, 480)
    # Loading data from dataset
    data = numpy.loadtxt(DataSet)

    # Adding ones column
    data = numpy.c_[data, numpy.ones(len(data))]
    
    # Matrices with transofrmation
    T1 = numpy.matrix(((1,0,0),
                       (0,1,0),
                       (-C[0], -C[1], 1)))
    
    T2 = numpy.matrix(((cos(O), sin(O), 0),
                       (-sin(O), cos(O), 0),
                       (0, 0, 1)))

    T3 = numpy.matrix(((1, 0, 0),
                       (0, 1, 0),
                       (C[0], C[1], 1)))


    # Pretty inefective way, yet it works ;)
    for vec in data:
        m = vec @ T1 @ T2 @ T3
        m = numpy.delete(m, 2)
        x, y = numpy.hsplit(m, 2)
        plt.plot(y, x, "o", color="blue")

    # Setting canvas size to 960x960
    plt.axis([0, 960, 0, 960])
    
    # Show Pyplot GUI or not
    if interactive:
        plt.show()
    else:
        plt.savefig(out_file)


if __name__ == "__main__":
    import numpy
    import matplotlib.pyplot as plt
    from math import sin, cos, pi

    DataSet = "DS8.txt"
    OutFile = "DS8.png"
    plot_points(DataSet, OutFile)
