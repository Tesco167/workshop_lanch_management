from odoo import models, fields, api, exceptions


class TestGithub(models.Model):
    _name = 'test.github'

    name = fields.Char(
        string="Name",
        required=True,
    )