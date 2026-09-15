from odoo import fields, models


class QuickNoteStage(models.Model):
    _name = 'quick.note.stage'
    _description = 'Quick Note Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Nom', required=True, translate=True)
    sequence = fields.Integer(string='Séquence', default=10)
    fold = fields.Boolean(string='Replié dans le Kanban')
