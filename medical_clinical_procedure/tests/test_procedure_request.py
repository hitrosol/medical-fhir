# Copyright 2017 CreuBlanca
# Copyright 2017 ForgeFlow
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase


class TestProcedureRequest(TransactionCase):
    def setUp(self):
        res = super(TestProcedureRequest, self).setUp()
        self.patient = self.browse_ref("medical_base.patient_01")
        self.plan = self.browse_ref("medical_workflow.mr_knee")
        return res

    def test_procedure_request_workflow(self):
        request = self.env["medical.procedure.request"].create(
            {"patient_id": self.patient.id}
        )
        self.assertNotEqual(request.internal_identifier, "/")
        procedure = request.generate_event()
        self.assertEqual(procedure.procedure_request_id.id, request.id)
        self.assertEqual(request.fhir_state, "draft")
        request.draft2active()
        self.assertEqual(request.fhir_state, "active")
        request.active2suspended()
        self.assertEqual(request.fhir_state, "suspended")
        request.reactive()
        request.active2error()
        self.assertEqual(request.fhir_state, "entered-in-error")
        request.reactive()
        request.active2completed()
        self.assertEqual(request.fhir_state, "completed")
        request.reactive()
        request.cancel()
        self.assertEqual(request.fhir_state, "cancelled")
