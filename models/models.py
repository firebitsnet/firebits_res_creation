from odoo import models,fields,api,_

hq_warnning = _(""" 
The HQ or your manager has stoped the resources creation at this moment. 
Please contact them if you think this is a problem.
""")

class ResourcesAccessMixin(models.AbstractModel):
    _name = "res.firebits.mixin"

    def create(self, vals):

        if self.env.user:
            if not self.env.user.has_group('firebits_res_creation.group_create_res'):
                raise AccessError(hq_warnning)

        return super().create(vals)

    def unlink(self):

        if self.env.user:
            if not self.env.user.has_group('firebits_res_creation.group_create_res'):
                raise AccessError(hq_warnning)

        return super().unlink()

