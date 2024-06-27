function toggleDropdown(element) {
    console.log('toggle');
    a = 0;
    switch (element) {
        case "toggle1":
            a = 1
            break;
        case "toggle2":
            a = 2;
            break;
        case "toggle3":
            a = 3;
            break;
    }

    dropDownlist = '.dropdown-inlist* .dropdown-content'
    dropDownlist = dropDownlist.replace('*', a)

    if ($(dropDownlist).hasClass('show')) {
        $(dropDownlist).hide();
        $(dropDownlist).removeClass('show');
    }
    else {
        $(dropDownlist).show();
        $(dropDownlist).addClass('show');
    }
}