______ ___
____ ? ______ ?C.. __ qtc
____ ? ______ ?W.. __ qtw
____ ? ______ QtMultimedia __ qtmm
____ ? ______ QtMultimediaWidgets __ qtmmw


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        super().__init__()
        # Main framework
        self.resize(qtc.QSize(800, 600))
        base_widget _ qtw.?W..
        base_widget.sL..(qtw.QHBoxLayout())
        notebook _ qtw.QTabWidget()
        base_widget.layout().aW..(notebook)
        self.file_list _ qtw.QListWidget()
        base_widget.layout().aW..(self.file_list)

        self.sCW..(base_widget)

        # transport controls
        toolbar _ self.addToolBar("Transport")
        record_act _ toolbar.aA..('Rec')
        stop_act _ toolbar.aA..('Stop')
        play_act _ toolbar.aA..('Play')
        pause_act _ toolbar.aA..('Pause')

        # define the video directory
        self.video_dir _ qtc.QDir.home()
        __ no. self.video_dir.cd('captains_log'):
            qtc.QDir.home().mkdir('captains_log')
            self.video_dir.cd('captains_log')

        # Read the files in the directory
        self.refresh_video_list()

        ############
        # Playback #
        ############

        # setup the player and video widget
        self.player _ qtmm.QMediaPlayer()
        self.video_widget _ qtmmw.QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        notebook.addTab(self.video_widget, "Play")

        # connect the transport
        play_act.t__.c..(self.player.play)
        pause_act.t__.c..(self.player.pause)
        stop_act.t__.c..(self.player.stop)
        play_act.t__.c..(
            lambda: notebook.setCurrentWidget(self.video_widget))

        # connect file list
        self.file_list.itemDoubleClicked.c..(
            self.on_file_selected)
        self.file_list.itemDoubleClicked.c..(
            lambda: notebook.setCurrentWidget(self.video_widget))



        #############
        # Recording #
        #############

        # set up camera
        self.camera _ self.camera_check()
        __ no. self.camera:
            self.s..
            r_
        self.camera.setCaptureMode(qtmm.QCamera.CaptureVideo)

        # Create the viewfinder widget for recording
        self.cvf _ qtmmw.QCameraViewfinder()
        self.camera.setViewfinder(self.cvf)
        notebook.addTab(self.cvf, 'Record')

        # start the camera
        self.camera.start()

        # Configure recorder
        self.recorder _ qtmm.QMediaRecorder(self.camera)
        #settings = self.recorder.videoSettings()
        #settings.setResolution(640, 480)
        #settings.setFrameRate(24.0)
        #settings.setQuality(qtmm.QMultimedia.VeryHighQuality)
        #self.recorder.setVideoSettings(settings)

        # connect the transport
        record_act.t__.c..(self.record)
        record_act.t__.c..(
            lambda: notebook.setCurrentWidget(self.cvf)
        )
        pause_act.t__.c..(self.recorder.pause)
        stop_act.t__.c..(self.recorder.stop)

        # refresh the files when the recording is made
        stop_act.t__.c..(self.refresh_video_list)


        self.s..

    ######################
    # Playback callbacks #
    ######################

    ___ refresh_video_list(self):
        self.file_list.clear()
        video_files _ self.video_dir.entryList(
            ["*.ogg", "*.avi", "*.mov", "*.mp4", "*.mkv"],
            qtc.QDir.Files | qtc.QDir.Readable
        )
        for fn in sorted(video_files):
            self.file_list.addItem(fn)

    ___ on_file_selected  item):
        fn _ item.t__()
        url _ qtc.QUrl.fromLocalFile(self.video_dir.filePath(fn))
        content _ qtmm.QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    #######################
    # Recording callbacks #
    #######################

    ___ camera_check(self):
        cameras _ qtmm.QCameraInfo.availableCameras()
        print(cameras)
        __ no. cameras:
            qtw.?MB...critical(
                self,
                'No cameras',
                'No cameras were found, recording disabled.'
            )
        ____
            r_ qtmm.QCamera(cameras[0])

    ___ record(self):
        # create a filename
        datestamp _ qtc.QDateTime.currentDateTime().toString()
        self.mediafile _ qtc.QUrl.fromLocalFile(
            self.video_dir.filePath('log - ' + datestamp)
        )
        self.recorder.setOutputLocation(self.mediafile)
        # start recording
        self.recorder.record()

__ __name__ == '__main__':
    app _ qtw.?A..(___.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
