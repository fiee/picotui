import copy
from picotui import widgets as piwi
from .defaults import WIDGETS, SETTINGS


__all__ = ['defaults', 'dialog_factory']


def dialog_factory(data, values={}):
    """
    Create a dialog from configuration data.
    See ``examples/example_piconf.py``

    Params:
    `data` (dict)
    `values` (dict)

    Returns:
    `picotui.Dialog`
    """
    widgets = {}
    dlg = copy.deepcopy(SETTINGS)
    dlg.update(data)
    d = piwi.Dialog(
        dlg['x'],
        dlg['y'],
        w=dlg['w'],
        h=dlg['h'],
        title=dlg['title']
    )
    # find maximum length of label and fields
    label_len = dlg['label_min_width']
    field_len = dlg['field_min_width']
    count = 0
    for wg in dlg['widgets']: # 'widgets' is a list of dict
        wdg = copy.deepcopy(dlg['widget']) # 'widget' is a dict from defaults
        wdg.update(wg)
        label_len = max(label_len, len(wg['label']))
        if 'length' in wdg:
            field_len = max(field_len, wg['length'])
        if 'choices' in wdg:
            # call choices
            if callable(wdg['choices']):
                wdg['choices'] = wdg['choices']()
            for c in wdg['choices']:
                field_len = max(field_len, len(c))
        dlg['widgets'][count] = wdg
        count += 1
    # add labels and fields
    line = dlg['start_y']
    label_x = dlg['start_x']
    field_x = label_x + dlg['gap_x'] + label_len
    for wg in dlg['widgets']:
        try:
            # is there a value set for this widget?
            val = values[wg['id']]
        except KeyError:
            val = ''
            if 'default' in wg:
                val = wg['default']
            elif 'value' in wg:
                val = wg['value']
        wdg = copy.deepcopy(dlg['widget'])
        wdg.update(wg)
        WClass = WIDGETS[wdg['type']]
        # add label
        d.add(label_x, line, wdg['label'])
        # add widget
        if wdg['type'] in ('text', 'date', 'int', 'float'):
            # simple entries have a length and a value
            widgets[wdg['id']] = WClass(wdg['length'], val)
        elif wdg['type'] == 'label':
            widgets[wdg['id']] = WClass(val)
        elif wdg['type'] in ('combo', 'auto', 'multi', 'list', 'drop'):
            # complex widgets have also a list of choices
            if wdg['type'] == 'drop':
                # Dropdown has no value
                widgets[wdg['id']] = WClass(wdg['length'], wdg['choices'])
            else:
                widgets[wdg['id']] = WClass(wdg['length'], val, wdg['choices'])
        else:
            print('Not yet implemented: widget %s' % wdg['type'])
            widgets[wdg['id']] = WClass()
        d.add(field_x, line, widgets[wdg['id']])
        line += 1 + dlg['gap_y']
    # add empty label to extend auto width
    d.add(field_x + field_len, dlg['start_y'], ' ' * dlg['gap_x'])
    # add buttons
    bt_min_width = dlg['button_min_width']
    bt_distance = dlg['button_gap']
    bt_x = label_x
    for bt in dlg['buttons']:
        bt_width = max(len(bt), bt_min_width)
        d.add(bt_x, line, WIDGETS['button'](bt_width, bt))
        bt_x += bt_width + bt_distance
    return d
