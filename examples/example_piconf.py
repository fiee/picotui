# -*- encoding: utf-8 -*-
from picotui import screen as pisc
from picotui import widgets as piwi
from picotui import defs as pide
import piconf


def Customers():
    return ('one', 'two', 'three', 'four', 'five')


def Countries():
    return ('Germany', 'Switzerland', 'Austria')


DIALOGS = {
    'invoice_head': {
        'title': 'Invoice',
        'idprefix': 'inv',  # not yet used
        'widgets': [
            {'id': 'date', 'label': 'Invoice Date', 'type': 'date', 'length': 10, 'value': '1970-01-01'},
            {'id': 'no', 'label': 'Invoice Number', 'length': 30},
            {'id': 'orderdate', 'label': 'Order Date', 'type': 'date', 'length': 10},
            {'id': 'ordercode', 'label': 'Order Code', 'length': 30},
            {'id': 'discount', 'label': 'Discount', 'type': 'int', 'length': 3},
            {'id': 'tax', 'label': 'Tax Mode', 'type': 'radio', 'choices': ['netto', 'brutto']},
        ]
    },
    'customer': {
        'title': 'Customer',
        'idprefix': 'cust',
        'widgets': [
            {'id': 'title', 'label': '', 'type': 'label', 'value': 'New Customer'},
            {'id': 'code', 'label': 'Code', 'type': 'auto', 'length': 30, 'choices': Customers},
            {'id': 'company', 'label': 'Company', 'length': 30, 'value': 'fiee visuelle'},
            {'id': 'name', 'label': 'Name', 'length': 30, 'value': 'Hraban Ramm'},
            {'id': 'street', 'label': 'Street', 'length': 30},
            {'id': 'city', 'label': 'City', 'length': 30},
            {'id': 'zip', 'label': 'ZIP', 'length': 8},
            {'id': 'country', 'label': 'Country', 'type': 'combo', 'length': 30, 'choices': Countries, 'value': 'Germany'},
        ],
        'buttons': [
            {'id': 'OK', 'label': 'Ok', 'finish_action': piwi.ACTION_OK },
            {'id': 'Cancel', 'label': 'Cancel', 'finish_action': piwi.ACTION_CANCEL },
        ]
    }
}


def show(dialog):
    s = pisc.Screen()
    try:
        s.init_tty()
        s.enable_mouse()
        s.attr_color(pide.C_BLACK, pide.C_YELLOW)
        s.cls()
        s.attr_reset()
        res = dialog.loop()
    finally:
        s.goto(0, 50)
        s.cursor(True)
        s.disable_mouse()
        s.deinit_tty()
    return res


if __name__ == '__main__':
    values = {}
    values = show(piconf.dialog_factory(DIALOGS['customer'], values))
    # print(values)
