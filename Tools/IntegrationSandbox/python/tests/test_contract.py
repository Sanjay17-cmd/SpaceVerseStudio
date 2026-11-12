from pathlib import Path
import json
import unittest

from google.protobuf import json_format

from spaceverse.v1 import simulation_pb2 as pb
from spaceverse_mock.model import MOCK_RUN_ID, make_snapshot
from spaceverse_mock.validation import validate_snapshot

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "fixtures" / "sample_snapshot.json"


class ContractTests(unittest.TestCase):
    def test_sample_fixture_parses_and_validates(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        snapshot = json_format.ParseDict(payload, pb.StateSnapshot())
        validate_snapshot(snapshot)
        self.assertEqual(snapshot.entity_id, "terra-001")
        self.assertEqual(snapshot.position_unit, pb.LENGTH_UNIT_KILOMETER)

    def test_generator_is_deterministic(self):
        a = make_snapshot("terra-001", 12, 6.0, MOCK_RUN_ID)
        b = make_snapshot("terra-001", 12, 6.0, MOCK_RUN_ID)
        validate_snapshot(a)
        self.assertEqual(a.SerializeToString(deterministic=True),
                         b.SerializeToString(deterministic=True))

    def test_multiple_entities_have_distinct_ids_and_states(self):
        a = make_snapshot("terra-001", 0, 0.0)
        b = make_snapshot("demo-sat-002", 0, 0.0)
        self.assertNotEqual(a.entity_id, b.entity_id)
        self.assertNotEqual(a.position.x, b.position.x)

    def test_unspecified_frame_is_rejected(self):
        snapshot = make_snapshot("terra-001", 0, 0.0)
        snapshot.reference_frame = pb.REFERENCE_FRAME_UNSPECIFIED
        with self.assertRaises(ValueError):
            validate_snapshot(snapshot)

    def test_non_normalized_quaternion_is_rejected(self):
        snapshot = make_snapshot("terra-001", 0, 0.0)
        snapshot.attitude.w = 2.0
        with self.assertRaises(ValueError):
            validate_snapshot(snapshot)


if __name__ == "__main__":
    unittest.main()
