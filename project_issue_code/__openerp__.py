# -*- coding: utf-8 -*-
# © 2016 Michael Viriyananda
# © 2017 Stella Fredö, adapt it to v9
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Project Issue Code",
    "version": "9.0.1.0.0",
    'author': 'Michael Viriyananda, Stella Fredö',
    "category": "Project Management",
    'summary': 'Adding Field Code For Project Issue',
    'website': 'http://github.com/mikevhe18',
    "license": "AGPL-3",
    "depends": [
        "project_issue",
    ],
    "data": [
        "data/project_issue_sequence.xml",
        "views/project_issue_view.xml",
    ],
    "installable": True,
    "pre_init_hook": "create_code_equal_to_id",
    "post_init_hook": "assign_old_sequences",
}
