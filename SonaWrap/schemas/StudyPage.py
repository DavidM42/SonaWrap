from marshmallow import Schema,fields


class StudySchema(Schema):
    #TODO create html field for these like exp name which contain html
    exp_name = fields.Str()
    experiment_id = fields.Int()
    first_line = fields.Str()
    second_line = fields.Str()
    timeslots_available = fields.Bool()
    web_flag = fields.Bool()


class StudyPageSchema(Schema):
    # study_signups = fields.List(fields.Str())
    #TODO what with this
    # study_signups = fields.Nested(StudySchema(many=True))
    application_text = fields.Str()
    studies = fields.Nested(StudySchema(many=True))