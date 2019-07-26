from picotui import widgets as piwi
# from picotui import defs as pide

WIDGETS = {
    'text': piwi.WTextEntry,
    'label': piwi.WLabel,
    'drop': piwi.WDropDown,
    'combo': piwi.WComboBox,
    'auto': piwi.WAutoComplete,
    'multi': piwi.WMultiEntry,
    'check': piwi.WCheckbox,
    'radio': piwi.WRadioButton,
    'list': piwi.WListBox,
    'button': piwi.WButton,
    # need new widgets or validators:
    'date': piwi.WTextEntry,
    'int': piwi.WTextEntry,
    'float': piwi.WTextEntry,
}

SETTINGS = {
    'x': 2,
    'y': 1,
    'w': 0,
    'h': 0,
    'title': '',
    'buttons': [
        {'id': 'OK', 'label': 'Ok', 'finish_action': piwi.ACTION_OK },
        {'id': 'CANCEL', 'label': 'Cancel', 'finish_action': piwi.ACTION_CANCEL },
    ],
    'widget': {'type': 'text', 'label': ''},
    'start_x': 3,  # x of label
    'start_y': 2,  # y of first field
    'gap_x': 3,    # distance (chars) between label and field
    'gap_y': 1,    # distance (lines) between fields
    'label_min_width': 0,
    'field_min_width': 2,
    'button_min_width': 4,
    'button_gap': 3,
}
