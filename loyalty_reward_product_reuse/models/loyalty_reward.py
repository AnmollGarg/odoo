# -*- coding: utf-8 -*-
from odoo import api, fields, models

class LoyaltyReward(models.Model):
    _inherit = 'loyalty.reward'

    def _create_missing_discount_line_products(self):
        # We override this completely to reuse existing service products with the SAME NAME.
        # This prevents creating a new product for EVERY single reward.
        rewards = self.filtered(lambda r: not r.discount_line_product_id)
        
        for reward in rewards:
            if not reward.description:
                continue
                
            # Look for an existing product with the exact same name
            existing_product = self.env['product.product'].search([
                ('name', '=', reward.description),
                ('type', '=', 'service')
            ], limit=1)
            
            if existing_product:
                reward.discount_line_product_id = existing_product
            else:
                # Create a new one if it doesn't exist
                new_product = self.env['product.product'].create({
                    'name': reward.description,
                    'type': 'service',
                    'sale_ok': False,
                    'purchase_ok': False,
                    'lst_price': 0.0,
                })
                reward.discount_line_product_id = new_product

    def write(self, vals):
        if 'description' in vals:
            # If the description changes, we unset the product so that Odoo doesn't 
            # rename our shared product. It will then recreate/relink the correct one.
            vals['discount_line_product_id'] = False
            
        return super(LoyaltyReward, self).write(vals)
