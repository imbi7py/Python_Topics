____ os.path ______ expanduser
____ ?.QtWidgets ______ *

home_directory _ expanduser('~')

app _ ?A..([])
model _ QDirModel()
view _ QTreeView()
view.sM..(model)
view.setRootIndex(model.index(home_directory))
view.s..
app.exec_()