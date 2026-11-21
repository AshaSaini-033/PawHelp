import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from matching import find_overdue_points, suggest_matches
from validation import validate_row


class PawHelpEngineTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 11, 21, 12, 0)
        self.point = {
            "point_id": "FP-1", "area_label": "Campus Gate", "food_type_needed": "Dry dog food",
            "quantity_needed": "2", "quantity_unit": "kg", "last_confirmed_visit": "2026-11-20 08:00",
            "visit_interval_hours": "24", "feeder_alias": "Feeder A", "status": "active", "notes": "Observed with feeder",
        }
        self.offer = {
            "offer_id": "OF-1", "area_label": "Campus Gate", "food_type": "Dry dog food",
            "quantity": "2.5", "quantity_unit": "kg", "available_until": "2026-11-21 18:00",
            "donor_alias": "Donor B", "status": "available", "notes": "Sealed pack",
        }
        self.volunteer = {
            "volunteer_id": "VL-1", "area_label": "Campus Gate", "available_from": "2026-11-21 11:00",
            "available_until": "2026-11-21 14:00", "volunteer_alias": "Volunteer C", "status": "available",
        }

    def test_compatible_records_create_candidate_match(self):
        matches = suggest_matches([self.point], [self.offer], [self.volunteer], self.now)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["point_id"], "FP-1")
        self.assertEqual(matches[0]["priority"], "Overdue")

    def test_area_must_match(self):
        self.offer["area_label"] = "Different area"
        self.assertEqual(suggest_matches([self.point], [self.offer], [self.volunteer], self.now), [])

    def test_quantity_unit_must_match(self):
        self.offer["quantity_unit"] = "portions"
        self.assertEqual(suggest_matches([self.point], [self.offer], [self.volunteer], self.now), [])

    def test_unavailable_volunteer_means_no_match(self):
        self.volunteer["available_until"] = "2026-11-21 11:30"
        self.assertEqual(suggest_matches([self.point], [self.offer], [self.volunteer], self.now), [])

    def test_due_point_is_reported_overdue(self):
        overdue = find_overdue_points([self.point], self.now)
        self.assertEqual(overdue[0]["point_id"], "FP-1")
        self.assertGreater(overdue[0]["hours_overdue"], 0)

    def test_invalid_positive_quantity_is_rejected(self):
        bad = {
            "record_type": "feeding_point", "record_id": "FP-2", "recorded_at": "2026-11-21 10:00",
            "area_label": "Campus Gate", "food_type": "Dry dog food", "quantity": "0", "quantity_unit": "kg",
            "last_confirmed_visit": "2026-11-20 08:00", "visit_interval_hours": "24", "available_from": "",
            "available_until": "", "valid_until": "", "person_alias": "Feeder A", "status": "active", "notes": "",
        }
        errors = validate_row(bad)
        self.assertTrue(any("greater than zero" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
