from odoo import fields, models


class QuickNoteTag(models.Model):
    _name = 'quick.note.tag'
    _description = 'Quick Note Tag'
    _order = 'name'

    name = fields.Char(string='Nom', required=True)
    color = fields.Integer(string='Couleur')

    _name_uniq = models.Constraint(
        'unique (name)',
        "Cette étiquette existe déjà.",
    )
