import unittest
from evidence_and_tool_guard import Evidence, select_evidence, evidence_preview, authorize_tool, DeniedToolCall

class EvidenceTests(unittest.TestCase):
    def test_best_sources_first_and_deduplicated(self):
        a=Evidence("guide","c1","First excerpt",0.8)
        b=Evidence("guide","c2","Second excerpt",0.95)
        self.assertEqual([x.chunk_id for x in select_evidence([a,b,a])],["c2","c1"])
    def test_abstains_without_evidence(self):
        self.assertEqual(evidence_preview([Evidence("guide","c1","low",0.1)])["status"],"insufficient_evidence")
    def test_empty_text_is_not_evidence(self):
        self.assertEqual(select_evidence([Evidence("guide","c1","  ",0.99)]),[])
    def test_source_id_is_validated(self):
        self.assertEqual(select_evidence([Evidence("../etc/passwd","c1","bad id",0.99)]),[])
    def test_citations_expose_source_and_chunk(self):
        r=evidence_preview([Evidence("guide","c1","Supported excerpt",0.9)])
        self.assertEqual(r["citations"][0]["source"],"guide")
        self.assertIsNone(r["answer"])
    def test_valid_tool_call_is_only_authorized_not_executed(self):
        r=authorize_tool("lookup_order_status",{"order_id":"ORD-1234"},{"lookup_order_status"})
        self.assertEqual(r["executed"],"false")
    def test_unknown_tool_rejected(self):
        with self.assertRaises(DeniedToolCall):authorize_tool("send_bulk_emails",{},{"lookup_order_status"})
    def test_permission_rejected(self):
        with self.assertRaises(DeniedToolCall):authorize_tool("lookup_order_status",{"order_id":"ORD-1234"},set())
    def test_extra_args_rejected(self):
        with self.assertRaises(DeniedToolCall):authorize_tool("lookup_order_status",{"order_id":"ORD-1234","secret":"x"},{"lookup_order_status"})
    def test_invalid_id_rejected(self):
        with self.assertRaises(DeniedToolCall):authorize_tool("lookup_order_status",{"order_id":"../../etc"},{"lookup_order_status"})

if __name__=="__main__":unittest.main(verbosity=2)