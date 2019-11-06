from marshmallow import Schema,fields, pre_load

class ResearcherSchema(Schema):
    email = fields.Email()
    first_name = fields.Str()
    full_name = fields.Str()
    last_name = fields.Str()
    office = fields.Str()
    phone = fields.Str()  #TODO phone field

class ExperimentRefSchema(Schema):
    exp_name = fields.Str()
    experiment_id = fields.Number()
    qualifies = fields.Bool()
    qualifies_text = fields.Str()


class StudyInfoSchema(Schema):
    course_credits = fields.List(fields.Str())
    PI = fields.Str(allow_none=True) #was None TODO
    abstract_text = fields.Str()
    credits_label = fields.Str()
    credits_part1_value = fields.Float(required=False, allow_none=True)
    credits_part2_value = fields.Float(required=False, allow_none=True)
    credits_part3_value = fields.Float(required=False, allow_none=True)
    credits_part4_value = fields.Float(required=False, allow_none=True) #ALL THESE IN VPh part floats
    credits_total_value = fields.Float(required=True)
    description_text = fields.Str() #TODO html code field
    display_timeslots_button = fields.Bool()
    display_timeslots_reason = fields.Str()
    disqualifier_info = fields.Nested(ExperimentRefSchema(many=True))
    disqualifier_text = fields.Str()
    duration_part1 = fields.Float(allow_none=True)
    duration_part2 = fields.Float(allow_none=True) #TODO maybe number not float cause full minutes always?
    duration_part3 = fields.Float(allow_none=True) #all this in minutes number
    duration_part4 = fields.Float(allow_none=True)
    duration_total = fields.Float(required=True) # was 45 Minuten needs to be preprocessed,
    eligibility_reqs = fields.Str(allow_none=True) #was None TODO
    exp_name = fields.Str()
    experiment_id = fields.Number()
    invitation_code_text = fields.Str()
    multipart_count = fields.Number()
    preparation = fields.Str()
    prereq_info = fields.Nested(ExperimentRefSchema(many=True))
    prereq_text = fields.Str()
    researchers = fields.Nested(ResearcherSchema(many=True))
    twopart_study_text = fields.Str()
    website_label = fields.Str()
    website_link_label = fields.Str()
    website_link_text = fields.Str()

    @pre_load
    def duration_credits_float(self, in_data, **kwargs):
        # Credits get float value from "3,5 VPh XXXX" string
        in_data['credits_part1_value'] = float(in_data['credits_part1_value'].replace(" VPh", "")) if in_data['credits_part1_value'] else None
        in_data['credits_part2_value'] = float(in_data['credits_part2_value'].replace(" VPh", "")) if in_data['credits_part2_value'] else None
        in_data['credits_part3_value'] = float(in_data['credits_part3_value'].replace(" VPh", "")) if in_data['credits_part3_value'] else None
        in_data['credits_part4_value'] = float(in_data['credits_part4_value'].replace(" VPh", "")) if in_data['credits_part4_value'] else None
        in_data['credits_total_value'] = float(in_data['credits_total_value'].replace(" VPh", ""))

        #Duration get minutes from " 45 Min XXXX" string
        in_data['duration_part1'] = float(in_data['duration_part1'].strip().split(" ")[0]) if in_data['duration_part1'] else None
        in_data['duration_part2'] = float(in_data['duration_part2'].strip().split(" ")[0]) if in_data['duration_part2'] else None
        in_data['duration_part3'] = float(in_data['duration_part3'].strip().split(" ")[0]) if in_data['duration_part3'] else None
        in_data['duration_part4'] = float(in_data['duration_part4'].strip().split(" ")[0]) if in_data['duration_part4'] else None
        in_data['duration_total'] = float(in_data['duration_total'].strip().split(" ")[0])
        return in_data