____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
______ sys


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        super().__init__()

        # Your code goes here
        self.resize(800, 600)
        main _ qtw.?W..
        self.sCW..(main)
        main.sL..(qtw.QVBoxLayout())
        oglw _ GlWidget()
        main.layout().aW..(oglw)

        # Animation controls
        btn_layout _ qtw.QHBoxLayout()
        main.layout().addLayout(btn_layout)
        for direction in ('none', 'left', 'right', 'up', 'down'):
            button _ qtw.?PB..(
                direction,
                autoExclusive_True,
                checkable_True,
                c___getattr(oglw, f'spin_{direction}')
                )
            btn_layout.aW..(button)
        zoom_layout _ qtw.QHBoxLayout()
        main.layout().addLayout(zoom_layout)
        zoom_in _ qtw.?PB..('zoom in', c___oglw.zoom_in)
        zoom_layout.aW..(zoom_in)
        zoom_out _ qtw.?PB..('zoom out', c___oglw.zoom_out)
        zoom_layout.aW..(zoom_out)
        self.s..


c_ GlWidget(qtw.QOpenGLWidget):
    """A widget to display our OpenGL drawing"""

    ___ initializeGL(self):
        super().initializeGL()

        # Fetch version-specific functions
        gl_context _ self.context()
        version _ qtg.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl _ gl_context.versionFunctions(version)

        # Configure
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glDepthFunc(self.gl.GL_LESS)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

        # Create the program
        self.program _ qtg.QOpenGLShaderProgram()
        self.program.addShaderFromSourceFile(
            qtg.QOpenGLShader.Vertex, 'vertex_shader.glsl')
        self.program.addShaderFromSourceFile(
            qtg.QOpenGLShader.Fragment, 'fragment_shader.glsl')
        self.program.link()

        # Get variable locations
        self.vertex_location _ self.program.attributeLocation('vertex')
        self.matrix_location _ self.program.uniformLocation('matrix')
        self.color_location _ self.program.attributeLocation('color_attr')

        # Create transformation matrix
        self.view_matrix _ qtg.QMatrix4x4()
        self.view_matrix.perspective(
            45,  # Angle
            self.width() / self.height(),  # Aspect Ratio
            0.1,  # Near clipping plane
            100.0  # Far clipping plane
        )
        self.view_matrix.translate(0, 0, -5)
        self.rotation _ [0, 0, 0, 0]

    ___ paintGL(self):
        # Fill the window with dark violet
        self.gl.glClearColor(0.1, 0, 0.2, 1)
        self.gl.glClear(
            self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.program.bind()

        # Drawing
        front_vertices _ [
            qtg.QVector3D(0.0, 1.0, 0.0),  # Peak
            qtg.QVector3D(-1.0, 0.0, 0.0),  # Bottom left
            qtg.QVector3D(1.0, 0.0, 0.0)  # Bottom right
            ]

        face_colors _ (
            qtg.?C..('red'),
            qtg.?C..('orange'),
            qtg.?C..('yellow'),
        )
        gl_colors _ [
            self.qcolor_to_glvec(color)
            for color in face_colors
        ]
        self.program.setUniformValue(
            self.matrix_location, self.view_matrix)
        self.program.enableAttributeArray(self.vertex_location)
        self.program.setAttributeArray(self.vertex_location, front_vertices)
        self.program.enableAttributeArray(self.color_location)
        self.program.setAttributeArray(self.color_location, gl_colors)

        # Draw the front
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)
        # Draw the back
        back_vertices _ [
            qtg.QVector3D(x.toVector2D(), -0.5)
            for x in front_vertices]
        self.program.setAttributeArray(
            self.vertex_location, reversed(back_vertices))
            # If you try the line below instead, the back side
            # will not show unless you disable face culling
            #self.vertex_location, back_vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)

        # draw the sides
        sides _ [(0, 1), (1, 2), (2, 0)]
        side_vertices _ list()
        for index1, index2 in sides:
            side_vertices +_ [
                front_vertices[index1],
                back_vertices[index1],
                back_vertices[index2],
                front_vertices[index2]
            ]
        side_colors _ [
            qtg.?C..('blue'),
            qtg.?C..('purple'),
            qtg.?C..('cyan'),
            qtg.?C..('magenta'),
        ]
        gl_colors _ [
            self.qcolor_to_glvec(color)
            for color in side_colors
        ] * 3

        self.program.setAttributeArray(self.color_location, gl_colors)
        self.program.setAttributeArray(self.vertex_location, side_vertices)
        self.gl.glDrawArrays(self.gl.GL_QUADS, 0, le.(side_vertices))
        self.program.disableAttributeArray(self.vertex_location)
        self.program.disableAttributeArray(self.color_location)
        self.program.release()

        # Animation
        # rotate
        self.view_matrix.rotate(*self.rotation)
        self.update()

    ___ qcolor_to_glvec  qcolor):
        r_ qtg.QVector3D(
            qcolor.red() / 255,
            qcolor.green() / 255,
            qcolor.blue() / 255
        )

    ___ spin_none(self):
        self.rotation _ [0, 0, 0, 0]

    ___ spin_left(self):
        self.rotation _ [-1, 0, 1, 0]

    ___ spin_right(self):
        self.rotation _ [1, 0, 1, 0]

    ___ spin_up(self):
        self.rotation _ [1, 1, 0, 0]

    ___ spin_down(self):
        self.rotation _ [-1, 1, 0, 0]

    ___ zoom_in(self):
        self.view_matrix.scale(1.1, 1.1, 1.1)

    ___ zoom_out(self):
        self.view_matrix.scale(.9, .9, .9)


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    mw _ MainWindow()
    app.e..
