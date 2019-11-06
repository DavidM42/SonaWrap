from marshmallow import Schema,fields

class MainMenuInfoSchema(Schema):
    announcement_display = fields.Bool()
    announcement_name = fields.Str()
    announcement_text = fields.Str()
    credits_display = fields.Bool()
    credits_earned = fields.Float()
    credits_name = fields.Str()
    credits_needed = fields.Float()
    credits_pending = fields.Float()
    email_questions_text = fields.Str()
    faq_enabled = fields.Bool()
    logo_url = fields.Url()
    #TODO what this cause for now was null
    # signups = fields.List(field)
    signups_display = fields.Bool()
    signups_name = fields.Str()
    site_name = fields.Str()
    username_name = fields.Str()
    username_text = fields.Str()
    username_type = fields.Str()