# Part of Pearl EnterPrise. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class EmployeeAttendenceReportWizard(models.TransientModel):
    _name = "employee.attendence.report.wizard"
    _description = "Employee Attendance Report Wizard"

    hr_employee_ids = fields.Many2many("hr.employee", string="Employees Selection")
    starting_date = fields.Date(string="Start date", required=True)
    ending_date = fields.Date(string="End date", required=True)

    def generate_employee_pdf_report(self):
        if self.starting_date > self.ending_date:
            raise ValidationError(_("Invalid DATE selection; please select a proper date and month."))
        else:
            data = {
                'form_data': self.read()[0],
            }
            return self.env.ref('bi_hr_attendance_report.action_report_attendence_report_wizard').report_action(self,
                                                                                                                data=data)
