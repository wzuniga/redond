# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Player(models.Model):
    _name = 'system.player'
    _rec_name = 'player_name'

    player_name = fields.Char(string="Nombre",
    						  size=40,
    						  required=True,
    						  help="Nombre del Jugador")

    debts_ids = fields.One2many("system.debt",
    							"player_ids",
    							string="Deudas"
    							)

    total_debts = fields.Char(string="Total Deudas",
                              compute="_all_debts",
                              help="Total de prestamos hechos"
                              )

    payments_ids = fields.One2many("system.payment",
    							   "player_ids",
                                   string="Pagos")

    total_payments = fields.Char(string="Total Pagos",
                                 compute="_all_payments",
                                 help="Total de pagos hechos")

    #TODO debts relacion
    @api.one
    @api.depends('payments_ids')
    def _all_payments(self):
        self.total_payments = " "
        count = 0
        for c in self.payments_ids:
            count += c.monto_payment

        self.total_payments = str(count)
    
    @api.one
    @api.depends('debts_ids')
    def _all_debts(self):
        self.total_debts = " "
        count = 0
        for c in self.debts_ids:
            count += c.monto_debt

        self.total_debts = str(count)
    

class Debt(models.Model):
	_name = 'system.debt'
	_rec_name = 'monto_debt'

	monto_debt = fields.Integer(string="Monto",
								required=True,
								help="Monto que se desea prestar")
	player_ids = fields.Many2one('system.player',
								 'Jugador',
								 required=True,
								 help="Jugador que quiere hacer un prestamo")

class Payment(models.Model):
	_name = 'system.payment'
	_rec_name = 'monto_payment'

	monto_payment = fields.Integer(string="Monto",
								   required=True,
								   help="Monto a pagar")

	player_ids = fields.Many2one('system.player',
								 'Jugador',
								 required=True,
								 help="Jugador que quiere hacer un pago")

