______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ QtMultimedia __ qtmm

______ resources


c_ SoundButton(qtw.?PB..):

    ___ __init__  wav_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wav_file _ wav_file
        self.player _ qtmm.QSoundEffect()
        self.player.setSource(qtc.QUrl.fromLocalFile(wav_file))
        self.c__.c..(self.player.play)


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        dialpad _ qtw.?W..
        self.sCW..(dialpad)
        dialpad.sL..(qtw.QGridLayout())

        for i, symbol in enumerate('123456789*0#'):
            button _ SoundButton(f':/dtmf/{symbol}.wav', symbol)
            row _ i // 3
            column _ i % 3
            dialpad.layout().aW..(button, row, column)

        # End main UI code
        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(___.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
