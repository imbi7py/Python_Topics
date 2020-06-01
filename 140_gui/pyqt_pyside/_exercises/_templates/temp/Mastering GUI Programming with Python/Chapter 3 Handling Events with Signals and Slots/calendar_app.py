______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ CategoryWindow ?.?W..
    """A basic dialog to demonstrate inter-widget communication"""

    # when submitted, we'll emit this signal
    # with the entered string
    submitted _ qtc.pS.. st.

    ___  -
        s_. - N.. modal_ st.

        sL.. ?.?VBL..
        l__ .aW..
            ?.?L..('Please enter a new catgory name:')
            )
        category_entry _ ?.?LE..
        la__ .aW.. ?

        submit_btn _ ?.?PB..
            'Submit',
            c___self.oS..
            
        la__ .aW.. ?
        cancel_btn _ ?.?PB..
            Cancel
            c___self.d..
            )
        la__ .aW.. ?
        s..

    ??.?
    ___ oS..
        __ c_e_.t__
            su__.e.. c_e_.t__
        c..


c_ MainWindow ?.?W..

    events _   # dict

    ___  -
        """MainWindow constructor. """
        s_. -
        # Configure the window
        sWT..("My Calendar App")
        r.. 800, 600


        # Create our widgets
        calendar _ ?.?CW..
        event_list _ ?.?LW..
        event_title _ ?.?LE..
        event_category _ ?.?CB..
        event_time _ ?.?TE..(qtc.?T.. 8, 0
        allday_check _ ?.?CB.. All Day
        event_detail _ ?.?TE..
        add_button _ ?.?PB.. Add/Update
        del_button _ ?.?PB.. Delete

        # Configure some widgets

        # Add event categories
        e_c_.aI..
            'Select category…', 'New…', 'Work',
             'Meeting', 'Doctor', 'Family']

        # disable the first category item
        e_c_.model().item(0).sE.. F..

        # Arrange the widgets
        main_layout _ ?.?HBL..
        sL..(main_layout)
        main_layout.aW..(calendar)
        # Calendar expands to fill the window
        calendar.sSP..(
            ?.?SP...E..,
            ?.?SP...E..
        )
        right_layout _ qtw.?VBL..
        main_layout.aL..(right_layout)
        right_layout.aW..(?.?L..('Events on Date'))
        right_layout.aW..(event_list)
        # Event list expands to fill the right area
        event_list.sSP..(
            ?.?SP...E..,
            ?.?SP...E..
            )

        # Create a sub-layout for the event view/add form
        event_form _ ?.?GB..('Event')
        right_layout.aW..(event_form)
        event_form_layout _ ?.?GL..
        event_form_layout.aW..(event_title, 1, 1, 1, 3)
        event_form_layout.aW..(e_c_, 2, 1)
        event_form_layout.aW..(event_time, 2, 2,)
        event_form_layout.aW..(allday_check, 2, 3)
        event_form_layout.aW..(event_detail, 3, 1, 1, 3)
        event_form_layout.aW..(add_button, 4, 2)
        event_form_layout.aW..(del_button, 4, 3)
        event_form.sL..(event_form_layout)



        ##################
        # Connect Events #
        ##################

        # disable time when "all day" is checked.
        allday_check.toggled.c..(event_time.setDisabled)

        # Populate the event list when the calendar is clicked
        calendar.selectionChanged.c..(populate_list)

        # Populate the event form when an item is selected
        event_list.itemSelectionChanged.c..(populate_form)

        # Save event when save is hit
        add_button.c__.c..(save_event)

        # connect delete button
        del_button.c__.c..(delete_event)

        # Enable 'delete' only when an event is selected
        event_list.itemSelectionChanged.c..(
            check_delete_btn)
        check_delete_btn()

        # check for selection of "new…" for category
        e_c_.currentTextChanged.c..(on_category_change)

        s..

    ___ clear_form 
        event_title.clear()
        e_c_.setCurrentIndex(0)
        event_time.setTime(qtc.?T..(8, 0))
        allday_check.setChecked F..
        event_detail.sPT..('')

    ___ populate_list 
        event_list.clear()
        clear_form()
        date _ calendar.selectedDate()
        ___ event __ events.g..(date,   # list):
            time _ (
                event['time'].toString('hh:mm')
                __ event['time']
                else 'All Day'
            )
            event_list.aI..(f"{time}: {event['title']}")

    ___ populate_form 
        clear_form()
        date _ calendar.selectedDate()
        event_number _ event_list.currentRow()
        __ event_number == -1:
            r_

        event_data _ events.g..(date)[event_number]

        e_c_.setCurrentText(event_data['category'])
        __ event_data['time'] __ N..:
            allday_check.setChecked( st.
        ____
            event_time.setTime(event_data['time'])
        event_title.sT..(event_data['title'])
        event_detail.sPT..(event_data['detail'])

    ___ save_event 
        event _ {
            'category': e_c_.currentText(),
            'time': (
                N..
                __ allday_check.isChecked()
                else event_time.time()
                ),
            'title': event_title.t__(),
            'detail': event_detail.toPlainText()
            }

        date _ calendar.selectedDate()
        event_list _ events.g..(date,   # list)
        event_number _ event_list.currentRow()

        # if no events are selected, this is a new event
        __ event_number == -1:
            event_list.ap..(event)
        ____
            event_list[event_number] _ event

        event_list.sort(key_lambda x: x['time'] or qtc.?T..(0, 0))
        events[date] _ event_list
        populate_list()

    ___ delete_event 
        date _ calendar.selectedDate()
        row _ event_list.currentRow()
        del(events[date][row])
        event_list.setCurrentRow(-1)
        clear_form()
        populate_list()

    ___ check_delete_btn 
        del_button.setDisabled(event_list.currentRow() == -1)

    ___ on_category_change  t__):
        __ t__ == 'New…':
            dialog _ CategoryWindow()
            dialog.submitted.c..(add_category)
            e_c_.setCurrentIndex(0)

    ___ add_category  category):
        e_c_.aI..(category)
        e_c_.setCurrentText(category)

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
