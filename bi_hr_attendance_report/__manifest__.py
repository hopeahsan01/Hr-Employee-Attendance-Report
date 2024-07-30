# -*- coding: utf-8 -*-
# Part of Pearl EnterPrise. See LICENSE file for full copyright and licensing details.

{
    "name": "Hr Employee Attendance Report",
    "version": "17.0.0.1",
    "category": "Employee",
    "summary": "print hr attendance pdf report employee attendance report ",
    "description": """The Employee Attendance Report Odoo app allows businesses to streamline attendance tracking,
     generate detailed reports, and ensure effective workforce management.
     Human resource manager can easily generate detailed attendance report based on employee and also can select specific employee in  or PDF format.""",
    "license": "OPL-1",
    "author": "Pearl Enterprise",
    "depends": ["base",
                "hr_attendance",
                "hr",
                ],
    "data": [
        "security/ir.model.access.csv",
        "report/employee_attendence_report_wizard_form.xml",
        "report/employee_attendence_report_wizard_view.xml",
        "wizard/employee_attendence_report_wizard_view.xml",
        "views/hr_employee_view.xml",
    ],
    "auto_install": False,
    "application": True,
    "installable": True,
}
