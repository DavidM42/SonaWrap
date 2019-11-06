from marshmallow import Schema,fields, pre_load

class ScheduleSchema(Schema):
    course_credits = fields.List(fields.Str())
    display_course_credits = fields.Bool()
    display_overall_credits = fields.Bool()
    overall_credits_earned = fields.Float()
    overall_credits_needed = fields.Float()
    study_signups = fields.List(fields.Str())
    text_progress_display = fields.Str()

    @pre_load
    def credits_floatification(self, in_data, **kwargs):
        # converts cause real content is stupid
        in_data["overall_credits_earned"] = in_data["overall_credits_earned"].split(":")[1]
        in_data["overall_credits_needed"] = in_data["overall_credits_needed"].split(":")[1]
        return in_data

