from odoo import fields, models


class QuickNote(models.Model):
    _name = 'quick.note'
    _description = 'Quick Note'
    _order = 'is_pinned desc, priority desc, write_date desc'

    def _default_stage_id(self):
        return self.env['quick.note.stage'].search([], order='sequence, id', limit=1)

    def _read_group_stage_ids(self, stages, domain):
        return stages.search([], order='sequence, id')

    name = fields.Char(string='Titre', required=True)
    content = fields.Html(string='Contenu')
    priority = fields.Selection(
        [
            ('0', 'Normal'),
            ('1', 'Important'),
            ('2', 'Urgent'),
        ],
        string='Priorité',
        default='0',
    )
    stage_id = fields.Many2one(
        'quick.note.stage',
        string='Statut',
        default=_default_stage_id,
        group_expand='_read_group_stage_ids',
        ondelete='restrict',
    )
    user_id = fields.Many2one(
        'res.users',
        string='Propriétaire',
        default=lambda self: self.env.user,
        required=True,
    )
    tag_ids = fields.Many2many('quick.note.tag', string='Étiquettes')
    deadline = fields.Date(string='Échéance')
    is_pinned = fields.Boolean(string='Épinglée', default=False)
