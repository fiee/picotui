piconf
======

Picotui is nice, but it could be easier.
This package allows for configuration-driven dialog setup.

Work in progress...

At the moment there’s just one function, ``dialog_factory``.

Have a look at ``examples/example_piconf.py``.

Define a nested dict of dialog configuration::

        DIALOGS = {
            'invoice_head': {  # internal name
                'title': 'Invoice',  # dialog title
                'idprefix': 'inv',  # not yet used
                'widgets': [
                    {'id': 'date', 'label': 'Invoice Date', 'type': 'date', 'length': 10},
                    {'id': 'no', 'label': 'Invoice Number', 'length': 30},
                    {'id': 'orderdate', 'label': 'Order Date', 'type': 'date', 'length': 10},
                    {'id': 'ordercode', 'label': 'Order Code', 'length': 30},
                    {'id': 'discount', 'label': 'Discount', 'type': 'int', 'length': 3},
                    {'id': 'tax', 'label': 'Tax Mode', 'type': 'radio', 'choices': ['netto', 'brutto']},
                ],
                'buttons': [
                    {'id': 'OK', 'label': 'Ok',
                    'finish_action': picotui.widgets.ACTION_OK },
                    {'id': 'Cancel', 'label': 'Cancel',
                    'finish_action': picotui.widgets.ACTION_CANCEL },
                ]
            },
            # ... more
        }

        mydialog = piconf.dialog_factory(DIALOGS['invoice_head'], {})

Each item of 'widgets' will become a label plus field.
You need to define only those values that differ from defaults (see ``defaults.py``).

* ``id``: id of the widget and its values
* ``label``: text of the label (default: '')
* ``length``: width of the field in characters
* ``type``: widget type (default: 'text')

  + ``text``: WTextEntry
  + ``label``: WLabel only (not yet implemented)
  + ``drop``: WDropDown
  + ``combo``: WComboBox
  + ``auto``: WAutoComplete
  + ``multi``: WMultiEntry
  + ``check``: WCheckbox
  + ``radio``: WRadioButton
  + ``list``: WListBox
  + ``button``: WButton (not yet implemented)
  + ``date``: WTextEntry (needs new widget for date entry)
  + ``int``: WTextEntry for integer values (needs validators or new widget)
  + ``float``: WTextEntry for float values (needs validators or new widget)

* ``choices``: iterable or callable that returns an interable, for selection
  widgets (drop, combo, auto, multi, radio, list)

The configured widgets will get added in two columns (labels, fields).
Feel free to add more to the returned dialog.

Dialog data can overwrite all of the default values:

* ``x`` (default: 2), x position of the dialog
* ``y`` (default: 1), y position of the dialog
* ``w`` (default: 0), width of the dialog (0 = auto)
* ``h`` (default: 0), height of the dialog (0 = auto)
* ``title`` (default: '')
* ``buttons`` (default: ``['Ok', 'Cancel']``) – see example
* ``widget`` (default: ``{ 'type': 'text', 'label': '' }``), default values
  for every widget
* ``start_x`` (default: 3), x position of labels
* ``start_y`` (default: 2), y position of first label/field
* ``gap_x`` (default: 3), distance (chars) between label and field
* ``gap_y`` (default: 1), distance (lines) between fields
* ``label_min_width`` (default: 0), minimum width of labels
  (actual/maximum width is calculated)
* ``field_min_width`` (default: 2), minimum width of fields
  (actual/maximum width is calculated)
* ``button_min_width`` (default: 4), minimum width of buttons
  (actual/maximum width is calculated)
* ``button_gap`` (default: 3), distance between automatically placed buttons

ATM buttons are only handled in the button area, not in the widgets area.
They can have a ``finish_action`` (``picotui``: ``finish_dialog``) or an ``on_click`` handler.


Roadmap
-------

* return values
* make buttons work (also between other widgets)
* include missing ``picotui`` widgets
* validators
* add some more widgets (date, int, float...)


Author
------

fiëé visuëlle, Henning Hraban Ramm, <hraban@fiee.net>
