_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ reservehotel _____ _

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ ?
        ui.sU..
        roomtypes_['Suite', 'Super Luxury', 'Super Deluxe', 'Ordinary']
        addcontent()     
        ui.pushButton.c___.c..(computeRoomRent)
        s..

    ___ addcontent 
        ___ i __ roomtypes:
          ui.comboBox.aI..(i)
     
    ___ computeRoomRent 
        dateselected_ui.cW__.selectedDate()
        dateinstring_st.(dateselected.toPyDate())
        noOfDays_ui.spinBox.v..
        chosenRoomType_ui.comboBox.iT..(ui.comboBox.cI..())
        ui.Enteredinfo.sT..('Date of reservation: '+dateinstring+ ', Number of days: '+ st.(noOfDays) + ' \nand Room type selected: '+ chosenRoomType)
        roomRent_0
        __ chosenRoomType__"Suite":
          roomRent_40
        __ chosenRoomType__"Super Luxury":
          roomRent_30
        __ chosenRoomType__"Super Deluxe":
          roomRent_20
        __ chosenRoomType__"Ordinary":
          roomRent_10
        total_roomRent*noOfDays
        ui.RoomRentinfo.sT..('Room Rent for single day for '+ chosenRoomType +' type is '+ st.(roomRent)+ '$. \nTotal room rent is '+ st.(total)+ '$')
 
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
