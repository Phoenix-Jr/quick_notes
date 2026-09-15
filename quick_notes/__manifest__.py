{
    'name': 'Quick Notes',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Gérez vos notes personnelles directement depuis Odoo',
    'description': """
Quick Notes
===========
Créez, modifiez et organisez vos notes personnelles :
titre, contenu, priorité et statut. Chaque utilisateur ne voit que ses propres notes.
""",
    'author': 'Donald Ntsibah',
    'support': 'ntsibahdonald@gmail.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/quick_notes_security.xml',
        'data/quick_note_stage_data.xml',
        'views/quick_note_views.xml',
        'views/quick_note_stage_views.xml',
        'views/quick_note_tag_views.xml',
        'views/quick_notes_menus.xml',
    ],
    'application': True,
    'installable': True,
}
